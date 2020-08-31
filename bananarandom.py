#!/usr/bin/env python3
import argparse
import banana

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate random banana")
    parser.add_argument("--dictstart", help="Set starting dictionary", type=int)
    parser.add_argument("--shiftend", help="Set shift for ending dictionary", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int)
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs='+')
    args = parser.parse_args()

    print(banana.bananarandom(args.dictstart, args.shiftend, args.minlength, args.dictionary))
