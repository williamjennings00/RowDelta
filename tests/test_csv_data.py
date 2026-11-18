"""Smoke test the deterministic synthetic CSV fixture."""

import csv
from pathlib import Path


def test_synthetic_fixture_has_header_and_rows() -> None:
    fixture = Path(__file__).parent / "data" / "synthetic_customers.csv"
    with fixture.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    assert len(rows) == 5
    assert {"customer_id", "region", "status"} <= set(rows[0])
