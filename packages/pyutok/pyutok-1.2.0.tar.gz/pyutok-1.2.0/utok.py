"""Python interpretation of utok."""

from __future__ import annotations

import argparse
from importlib import metadata
import itertools
import sys

__date__ = "2024/07/13 17:09:03 hoel"
__author__ = "Berthold Höllmann"
__copyright__ = "Copyright © 2020 by Berthold Höllmann"
__credits__ = ["Berthold Höllmann"]
__maintainer__ = "Berthold Höllmann"
__email__ = "berhoel@gmail.com"


def get_parser() -> argparse.ArgumentParser:
    """Define the command line parser for ``utok``.

    Returns
    -------
      ArgumentParser: Command line argument parser for ``utok``.
    """
    parser = argparse.ArgumentParser(
        prog="utok",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--delimiter",
        "-s",
        type=str,
        default=":",
        help="""
Allows one to change the delimiter. If you use csh you might want to set your
path with something like: set path = (`utok -s \\  /usr/local/bin $path`) """,
    )
    parser.add_argument(
        "--delete-list",
        "-d",
        type=str,
        help="""\
Allows one to remove tokens from a list, to remove /usr/sbin and . from a path \
in Bourne Shell one might use: PATH=`utok $PATH -d .:/usr/sbin`
""",
    )
    parser.add_argument("tokens", nargs="+", type=str)
    parser.add_argument(
        "--version",
        "-V",
        action="version",
        version=f"%(prog)s {metadata.version('pyutok')}",
    )
    return parser


def utok(tokens: list[str], delimiter: str = ":", delete_list: str = "") -> str:
    """Process token.

    The token chains are splitted at `delimiter` into tokens, and then
    the tokens joined again using `delimiter` after removing double
    tokens.

    Args
    ----
        tokens (list[str]): List of strings representing tokens chains.
        delimiter (str): Character used to construct token chains.
        delete_list (str): Chain of tokens to be deleted from `tokens`.

    Returns
    -------
    str: Token chain with all tokens.
    """
    res = []
    _delete_list = delete_list.split(delimiter) if delete_list else []
    for t in itertools.chain(*(j.split(delimiter) for j in tokens)):
        if t not in res and t not in _delete_list:
            res.append(t)
    return delimiter.join(res)


def prog() -> str:
    """Process command line options and execute joining.

    ``utok [-s delimiter] [ tokens...  [-d delete-list ] tokens...]``

    Returns
    -------
    str: Newly constructed string.
    """
    args = get_parser().parse_args()

    return utok(args.tokens, delimiter=args.delimiter, delete_list=args.delete_list)


def main() -> None:
    """Print the result string."""
    sys.stdout.write(f"{prog()}\n")


if __name__ == "__main__":
    main()
