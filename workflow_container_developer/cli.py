"""Command line interface for workflow-container developer tooling."""

import argparse


def main() -> int:
    """Run the workflow-container developer CLI.

    Returns:
        Process exit code.
    """

    parser = argparse.ArgumentParser(prog="workflow-container-dev")
    parser.add_argument("--version", action="version", version="workflow-container-dev 0.1.0")
    parser.parse_args()
    return 0
