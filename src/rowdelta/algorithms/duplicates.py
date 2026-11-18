"""Duplicate-identifier assignment for record-key validation."""

from collections.abc import Hashable, Iterable


def find_duplicate_identifiers(identifiers: Iterable[Hashable]) -> list[Hashable]:
    """Return identifiers that occur more than once in the input.

    Args:
        identifiers: Any iterable of hashable identifiers. It may be one-shot
            (such as a generator) and may be empty.

    Returns:
        Each identifier that appears at least twice, listed once. The order is
        determined by when each identifier appears for the second time. Empty
        input or input with no repeats returns an empty list.

    Examples:
        >>> find_duplicate_identifiers(["a", "b", "a", "b", "a"])
        ['a', 'b']
        >>> find_duplicate_identifiers(iter([7, 9, 7]))
        [7]
        >>> find_duplicate_identifiers([])
        []

    Assignment acceptance criteria:
        - Return each repeated identifier once, even if it occurs three or
          more times.
        - Preserve the order in which identifiers first become duplicates.
        - Consume a one-shot iterable only once.
        - Return an empty list for empty input or input with no duplicates.
        - Do not mutate the input or retain unrelated state between calls.

    Raises:
        TypeError: If an input item is not hashable.

    Complexity:
        Expected O(n) time for n identifiers and O(u) extra space for u
        distinct identifiers.
    """
    frequency: dict[Hashable, int] = {}
    duplicates: list[Hashable] = []
    for x in identifiers:
        if x in frequency:
            frequency[x] += 1
            if frequency[x] == 2:
                duplicates.append(x)
        else:
            frequency[x] = 1

    return duplicates

