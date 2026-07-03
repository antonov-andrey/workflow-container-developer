"""Tests for the workflow-container-developer CLI."""

from workflow_container_developer.cli import main


def test_main_is_importable() -> None:
    """Verify the CLI entrypoint can be imported."""

    assert callable(main)
