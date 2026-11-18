"""Generate deterministic synthetic CSV data for manual benchmarks."""

import argparse
import csv
from pathlib import Path


def generate_csv(output: Path, rows: int) -> None:
    """Write ``rows`` synthetic customer records to OUTPUT."""
    if rows < 0:
        raise ValueError("rows must be non-negative")
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["customer_id", "region", "status"])
        regions = ("north", "south", "east", "west")
        statuses = ("active", "inactive")
        for index in range(rows):
            writer.writerow((f"C{index:09d}", regions[index % 4], statuses[index % 2]))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("--rows", type=int, default=1_000_000)
    args = parser.parse_args()
    generate_csv(args.output, args.rows)


if __name__ == "__main__":
    main()
