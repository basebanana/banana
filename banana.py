import argparse

def dec2banana():
    parser = argparse.ArgumentParser(description="Create banana words")
    parser.add_argument("num", help="number to be converted", type=int)
    parser.add_argument("--dictionary", help="Set dictionary", type=list, nargs='+', default=[list("bcdfglmnprstvz"), list("aeiou")]) # , list("123456")
    parser.add_argument("--exactlength", help="Set exact length", type=int, default=0)
    parser.add_argument("--minlength", help="Set minimum length", type=int, default=0)
    parser.add_argument("--dictstart", help="Set starting dictionary", type=int, default=0)
    parser.add_argument("--shiftend", help="Set shift for ending dictionary", type=int, default=0)
    
    args = parser.parse_args()

    dictionary = args.dictionary
    numdict = len(dictionary)
    minlength = args.minlength
    
    v = args.num
    st = ""
    l = 0

    

    if args.exactlength == 0:
        i = (numdict - 1 + args.dictstart + args.shiftend) % numdict
        while not (v == 0 and i == (numdict - 1 + args.dictstart) % numdict and l >= args.minlength):
            r = v % len(dictionary[i])
            v = int(v / len(dictionary[i]))
            st = dictionary[i][r] + st
            i = (i - 1) % numdict
            l += 1
    else:
        i = (numdict - 1 + args.dictstart + args.shiftend + args.exactlength) % numdict
        while not (l >= args.exactlength):
            r = v % len(dictionary[i])
            v = int(v / len(dictionary[i]))
            st = dictionary[i][r] + st
            i = (i - 1) % numdict
            l += 1
        if v > 0:
            print("Error, result longer than exactlength")
            return
            
    print(st)


   





if __name__ == "__main__":
    dec2banana()