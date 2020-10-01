"""Console script for banana."""
import argparse
import sys

from . import bananalib as banana


def ananas2dec():
    parser = argparse.ArgumentParser(description="Convert ananas string to dec")
    parser.add_argument("ananas", help="String to be converted")
    args = parser.parse_args()

    print(banana.banana2dec(args.ananas, 1, 0))


def avocado2dec():
    parser = argparse.ArgumentParser(description="Convert avocado string to dec")
    parser.add_argument("avocado", help="String to be converted")
    args = parser.parse_args()

    print(banana.banana2dec(args.avocado, 1, 0))


def banana2dec():
    parser = argparse.ArgumentParser(description="Convert banana string to dec")
    parser.add_argument("banana", help="String to be converted")
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs="+")
    parser.add_argument(
        "--dictstart", help="Set starting dictionary", type=int, default=0
    )
    parser.add_argument(
        "--shiftend", help="Set shift for ending dictionary", type=int, default=0
    )
    args = parser.parse_args()

    print(banana.banana2dec(args.banana))


def ribes2dec():
    parser = argparse.ArgumentParser(description="Convert ribes string to dec")
    parser.add_argument("ribes", help="String to be converted")
    args = parser.parse_args()

    print(banana.banana2dec(args.ribes, 1, 0))


def bananarandom():
    parser = argparse.ArgumentParser(description="Generate random banana")
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs="+")
    parser.add_argument(
        "--dictstart", help="Set starting dictionary", type=int, default=0
    )
    parser.add_argument(
        "--shiftend", help="Set shift for ending dictionary", type=int, default=0
    )
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=6)
    args = parser.parse_args()

    print(
        banana.bananarandom(
            args.dictstart, args.shiftend, args.minlength, args.dictionary
        )
    )


def dec2ananas():
    parser = argparse.ArgumentParser(description="Convert dec number to ananas")
    parser.add_argument("num", help="Number to be converted", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    args = parser.parse_args()

    print(banana.dec2banana(args.num, 1, 0, args.minlength))


def dec2avocado():
    parser = argparse.ArgumentParser(description="Convert dec number to avocado")
    parser.add_argument("num", help="Number to be converted", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    args = parser.parse_args()

    print(banana.dec2banana(args.num, 1, 1, args.minlength))


def dec2banana():
    parser = argparse.ArgumentParser(description="Convert dec number to banana")
    parser.add_argument("num", help="Number to be converted", type=int)
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs="+")
    parser.add_argument(
        "--dictstart", help="Set starting dictionary", type=int, default=0
    )
    parser.add_argument(
        "--shiftend", help="Set shift for ending dictionary", type=int, default=0
    )
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    args = parser.parse_args()

    print(
        banana.dec2banana(
            args.num, args.dictstart, args.shiftend, args.minlength, args.dictionary
        )
    )


def dec2ribes():
    parser = argparse.ArgumentParser(description="Convert dec number to ribes")
    parser.add_argument("num", help="Number to be converted", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    args = parser.parse_args()

    print(banana.dec2banana(args.num, 1, 1, args.minlength))


def isbanana():
    parser = argparse.ArgumentParser(description="Checks if string is banana")
    parser.add_argument("banana", help="String to be checked")
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs="+")
    parser.add_argument(
        "--dictstart", help="Set starting dictionary", type=int, default=0
    )
    parser.add_argument(
        "--shiftend", help="Set shift for ending dictionary", type=int, default=0
    )
    args = parser.parse_args()

    print(banana.isbanana(args.banana, args.dictstart, args.shiftend, args.dictionary))


def main():
    sys.exit(bananarandom())


if __name__ == "__main__":
    # pragma: no cover
    main()
