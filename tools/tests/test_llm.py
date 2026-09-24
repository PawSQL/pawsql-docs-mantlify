from __future__ import annotations

import re
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from pawsql_doc import changelog as cl
from pawsql_doc import llm
from pawsql_doc.models.changelog import ClassifiedEntry, ClassifiedPayload, ClassifiedSection

SOURCE = cl.ChangeSource(
    name="server",
    displayName={"zh": "服务端", "en": "Server"},
    repo=Path("E:/gitrepo/pawsql-server"),
    trunk="main",
    tagPattern=re.compile(r"^release-v(?P<version>[0-9]+\.[0-9]+\.[0-9]+)$"),
)

COMMIT = cl.Commit(
    sha="a" * 40,
    short="abc1234",
    date="2026-09-01",
    author="tomas",
    subject="feat: 新增匿名 key",
    files=("src/A.java",),
)

PAYLOAD = ClassifiedPayload(
    sections=[
        ClassifiedSection(
            category="审核引擎",
            entries=[ClassifiedEntry(text="新增匿名 key", sourceCommits=["abc1234"], tags=["审核引擎"])],
        )
    ]
)


class FakeMessages:
    def __init__(self, response):
        self.response = response
        self.kwargs = None

    def parse(self, **kwargs):
        self.kwargs = kwargs
        return self.response


def client_returning(response):
    messages = FakeMessages(response)
    return SimpleNamespace(messages=messages), messages


# ---------------------------------------------------------------------------
# configuration
# ---------------------------------------------------------------------------


def test_from_env_defaults_to_opus_5():
    config = llm.LlmConfig.from_env({})

    assert config.model == "claude-opus-5"
    assert config.timeout == 120.0
    assert config.baseUrl is None


def test_from_env_reads_overrides():
    config = llm.LlmConfig.from_env(
        {
            "PAWSQL_CHANGELOG_LLM_MODEL": "claude-haiku-4-5",
            "PAWSQL_CHANGELOG_LLM_TIMEOUT": "30",
            "PAWSQL_CHANGELOG_LLM_BASE_URL": "https://gateway.internal",
        }
    )

    assert config.model == "claude-haiku-4-5"
    assert config.timeout == 30.0
    assert config.baseUrl == "https://gateway.internal"


def test_make_client_without_sdk_points_at_the_extra(monkeypatch):
    monkeypatch.setitem(sys.modules, "anthropic", None)

    with pytest.raises(llm.LlmError) as excinfo:
        llm.make_client(llm.LlmConfig())

    assert "pawsql-doc[llm]" in str(excinfo.value)


def test_make_client_passes_timeout_and_base_url():
    captured = {}

    def factory(**kwargs):
        captured.update(kwargs)
        return "client"

    module = SimpleNamespace(Anthropic=factory)
    client = llm.make_client(llm.LlmConfig(timeout=5.0, baseUrl="https://gw"), anthropic_module=module)

    assert client == "client"
    assert captured == {"timeout": 5.0, "base_url": "https://gw"}


# ---------------------------------------------------------------------------
# prompt
# ---------------------------------------------------------------------------


def test_render_user_prompt_includes_commits_and_truncates_long_body():
    commit = cl.Commit(
        sha="a" * 40,
        short="abc1234",
        date="2026-09-01",
        author="tomas",
        subject="feat: 巡检慢查询AI优化功能",
        body="x" * (llm.MAX_BODY_CHARS + 200),
        files=("src/A.java",),
    )

    prompt = llm.render_user_prompt(SOURCE, [commit])

    assert "feat: 巡检慢查询AI优化功能" in prompt
    assert "abc1234" in prompt
    assert "src/A.java" in prompt
    assert len(prompt) < llm.MAX_BODY_CHARS + 1000


def test_render_user_prompt_omits_empty_body():
    commit = cl.Commit("a" * 40, "abc1234", "2026-09-01", "tomas", "feat: 改", body="  ")

    prompt = llm.render_user_prompt(SOURCE, [commit])

    assert '"body"' not in prompt


# ---------------------------------------------------------------------------
# classification
# ---------------------------------------------------------------------------


def test_classify_with_client_returns_validated_payload():
    client, messages = client_returning(SimpleNamespace(parsed_output=PAYLOAD, stop_reason="end_turn"))

    payload = llm.classify_with_client(client, llm.LlmConfig(), SOURCE, [COMMIT])

    assert payload is PAYLOAD
    assert messages.kwargs["model"] == "claude-opus-5"
    assert messages.kwargs["output_format"] is ClassifiedPayload
    assert messages.kwargs["max_tokens"] == llm.MAX_TOKENS
    assert "不得新增" in llm.SYSTEM_PROMPT


def test_classify_with_client_accepts_a_plain_mapping():
    client, _ = client_returning(
        SimpleNamespace(parsed_output=PAYLOAD.model_dump(mode="json"), stop_reason="end_turn")
    )

    payload = llm.classify_with_client(client, llm.LlmConfig(), SOURCE, [COMMIT])

    assert payload.sections[0].entries[0].text == "新增匿名 key"


def test_classify_with_client_rejects_refusal_and_truncation():
    refusing, _ = client_returning(SimpleNamespace(parsed_output=None, stop_reason="refusal"))
    truncated, _ = client_returning(SimpleNamespace(parsed_output=PAYLOAD, stop_reason="max_tokens"))
    empty, _ = client_returning(SimpleNamespace(parsed_output=None, stop_reason="end_turn"))

    for client in (refusing, truncated, empty):
        with pytest.raises(llm.LlmError):
            llm.classify_with_client(client, llm.LlmConfig(), SOURCE, [COMMIT])


def test_build_classifier_tags_the_cache_identity():
    client, _ = client_returning(SimpleNamespace(parsed_output=PAYLOAD, stop_reason="end_turn"))

    classifier = llm.build_classifier(llm.LlmConfig(model="claude-sonnet-5"), client=client)
    payload = classifier(SOURCE, [COMMIT])

    assert classifier.model == "claude-sonnet-5"
    assert classifier.promptVersion == llm.PROMPT_VERSION
    assert payload.sections[0].entries[0].sourceCommits == ["abc1234"]
