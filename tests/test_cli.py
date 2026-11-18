from typer.testing import CliRunner

from rowdelta.cli import app


def test_version_command() -> None:
    result = CliRunner().invoke(app, ["version"])
    assert result.exit_code == 0
    assert "RowDelta 0.1.0" in result.output


def test_validate_csv_accepts_consistent_csv(tmp_path) -> None:
    path = tmp_path / "valid.csv"
    path.write_text("id,name\n1,Ada\n2,Grace\n", encoding="utf-8")

    result = CliRunner().invoke(app, ["validate-csv", str(path)])

    assert result.exit_code == 0
    assert "Valid CSV" in result.output


def test_validate_csv_rejects_inconsistent_width(tmp_path) -> None:
    path = tmp_path / "invalid.csv"
    path.write_text("id,name\n1,Ada\n2\n", encoding="utf-8")

    result = CliRunner().invoke(app, ["validate-csv", str(path)])

    assert result.exit_code == 2
    assert "Invalid CSV" in result.output
