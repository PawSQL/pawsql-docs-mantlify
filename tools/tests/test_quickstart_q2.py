"""Smoke-test the tutorial dataset, not PawSQL or PostgreSQL performance."""
from pathlib import Path
import re
import sqlite3


def test_q2_quickstart_dataset_and_regional_ties():
    page = Path(__file__).resolve().parents[2] / "docs/getting-started/quickstart.mdx"
    blocks = re.findall(r"```sql\n(.*?)```", page.read_text(encoding="utf-8"), re.S)
    assert len(blocks) == 2
    connection = sqlite3.connect(":memory:")
    try:
        connection.execute("PRAGMA foreign_keys=ON")
        connection.executescript(blocks[0])
        rows = connection.execute(blocks[1]).fetchall()
        assert [row[:4] for row in rows] == [
            (2000, "Supplier Bravo", "FRANCE", 1),
            (1000, "Supplier Alpha", "GERMANY", 1),
        ]
        # A global minimum incorrectly discards both eligible European suppliers.
        wrong = blocks[1].replace("AND r_min.r_name = 'EUROPE'", "")
        assert connection.execute(wrong).fetchall() == []
    finally:
        connection.close()
