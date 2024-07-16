"""
Command-Line Interface
======================

Produces .html and .json when given .docx documents
"""

import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from jugmt.document import Document


def parse_args() -> Namespace:
    """Return command-line arguments"""

    parser = ArgumentParser(
        description="Extract table information from .docx documents"
    )
    parser.add_argument(
        "document", nargs="+", type=Path, help="Path to one or more .docx document(s)"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Directory where the output will be saved",
        default=Path("output"),
    )
    parser.add_argument(
        "--validate",
        type=int,
        default=1,
        choices=[0, 1, 2],
        help="0: skip validation; 1; true/false; 2: trace of errors",
    )

    return parser.parse_args()


def main() -> int:
    """CLI entrypoint"""

    args = parse_args()
    args.output.mkdir(parents=True, exist_ok=True)

    for path in args.document:
        document = Document(path)
        document.extract_figures()

        (args.output / document.path.stem).with_suffix(".html").write_text(
            document.to_html()
        )
        json_str = document.to_json()
        (args.output / document.path.stem).with_suffix(".json").write_text(json_str)

        if args.validate == 0:
            continue

        document.validate(args.validate)

    return 0


if __name__ == "__main__":
    sys.exit(main())
