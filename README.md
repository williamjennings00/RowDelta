# RowDelta

RowDelta is an early-stage command-line utility for comparing, validating, and analyzing CSV datasets. Its long-term direction is to support datasets larger than available memory, but that capability has not been implemented or benchmarked yet.

## Status

This project is in pre-alpha. The `validate-csv` command and packaging/quality infrastructure are implemented. Record comparison and analysis are not implemented. The current learning assignment is primary-key matching; see [ROADMAP.md](ROADMAP.md).

## Requirements

- Python 3.12 or newer

## Install for development

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

## Usage

```bash
rowdelta --help
rowdelta version
rowdelta validate-csv customers.csv
rowdelta --verbose validate-csv customers.csv
```

CSV validation checks that the file can be decoded, has a header, and each data row has the same number of fields as that header. It does not validate business-specific schemas or compare datasets.

## Development checks

```bash
ruff check .
ruff format --check .
mypy src
pytest
```

CI runs these checks on Python 3.12. The initial algorithm assignment tests that are not yet applicable are marked as skipped; a test confirms that the assignment remains explicitly unimplemented.

## Synthetic data and benchmarks

A small synthetic fixture lives at `tests/data/synthetic_customers.csv`. Generate a larger deterministic synthetic CSV with:

```bash
python benchmarks/generate_csv.py /tmp/rowdelta-customers.csv --rows 1000000
```

The generator is infrastructure only; no performance claims are made based on it.

## License

MIT. See [LICENSE](LICENSE).
