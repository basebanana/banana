#!/usr/bin/env python3
import argparse
import banana

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert banana string to dec")
    parser.add_argument("banana", help="String to be converted")
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs='+')
    parser.add_argument("--dictstart", help="Set starting dictionary", type=int)
    parser.add_argument("--shiftend", help="Set shift for ending dictionary", type=int)
    args = parser.parse_args()

    print(banana.banana2dec(args.banana, args.dictstart, args.shiftend, args.dictionary))
