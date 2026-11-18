"""Command-line entry point for RowDelta."""

import logging
from pathlib import Path

import typer
from rich.console import Console

from rowdelta import __version__

app = typer.Typer(
    name="rowdelta",
    help="Compare, validate, and analyze CSV datasets.",
    no_args_is_help=True,
    pretty_exceptions_enable=False,
)
console = Console()


@app.callback()
def configure_logging(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show diagnostic logging."),
) -> None:
    """Configure process-wide logging for CLI commands."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format="%(levelname)s: %(message)s",
    )


@app.command()
def version() -> None:
    """Show the installed RowDelta version."""
    console.print(f"RowDelta {__version__}")


@app.command()
def validate_csv(
    path: Path = typer.Argument(..., exists=True, dir_okay=False, readable=True),
    encoding: str = typer.Option("utf-8-sig", help="Text encoding used to read the CSV."),
) -> None:
    """Check that PATH is readable as a CSV with a header and consistent row widths."""
    import csv

    try:
        with path.open("r", encoding=encoding, newline="") as stream:
            reader = csv.reader(stream, strict=True)
            header = next(reader, None)
            if header is None:
                raise ValueError("CSV file is empty and has no header")
            if not header:
                raise ValueError("CSV header has no columns")
            for row in reader:
                if len(row) != len(header):
                    raise ValueError(
                        f"row {reader.line_num} has {len(row)} fields; expected {len(header)}"
                    )
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        console.print(f"[red]Invalid CSV:[/red] {exc}")
        raise typer.Exit(code=2) from exc

    console.print(f"[green]Valid CSV[/green]: {path} ({len(header)} columns)")
