"""Tests for workflow-container-developer package metadata."""

import tomllib
from pathlib import Path

PYPROJECT_PATH = Path(__file__).resolve().parents[1] / "pyproject.toml"


def test_pytest_is_test_extra_not_runtime_dependency() -> None:
    """Keep pytest out of package runtime dependencies."""

    pyproject = tomllib.loads(PYPROJECT_PATH.read_text(encoding="utf-8"))

    assert "pytest>=8.4.0" not in pyproject["project"].get("dependencies", [])
    assert pyproject["project"]["optional-dependencies"]["test"] == ["pytest>=8.4.0"]
