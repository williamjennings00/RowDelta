"""Executable contract for Assignment 3: primary-key record matching."""

import pytest

from rowdelta.algorithms.matching import match_records_by_key


@pytest.mark.skip(reason="Assignment 3: implement match_records_by_key first")
def test_matches_records_in_left_input_order_and_omits_unmatched() -> None:
    left = [
        {"id": "c", "name": "Casey"},
        {"id": "a", "name": "Ari"},
        {"id": "unmatched-left", "name": "Morgan"},
    ]
    right = [
        {"id": "a", "name": "Ari second snapshot"},
        {"id": "unmatched-right", "name": "Sam"},
        {"id": "c", "name": "Casey second snapshot"},
    ]

    assert match_records_by_key(left, right, "id") == [
        (left[0], right[2]),
        (left[1], right[0]),
    ]


@pytest.mark.skip(reason="Assignment 3: implement match_records_by_key first")
@pytest.mark.parametrize(
    ("left", "right"),
    [
        ([{"id": "x"}, {"id": "x"}], [{"id": "x"}]),
        ([{"id": "x"}], [{"id": "x"}, {"id": "x"}]),
    ],
)
def test_rejects_duplicate_keys(
    left: list[dict[str, str]], right: list[dict[str, str]]
) -> None:
    with pytest.raises(ValueError):
        match_records_by_key(left, right, "id")


@pytest.mark.skip(reason="Assignment 3: implement match_records_by_key first")
@pytest.mark.parametrize(
    ("left", "right", "key"),
    [
        ([{"name": "Ari"}], [], "id"),
        ([], [{"name": "Ari"}], "id"),
        ([], [], ""),
    ],
)
def test_rejects_missing_or_empty_key(
    left: list[dict[str, str]], right: list[dict[str, str]], key: str
) -> None:
    with pytest.raises(ValueError):
        match_records_by_key(left, right, key)


@pytest.mark.skip(reason="Assignment 3: implement match_records_by_key first")
@pytest.mark.parametrize(
    ("left", "right"),
    [
        ([{"id": ""}], []),
        ([], [{"id": ""}]),
        ([{"id": ""}, {"id": ""}], []),
        ([], [{"id": ""}, {"id": ""}]),
    ],
)
def test_rejects_empty_or_repeated_empty_key_values(
    left: list[dict[str, str]], right: list[dict[str, str]]
) -> None:
    with pytest.raises(ValueError):
        match_records_by_key(left, right, "id")


def test_assignment_placeholder_is_explicit() -> None:
    with pytest.raises(NotImplementedError, match="Assignment 3"):
        match_records_by_key([], [], "id")
