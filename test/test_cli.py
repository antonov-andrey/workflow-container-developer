"""Tests for the workflow-container-developer CLI."""

from pathlib import Path

import pytest

from workflow_container_developer.cli import main


def _developer_path_create(tmp_path: Path) -> Path:
    """Create a developer checkout fixture.

    Args:
        tmp_path: Temporary test root.

    Returns:
        Developer path.
    """

    developer_path = tmp_path / "workflow-container-developer"
    developer_path.mkdir()
    return developer_path


def test_cli_help_lists_supported_commands(tmp_path: Path, capsys) -> None:
    """Show help text with the supported command set."""

    developer_path = _developer_path_create(tmp_path)

    with pytest.raises(SystemExit) as error:
        main(["--developer-path", str(developer_path), "--help"])

    assert error.value.code == 0

    captured = capsys.readouterr()
    assert "{list}" in captured.out
    assert "audit" not in captured.out
    assert "--version" not in captured.out


def test_cli_list_outputs_adjacent_project(tmp_path: Path, capsys) -> None:
    """List adjacent workflow-container projects."""

    developer_path = tmp_path / "workflow-container-developer"
    developer_path.mkdir()
    target_path = tmp_path / "sample-container"
    target_path.mkdir()
    (target_path / "workflow.yaml").write_text("name: sample\n", encoding="utf-8")
    (target_path / "versions.yaml").write_text("project: sample\nversion: 0.1.0\n", encoding="utf-8")

    assert main(["--developer-path", str(developer_path), "list"]) == 0

    captured = capsys.readouterr()
    assert "sample-container" in captured.out


def test_cli_rejects_removed_audit_command(tmp_path: Path, capsys) -> None:
    """Reject the removed audit subcommand."""

    developer_path = _developer_path_create(tmp_path)

    with pytest.raises(SystemExit) as error:
        main(["--developer-path", str(developer_path), "audit", "sample-container"])

    assert error.value.code == 2

    captured = capsys.readouterr()
    assert "invalid choice: 'audit'" in captured.err


def test_main_is_importable() -> None:
    """Verify the CLI entrypoint can be imported."""

    assert callable(main)
