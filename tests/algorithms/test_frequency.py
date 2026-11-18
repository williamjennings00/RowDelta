"""Executable contract for Assignment 1: frequency counting."""

import pytest

from rowdelta.algorithms.frequency import count_identifier_frequencies


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], {}),
        (["a", "b", "a"], {"a": 2, "b": 1}),
        ([7, 7, 9], {7: 2, 9: 1}),
        ([("team", 1), ("team", 2), ("team", 1)], {("team", 1): 2, ("team", 2): 1}),
    ],
)
def test_counts_identifiers(values: list[object], expected: dict[object, int]) -> None:
    assert count_identifier_frequencies(values) == expected


def test_accepts_one_shot_iterable_and_preserves_first_seen_order() -> None:
    values = (item for item in ["z", "a", "z", "b", "a"])

    result = count_identifier_frequencies(values)

    assert result == {"z": 2, "a": 2, "b": 1}
    assert list(result) == ["z", "a", "b"]
