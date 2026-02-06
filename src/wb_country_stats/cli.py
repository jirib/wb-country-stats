import argparse
import shutil
import signal
import sys
from .core import iter_countries, iter_indicators

# TODO: add country iso3366-1 alpha-2 code validation
# TODO: add indicators validation

def truncate_text(text: str, width: int) -> str:
    if width <= 3:
        return "." * width
    if len(text) <= width:
        return text
    return text[: width -3] + "..."


def list_countries(pattern: str | None) -> None:
    found = False
    for cou in iter_countries(pattern):
        found = True
        print(f"{cou['iso2Code']} | {cou['name']}")

    if not found:
        print("No country matched", file=sys.stderr)
        sys.exit(1)


def list_indicators(
        pattern: str | None,
        truncate: bool = True
) -> None:
    found = False
    id_width = 35
    cols = 88
    sep = " | "
    term_width = shutil.get_terminal_size((cols, 20)).columns
    name_width = max(
        cols - id_width - len(sep),
        term_width - id_width - len(sep)
    )

    for ind in iter_indicators(pattern):
        found = True

        name = ind.get("name", "")
        if truncate:
            name = truncate_text(name, name_width)
        
        print(
            f"{ind['id']:<{id_width}} | "
            f"{name:<{name_width}}"
        )

    if not found:
        print("No indicator matched", file=sys.stderr)
        sys.exit(1)


def main(argv=None):
    parser = argparse.ArgumentParser()
    # TODO: country
    # parser.add_argument("-c", "--country", help="ISO 3166-1 alpha-2 country code (can be defined multiple times).")
    parser.add_argument(
        "-C",
        "--list-countries",
        nargs="?",
        const="__ALL__",
        metavar="REGEX",
        help=(
            "List countries (optionally filtered, case insensively), by a regular expression)\n"
            "An example:\n"
            "  -C '(spain|columb|ecuad)'"
        )  
    )

    # TODO: indicator
    # parser.add_argument("-i", "--indicator", help="Indicator to limit query (comma separated).")
    parser.add_argument(
        "-I",
        "--list-indicators",
        nargs="?",
        const="__ALL__",
        metavar="REGEX",
        help=(
            "List indicators (optionally filtered, case-insensitevely, by a regular expression)\n"
            "An example:\n"
            "  -Q 'urban population,.*of total'"
        )
    )
    
    parser.add_argument(
        "--no-truncate",
        action="store_true",
        help=(
            "Do not truncate indicator descriptions"
        )
    )

    args = parser.parse_args(argv)

    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

    if args.list_countries is not None or args.list_indicators is not None:
        if args.list_countries:
            list_countries(
                None if args.list_countries == "__ALL__" else args.list_countries
            )
    
        if args.list_indicators:
            if args.list_countries:  # insert a blank line
                print()
            list_indicators(
                None if args.list_indicators == "__ALL__" else args.list_indicators,
                truncate = not args.no_truncate
            )

        sys.exit(0)