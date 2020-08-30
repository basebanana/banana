#!/usr/bin/env python3

def dec2banana(num, dictstart = 0, shiftend = 0, minlength = 0, dictionary = [list("bcdfglmnprstvz"), list("aeiou")]):
    numdict = len(dictionary)
    v = num
    st = ""
    l = 0

    i = (numdict - 1 + dictstart + shiftend) % numdict
    while not (v == 0 and i == (numdict - 1 + dictstart) % numdict and l >= minlength):
        r = v % len(dictionary[i])
        v = int(v / len(dictionary[i]))
        st = dictionary[i][r] + st
        i = (i - 1) % numdict
        l += 1
   
    return(st)

    
def banana2dec(banana, dictstart = 0, shiftend = 0, dictionary = [list("bcdfglmnprstvz"), list("aeiou")] ):
    numdict = len(dictionary)
    v = 0
    for i in range(len(banana)):
        r = (numdict + i + dictstart) % numdict
        try:
            v = v * len(dictionary[r]) + dictionary[r].index(banana[i])
        except:
            print("Carattere non valido in posizione", i+1)
            return()

    return(v)



if __name__ == "__main__":
    print("Ciao sono la libreria banana")
