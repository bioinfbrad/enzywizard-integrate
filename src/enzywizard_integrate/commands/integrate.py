from __future__ import annotations
from argparse import Namespace, ArgumentParser
import sys
from ..services.integrate_service import run_integrate_service

def add_integrate_parser(parser: ArgumentParser) -> None:
    parser.add_argument("-i", "--input_dir",required=True,help="Path to a directory containing JSON reports to integrate.")
    parser.add_argument("-o", "--output_dir",required=True,help="Directory to save integrated JSON outputs.")
    parser.add_argument("--strict", dest="strict", action="store_true",help="Enable strict mode requiring all 12 report types and all node fields (default: Disabled).")
    parser.set_defaults(strict=False)
    parser.set_defaults(func=run_integrate)

def run_integrate(args: Namespace) -> None:
    success = run_integrate_service(input_dir=args.input_dir, output_dir=args.output_dir, strict=args.strict)
    if not success:
        sys.exit(1)
