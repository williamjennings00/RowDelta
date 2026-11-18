"""Frequency-counting assignment for record identifiers."""

from collections.abc import Hashable, Iterable
from collections import Counter

def count_identifier_frequencies(
    identifiers: Iterable[Hashable],
) -> dict[Hashable, int]:
    """Count how often each hashable record identifier occurs.

    Args:
        identifiers: Any iterable of hashable identifiers. The iterable may be
            one-shot (such as a generator) and may be empty.

    Returns:
        A dictionary mapping each distinct identifier to its number of
        occurrences. Each returned count is a positive integer. Empty input
        returns an empty dictionary. Dictionary iteration order should follow
        the first appearance of each identifier for deterministic output.

    Examples:
        >>> count_identifier_frequencies(["a", "b", "a"])
        {'a': 2, 'b': 1}
        >>> count_identifier_frequencies(iter([7, 7, 9]))
        {7: 2, 9: 1}
        >>> count_identifier_frequencies([])
        {}

    Assignment acceptance criteria:
        - Count each identifier exactly, including repeated and mixed hashable
          values such as strings, integers, and tuples.
        - Consume an input iterable only once; do not require it to be sized or
          reusable.
        - Return an empty dictionary for empty input.
        - Preserve first-seen order in the returned dictionary.
        - Do not mutate the input or retain unrelated state between calls.

    Raises:
        TypeError: If an input item is not hashable.

    This function is intentionally unimplemented as the current learning
    assignment. Do not replace the placeholder until implementing the task.
    """
    
    return Counter(identifiers)
    
