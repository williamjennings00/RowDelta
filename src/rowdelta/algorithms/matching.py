"""Primary-key record-matching assignment."""

from collections.abc import Iterable, Mapping
from collections import Counter

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

 
    """
    match_records_by_key = []
    dict_right_records = {}

    for index, value in enumerate(right_records):
        if value[key] in dict_right_records:
            raise ValueError
        else:
            dict_right_records[value[key]] = value




    for index, value in enumerate(left_records):
        if value[key] in dict_right_records:
            match_records_by_key.append((value,dict_right_records[value[key]]))

    duplicate = set()
    for index, value in enumerate(match_records_by_key):
        if value[0][key] in duplicate or value[1][key] in duplicate:
            raise ValueError
        else:
            duplicate.add(value[0][key])

        if value[0][key] == "" or value[1][key] == "":
            raise ValueError

        if value[0] == "" or value[1] == "":
            raise ValueError

        if value[0][key] != value[1][key]:
            raise ValueError


    return match_records_by_key
    
