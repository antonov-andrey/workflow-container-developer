"""Tests for workflow-container-developer package metadata."""

import json
import tomllib
from pathlib import Path

import workflow_container_developer

PLUGIN_MANIFEST_PATH = (
    Path(__file__).resolve().parents[1] / "plugins" / "workflow-container-tools" / ".codex-plugin" / "plugin.json"
)
PYPROJECT_PATH = Path(__file__).resolve().parents[1] / "pyproject.toml"
README_PATH = Path(__file__).resolve().parents[1] / "README.md"


def test_pytest_is_test_extra_not_runtime_dependency() -> None:
    """Keep pytest out of package runtime dependencies."""

    pyproject = tomllib.loads(PYPROJECT_PATH.read_text(encoding="utf-8"))

    assert "pytest>=8.4.0" not in pyproject["project"].get("dependencies", [])
    assert pyproject["project"]["optional-dependencies"]["test"] == ["pytest>=8.4.0"]


def test_package_description_matches_public_scope() -> None:
    """Keep Python package metadata aligned with the README scope."""

    pyproject = tomllib.loads(PYPROJECT_PATH.read_text(encoding="utf-8"))

    assert (
        pyproject["project"]["description"]
        == "Codex plugin marketplace source for workflow-container authoring and audit skills with optional local discovery CLI"
    )


def test_readme_development_bootstrap_creates_uv_venv() -> None:
    """Make development commands reproducible from a clean checkout."""

    readme_text = README_PATH.read_text(encoding="utf-8")

    assert "uv venv --python 3.14" in readme_text
    assert "source .venv/bin/activate" in readme_text
    assert readme_text.index("uv venv --python 3.14") < readme_text.index("source .venv/bin/activate")
    assert readme_text.index("source .venv/bin/activate") < readme_text.index('uv pip install -e ".[test]"')


def test_readme_and_package_docstring_match_plugin_scope() -> None:
    """Keep project prose limited to authoring, audit and optional discovery."""

    readme_text = README_PATH.read_text(encoding="utf-8")

    assert (
        "`workflow-container-developer` is a Codex plugin marketplace source for workflow-container authoring and audit skills."
        in readme_text
    )
    assert "workflow-container development tools" not in readme_text
    assert (
        workflow_container_developer.__doc__
        == "Optional local discovery helpers for adjacent workflow-container projects."
    )


def test_plugin_manifest_description_matches_authoring_audit_scope() -> None:
    """Keep plugin manifest prose aligned with authoring and audit ownership."""

    plugin_manifest = json.loads(PLUGIN_MANIFEST_PATH.read_text(encoding="utf-8"))

    assert plugin_manifest["description"] == "Codex skills for authoring and auditing workflow-container projects."
    assert plugin_manifest["interface"]["shortDescription"] == "Author and audit workflow-container projects."
    assert "developing workflow-container projects" not in plugin_manifest["description"]
    assert "Develop and audit workflow-container projects" not in plugin_manifest["interface"]["shortDescription"]
