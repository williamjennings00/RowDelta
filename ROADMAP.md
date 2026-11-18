# RowDelta roadmap

Assignments are deliberately introduced one at a time. Only the current assignment is prepared in code and tests.

## Completed

- Repository foundation: Python packaging, Typer/Rich CLI, logging setup, strict mypy, Ruff, pytest/Hypothesis configuration, CI, MIT license.
- `rowdelta validate-csv`: validates a header and consistent field counts.
- Synthetic CSV fixture and deterministic benchmark data generator.

## Current assignment

1. **Frequency counting** — implement `count_identifier_frequencies(identifiers: Iterable[Hashable]) -> dict[Hashable, int]` in `src/rowdelta/algorithms/frequency.py`. This will support later record-key analysis and deterministic summaries. Assignment contract and tests are in that module and `tests/algorithms/test_frequency.py`.

## Upcoming assignments

2. Duplicate detection using sets.
3. Matching records by primary key.
4. Detecting added and removed records.
5. Comparing sorted datasets using two pointers.
6. Finding the top K most frequently modified columns.
7. Binary search over sorted records.
8. K-way merging of sorted datasets.
9. External merge sort.
10. Sliding-window anomaly detection where applicable.
11. Edit distance for optional fuzzy record matching.
12. Memory-efficient streaming algorithms.
