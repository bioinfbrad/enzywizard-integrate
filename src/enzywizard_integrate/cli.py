from __future__ import annotations

import argparse

from .commands.integrate import add_integrate_parser


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enzywizard-integrate",
        description="EnzyWizard-Integrate: Calculate protein/protein-substrate interactions and generate a detailed JSON report."
    )
    add_integrate_parser(parser)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)