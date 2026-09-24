"""Optional LLM classifier for changelog entries.

The Anthropic SDK is an optional extra, so the core validators and the
metadata-driven generators keep working without it:

    uv pip install 'pawsql-doc[llm]'

Credentials resolve the standard way (``ANTHROPIC_API_KEY`` or an ``ant auth
login`` profile); no key is read or stored by this module.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from pawsql_doc.changelog import ChangeSource, Classifier, Commit
from pawsql_doc.models.changelog import ClassifiedPayload

PROMPT_VERSION = "changelog-classify-1"
DEFAULT_MODEL = "claude-opus-5"
MAX_TOKENS = 16000
MAX_BODY_CHARS = 600
MAX_FILES = 12

SYSTEM_PROMPT = """你在为 PawSQL 的产品文档站整理「变更日志」。输入是某个发布区间内的 git 提交列表。

只依据输入中的提交信息判断，不得补充输入里没有的事实：
- 不得新增或推断 API 名称、参数、配置项、版本号、性能数字、客户名与案例。
- 只有提交信息里明确写出某个数据库名（例如 MySQL、Oracle、PostgreSQL、达梦、openGauss），才可归入 database-support。
- 不得把「修复了某处」改写成功能承诺；不确定对外影响的归入 internal。
- 每条条目一句话，保留提交的原始语言，不要翻译；不要输出 Markdown、链接或 HTML。
- 不要为凑数而改写、拆分或合并不同的改动。

分类取值（sections 的 category，也是条目 tags 的取值域）：
- 审核引擎：审核规则的新增、调整与缺陷修复。
- 优化算法：重写规则、查询折叠、解关联、谓词下推、代价模型等优化算法相关。
- 索引引擎：索引推荐、索引分析、索引清理、indexonly 判断相关。
- SQL解析与数据库支持：SQL 解析器与语法、脚本解析、以及对某个数据库（如 MySQL、Oracle、达梦、TDSQL、Hive、DB2、SQL Server）的支持。
- 缺陷修复：无法归入上述子系统的缺陷修复。
- internal：内部重构、依赖升级、构建与工程改动，文档读者不需要知道。

条目还要给 tags：与 category 同域（不含 internal），可多值 —— 一个位于某子系统的缺陷修复应同时挂该子系统与「缺陷修复」。

sourceCommits 只能使用输入中出现的短哈希，不得编造。按 schema 输出 JSON。"""


class LlmError(RuntimeError):
    """The classifier could not produce a validated payload."""


@dataclass(frozen=True)
class LlmConfig:
    model: str = DEFAULT_MODEL
    timeout: float = 120.0
    baseUrl: str | None = None

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> LlmConfig:
        environ = os.environ if env is None else env
        timeout = environ.get("PAWSQL_CHANGELOG_LLM_TIMEOUT")
        return cls(
            model=environ.get("PAWSQL_CHANGELOG_LLM_MODEL", DEFAULT_MODEL),
            timeout=float(timeout) if timeout else 120.0,
            baseUrl=environ.get("PAWSQL_CHANGELOG_LLM_BASE_URL") or None,
        )


def make_client(config: LlmConfig, anthropic_module: Any = None) -> Any:
    if anthropic_module is None:
        try:
            import anthropic as anthropic_module  # type: ignore[no-redef]
        except ImportError as exc:
            raise LlmError(
                "未安装 Anthropic SDK，无法调用 LLM 归类；请先执行 uv pip install 'pawsql-doc[llm]'"
            ) from exc
    kwargs: dict[str, Any] = {"timeout": config.timeout}
    if config.baseUrl:
        kwargs["base_url"] = config.baseUrl
    return anthropic_module.Anthropic(**kwargs)


def _commit_payload(commit: Commit) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "short": commit.short,
        "date": commit.date,
        "subject": commit.subject,
    }
    body = commit.body.strip()
    if body:
        payload["body"] = body[:MAX_BODY_CHARS]
    if commit.files:
        payload["files"] = list(commit.files[:MAX_FILES])
    return payload


def render_user_prompt(source: ChangeSource, commits: Sequence[Commit]) -> str:
    payload = {
        "component": source.name,
        "componentLabel": dict(source.displayName),
        "commits": [_commit_payload(commit) for commit in commits],
    }
    return "以下 JSON 是本次发布区间的提交列表：\n\n" + json.dumps(
        payload, ensure_ascii=False, indent=2, sort_keys=True
    )


def classify_with_client(
    client: Any,
    config: LlmConfig,
    source: ChangeSource,
    commits: Sequence[Commit],
) -> ClassifiedPayload:
    """One structured-output call; the class docstring's discipline lives in the prompt."""
    response = client.messages.parse(
        model=config.model,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": render_user_prompt(source, commits)}],
        output_format=ClassifiedPayload,
    )
    stop_reason = getattr(response, "stop_reason", None)
    if stop_reason == "refusal":
        raise LlmError(f"{source.name}: 模型拒绝了本次归类请求（stop_reason=refusal）")
    if stop_reason == "max_tokens":
        raise LlmError(
            f"{source.name}: 归类结果被 max_tokens 截断，请拆分区间或提高 MAX_TOKENS"
        )
    parsed = getattr(response, "parsed_output", None)
    if parsed is None:
        raise LlmError(f"{source.name}: 模型未返回符合 schema 的 JSON")
    if isinstance(parsed, ClassifiedPayload):
        return parsed
    return ClassifiedPayload.model_validate(parsed)


def build_classifier(config: LlmConfig | None = None, client: Any = None) -> Classifier:
    """A :class:`Classifier` bound to one client, tagged with its cache identity."""
    resolved = config or LlmConfig.from_env()
    client = client if client is not None else make_client(resolved)

    def classify(source: ChangeSource, commits: Sequence[Commit]) -> ClassifiedPayload:
        return classify_with_client(client, resolved, source, commits)

    return Classifier(model=resolved.model, promptVersion=PROMPT_VERSION, classify=classify)


__all__ = [
    "DEFAULT_MODEL",
    "LlmConfig",
    "LlmError",
    "PROMPT_VERSION",
    "SYSTEM_PROMPT",
    "build_classifier",
    "classify_with_client",
    "make_client",
    "render_user_prompt",
]
