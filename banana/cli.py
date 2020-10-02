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


if __name__ == "__main__":
    # pragma: no cover
    main()
