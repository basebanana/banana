#!/usr/bin/env python3

def dec2banana(num, dictstart = None, shiftend = None, minlength = None, dictionary = None):
    #defaults
    if dictstart is None: dictstart = 0
    if shiftend is None: shiftend = 0
    if minlength is None: minlength = 0
    if dictionary is None: dictionary = [list("bcdfglmnprstvz"), list("aeiou")]
    
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

    
def banana2dec(banana, dictstart = None, shiftend = None, dictionary = None):
    #defaults
    if dictstart is None: dictstart = 0
    if shiftend is None: shiftend = 0
    if dictionary is None: dictionary = [list("bcdfglmnprstvz"), list("aeiou")] #, list("123456")

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
