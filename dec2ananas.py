#!/usr/bin/env python3
import argparse
import banana

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert dec number to banana")
    parser.add_argument("num", help="number to be converted", type=int)
    parser.add_argument("--minlength", help="Set minimum length", type=int)
    args = parser.parse_args()

    print(banana.dec2banana(args.num, 1, 0, args.minlength))
