"""Console script for banana."""
import argparse
import logging
import random
import sys

import banana


def get_codec(args):
    kwargs = {}
    if args.alphabets:
        kwargs["alphabets"] = args.alphabets
    if args.shiftalpha:
        kwargs["shiftalpha"] = args.shiftalpha
    if args.alphaend:
        kwargs["alphaend"] = args.alphaend
    return banana.Codec(**kwargs)


def main_encode(args):
    codec = get_codec(args)
    kwargs = dict(num=args.num)
    if args.minlength:
        kwargs["minlength"] = args.minlength
    print(codec.encode(**kwargs))


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


def main_random(args):
    codec = get_codec(args)
    kwargs = dict(minlength=args.minlength)
    if args.seed:
        kwargs["prng"] = random.Random(args.seed)
    print(codec.random(**kwargs))


def colon_separated_list(s):
    return s.split(":")


def main():
    parser = argparse.ArgumentParser(description="Convert number to banana")
    parser.add_argument(
        "--log-level", choices=["DEBUG", "INFO", "WARN", "ERROR"], default="WARN"
    )
    parser.add_argument(
        "--alphabets", "-a",
        help="Set alphabets in colon-separated list",
        type=colon_separated_list,
    )
    parser.add_argument(
        "--shiftalpha", "-s", help="Set shift for alphabets", type=int, default=0
    )
    parser.add_argument(
        "--alphaend", "-e", help="Set ending alphabet", type=int, default=0
    )
    sub = parser.add_subparsers()
    encode = sub.add_parser("encode", help="Convert number to word")
    encode.add_argument("num", type=int)
    encode.add_argument("--minlength", "-l", help="Set minimum length", type=int, default=6)
    encode.set_defaults(func=main_encode)

    decode = sub.add_parser("decode", help="Convert word to number")
    decode.add_argument("word")
    decode.set_defaults(func=main_decode)

    check = sub.add_parser("check", help="Check if word is banana")
    check.add_argument("word")
    check.add_argument("--quiet", "-q", action="store_true")
    check.set_defaults(func=main_check)

    rand = sub.add_parser("random", help="Generate random banana")
    rand.add_argument("--minlength", "-l", help="Set minimum length", type=int, default=6)
    rand.add_argument("--seed", type=int, default=None)
    rand.set_defaults(func=main_random)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        print("You need to select one subcommand. \nUse --help", file=sys.stderr)
        # parser.print_help()
        sys.exit(1)
    logging.basicConfig(level=args.log_level)
    args.func(args)


if __name__ == "__main__":
    # pragma: no cover
    main()
