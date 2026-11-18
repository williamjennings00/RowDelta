"""Executable contract for Assignment 4: added and removed identifiers."""

import pytest

from rowdelta.algorithms.changes import find_added_and_removed_identifiers


@pytest.mark.skip(reason="Assignment 4: implement find_added_and_removed_identifiers first")
@pytest.mark.parametrize(
    ("before", "after", "expected"),
    [
        ([], [], ([], [])),
        (["a", "b"], ["a", "b"], ([], [])),
        (["a", "b"], ["b", "c"], (["c"], ["a"])),
        (["a", "b", "c"], ["d", "c", "b"], (["d"], ["a"])),
        ([7, 8], [8, 9], ([9], [7])),
    ],
)
def test_finds_added_and_removed_identifiers(
    before: list[object], after: list[object], expected: tuple[list[object], list[object]]
) -> None:
    assert find_added_and_removed_identifiers(before, after) == expected


@pytest.mark.skip(reason="Assignment 4: implement find_added_and_removed_identifiers first")
def test_preserves_first_seen_order_and_ignores_repeated_input_ids() -> None:
    before = (item for item in ["x", "a", "x", "b"])
    after = (item for item in ["y", "a", "y", "z", "z"])

    assert find_added_and_removed_identifiers(before, after) == (["y", "z"], ["x", "b"])


def test_assignment_placeholder_is_explicit() -> None:
    with pytest.raises(NotImplementedError, match="Assignment 4"):
        find_added_and_removed_identifiers([], [])
