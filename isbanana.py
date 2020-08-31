#!/usr/bin/env python3
import argparse
import banana

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Checks if string is banana")
    parser.add_argument("banana", help="String to be checked")
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs='+')
    parser.add_argument("--dictstart", help="Set starting dictionary", type=int)
    parser.add_argument("--shiftend", help="Set shift for ending dictionary", type=int)
    args = parser.parse_args()

    print(banana.isbanana(args.banana, args.dictstart, args.shiftend, args.dictionary))
