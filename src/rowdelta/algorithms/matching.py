"""Primary-key record-matching assignment."""

from collections.abc import Iterable, Mapping


def match_records_by_key(
    left_records: Iterable[Mapping[str, str]],
    right_records: Iterable[Mapping[str, str]],
    key: str,
) -> list[tuple[Mapping[str, str], Mapping[str, str]]]:
    """Pair records from two datasets when their primary-key values match.

    Args:
        left_records: Records from the first dataset.
        right_records: Records from the second dataset.
        key: The non-empty field name containing each record's primary key.

    Returns:
        Pairs of matching records, with the left dataset's record first in
        each pair. Pairs are ordered by the records' appearance in
        ``left_records``. Records without a counterpart are omitted. Key
        values are compared exactly as supplied, including case and spaces.

    Examples:
        >>> left = [{"id": "a", "name": "Ada"}, {"id": "b", "name": "Lin"}]
        >>> right = [{"id": "b", "name": "Linus"}, {"id": "a", "name": "Ada L."}]
        >>> match_records_by_key(left, right, "id")
        [({'id': 'a', 'name': 'Ada'}, {'id': 'a', 'name': 'Ada L.'}),
         ({'id': 'b', 'name': 'Lin'}, {'id': 'b', 'name': 'Linus'})]

    Assignment acceptance criteria:
        - Pair records only when both have the same value for ``key``.
        - Preserve left-side input order in the returned pairs.
        - Omit unmatched records; identifying them is a later assignment.
        - Reject an empty key name, a record missing the key field, an empty
          string key value, or a repeated key value in either dataset with
          ``ValueError``.
        - Consume each iterable at most once and do not mutate input records.
        - Return an empty list when both inputs are empty and the key name is
          valid.

    Raises:
        ValueError: If ``key`` is empty, a record lacks that field, a
            primary-key value is empty, or a primary-key value is repeated
            within either dataset.

    Complexity:
        Expected O(L + R) time and O(L + R) extra space for L left-side and
        R right-side records.
    """
    if not key:
        raise ValueError("key must be a non-empty field name")

    right_by_key: dict[str, Mapping[str, str]] = {}
    for record_number, record in enumerate(right_records, start=1):
        if key not in record:
            raise ValueError(f"right record {record_number} is missing key {key!r}")

        record_key = record[key]
        if record_key == "":
            raise ValueError(f"right record {record_number} has an empty key {key!r}")
        if record_key in right_by_key:
            raise ValueError(f"duplicate key {record_key!r} in right records")

        right_by_key[record_key] = record

    seen_left_keys: set[str] = set()
    matches: list[tuple[Mapping[str, str], Mapping[str, str]]] = []
    for record_number, record in enumerate(left_records, start=1):
        if key not in record:
            raise ValueError(f"left record {record_number} is missing key {key!r}")

        record_key = record[key]
        if record_key == "":
            raise ValueError(f"left record {record_number} has an empty key {key!r}")
        if record_key in seen_left_keys:
            raise ValueError(f"duplicate key {record_key!r} in left records")

        seen_left_keys.add(record_key)
        if record_key in right_by_key:
            matches.append((record, right_by_key[record_key]))

    return matches
