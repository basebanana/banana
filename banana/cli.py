"""Console script for banana."""
import argparse
import sys

import banana


def get_codec(args):
    if args.banana:
        return banana.BananaCodec()
    if args.ananas:
        return banana.AnanasCodec()
    kwargs = {}
    if args.dictionary:
        kwargs["dictionary"] = args.dictionary
    if args.dictstart:
        kwargs["dictstart"] = args.dictstart
    if args.shiftend:
        kwargs["shiftend"] = args.shiftend
    return banana.Codec(**kwargs)


def main_encode(args):
    print(get_codec(args).encode(args.num))


def main_decode(args):
    print(get_codec(args).decode(args.word))


def main_check(args):
    if get_codec(args).is_valid(args.word):
        if not args.quiet:
            print("yes")
        sys.exit(0)
    else:
        if not args.quiet:
            print("no")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Convert dec number to banana")
    parser.add_argument("--ananas", action="store_true")
    parser.add_argument("--avocado", action="store_true")
    parser.add_argument("--banana", action="store_true")
    parser.add_argument("--ribes", action="store_true")
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs="+")
    parser.add_argument(
        "--dictstart", help="Set starting dictionary", type=int, default=0
    )
    parser.add_argument(
        "--shiftend", help="Set shift for ending dictionary", type=int, default=0
    )
    sub = parser.add_subparsers()
    encode = sub.add_parser("encode", help="Convert numbers to words")
    encode.add_argument("num", type=int)
    encode.set_defaults(func=main_encode)

    decode = sub.add_parser("decode", help="Convert words to numbers")
    decode.add_argument("word")
    decode.set_defaults(func=main_decode)

    check = sub.add_parser("check", help="Convert words to numbers")
    check.add_argument("word")
    check.add_argument("--quiet", "-q", action="store_true")
    check.set_defaults(func=main_check)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        print("You need to select one subcommand. \nUse --help", file=sys.stderr)
        # parser.print_help()
        sys.exit(1)
    args.func(args)


def ananas2dec():
    parser = argparse.ArgumentParser(description="Convert ananas string to dec")
    parser.add_argument("ananas", help="String to be converted")
    args = parser.parse_args()

    print(banana.ananas2dec(args.ananas))


def avocado2dec():
    parser = argparse.ArgumentParser(description="Convert avocado string to dec")
    parser.add_argument("avocado", help="String to be converted")
    args = parser.parse_args()

    print(banana.avocado2dec(args.avocado))


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

    print(banana.ribes2dec(args.ribes))


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

    print(banana.dec2ananas(args.num))


def dec2avocado():
    parser = argparse.ArgumentParser(description="Convert dec number to avocado")
    parser.add_argument("num", help="Number to be converted", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    args = parser.parse_args()

    print(banana.dec2avocado(args.num, minlength=args.minlength))


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

    print(banana.dec2banana(args.num))


def dec2ribes():
    parser = argparse.ArgumentParser(description="Convert dec number to ribes")
    parser.add_argument("num", help="Number to be converted", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    args = parser.parse_args()

    print(banana.dec2ribes(args.num))


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

    print(banana.isbanana(args.banana))


if __name__ == "__main__":
    # pragma: no cover
    main()
