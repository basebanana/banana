#!/usr/bin/env python3
import argparse
import banana

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert ananas string to dec")
    parser.add_argument("ananas", help="String to be converted")
    args = parser.parse_args()

    print(banana.banana2dec(args.ananas, 1, 0))
