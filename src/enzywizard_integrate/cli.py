from __future__ import annotations

import argparse

from .commands.integrate import add_integrate_parser


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="enzywizard-integrate",
        description="EnzyWizard-Integrate: Integrate multiple EnzyWizard JSON reports and constructing a protein / protein-substrate graph representation."
    )
    add_integrate_parser(parser)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)