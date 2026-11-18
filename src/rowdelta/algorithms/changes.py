"""Added and removed identifier assignment."""

from collections.abc import Hashable, Iterable


def find_added_and_removed_identifiers(
    before: Iterable[Hashable],
    after: Iterable[Hashable],
) -> tuple[list[Hashable], list[Hashable]]:
    """Find identifiers present in only one of two dataset snapshots.

    Args:
        before: Identifiers from the earlier dataset snapshot.
        after: Identifiers from the later dataset snapshot.

    Returns:
        A pair ``(added, removed)``. ``added`` contains identifiers found only
        in ``after``, ordered by their first appearance there. ``removed``
        contains identifiers found only in ``before``, ordered by their first
        appearance there. Repeated identifiers in an input contribute at most
        one output entry.

    Examples:
        >>> find_added_and_removed_identifiers(["a", "b"], ["b", "c"])
        (['c'], ['a'])
        >>> find_added_and_removed_identifiers([], [7, 7, 9])
        ([7, 9], [])
        >>> find_added_and_removed_identifiers([], [])
        ([], [])

    Assignment acceptance criteria:
        - Return additions first and removals second.
        - Include each identifier only when it occurs in one snapshot and not
          the other.
        - Preserve first-seen order from the corresponding input.
        - Include each changed identifier at most once, even if an input
          contains repeats.
        - Consume each iterable at most once and do not mutate either input.
        - Return two empty lists when both inputs are empty.

    Raises:
        TypeError: If an input item is not hashable.

    This function is intentionally unimplemented as the current learning
    assignment. Do not replace the placeholder until implementing the task.
    """
    raise NotImplementedError("Assignment 4: implement added and removed identifier detection")
