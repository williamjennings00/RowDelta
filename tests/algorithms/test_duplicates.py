"""Executable contract for Assignment 2: duplicate identifier detection."""

import pytest

from rowdelta.algorithms.duplicates import find_duplicate_identifiers


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        (["a", "b", "c"], []),
        (["a", "b", "a"], ["a"]),
        (["a", "b", "a", "b", "a"], ["a", "b"]),
        ([("team", 1), ("team", 2), ("team", 1)], [("team", 1)]),
    ],
)
def test_finds_duplicate_identifiers(
    values: list[object], expected: list[object]
) -> None:
    assert find_duplicate_identifiers(values) == expected


def test_accepts_one_shot_iterable_and_orders_by_second_appearance() -> None:
    values = (item for item in ["z", "a", "z", "b", "a", "b"])

    assert find_duplicate_identifiers(values) == ["z", "a", "b"]


