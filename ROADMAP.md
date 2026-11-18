# RowDelta roadmap

Assignments are deliberately introduced one at a time. Only the current assignment is prepared in code and tests.

## Completed

- Repository foundation: Python packaging, Typer/Rich CLI, logging setup, strict mypy, Ruff, pytest/Hypothesis configuration, CI, MIT license.
- `rowdelta validate-csv`: validates a header and consistent field counts.
- Synthetic CSV fixture and deterministic benchmark data generator.

## Current assignment

3. **Match records by primary key** — implement `match_records_by_key(left_records: Iterable[Mapping[str, str]], right_records: Iterable[Mapping[str, str]], key: str) -> list[tuple[Mapping[str, str], Mapping[str, str]]]` in `src/rowdelta/algorithms/matching.py`. This will pair rows across CSV snapshots so later assignments can report changed records. Assignment contract and tests are in that module and `tests/algorithms/test_matching.py`.

## Completed assignments

1. **Frequency counting** — `count_identifier_frequencies(identifiers: Iterable[Hashable]) -> dict[Hashable, int]` in `src/rowdelta/algorithms/frequency.py`. Uses `Counter` and supports one-shot iterables. Contract tests are in `tests/algorithms/test_frequency.py`.
2. **Duplicate detection** — `find_duplicate_identifiers(identifiers: Iterable[Hashable]) -> list[Hashable]` in `src/rowdelta/algorithms/duplicates.py`. Reports repeated identifiers once, in the order they become duplicates. Contract tests are in `tests/algorithms/test_duplicates.py`.

## Upcoming assignments

4. Detecting added and removed records.
5. Comparing sorted datasets using two pointers.
6. Finding the top K most frequently modified columns.
7. Binary search over sorted records.
8. K-way merging of sorted datasets.
9. External merge sort.
10. Sliding-window anomaly detection where applicable.
11. Edit distance for optional fuzzy record matching.
12. Memory-efficient streaming algorithms.
