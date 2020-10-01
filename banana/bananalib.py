"""Main module."""


def encoder(num, dictstart=0, shiftend=0, minlength=0, dictionary=None):
    if dictionary is None:
        dictionary = [list("bcdfglmnprstvz"), list("aeiou")]

    numdict = len(dictionary)
    v = num
    st = ""
    length = 0

    idx = (numdict - 1 + dictstart + shiftend) % numdict
    while not (
        v == 0 and idx == (numdict - 1 + dictstart) % numdict and length >= minlength
    ):
        r = v % len(dictionary[idx])
        v = int(v / len(dictionary[idx]))
        st = dictionary[idx][r] + st
        idx = (idx - 1) % numdict
        length += 1

    return st


def decoder(banana, dictstart=0, shiftend=0, dictionary=None):
    # defaults
    if dictionary is None:
        dictionary = [list("bcdfglmnprstvz"), list("aeiou")]  # , list("123456")

    numdict = len(dictionary)
    if (len(banana) - shiftend) % numdict != 0:
        return "Banana non valida"
    v = 0
    for i in range(len(banana)):
        r = (numdict + i + dictstart) % numdict
        try:
            v = v * len(dictionary[r]) + dictionary[r].index(banana[i])
        except (ValueError, KeyError) as e:
            return "Carattere non valido in posizione", i + 1

    return v


def banana2dec(word):
    return decoder(word)


def dec2banana(word):
    return encoder(word)


def ribes2dec(word):
    return decoder(word, 1, 1)


def dec2ribes(word):
    return encoder(word, 1, 1)


def bananarandom(dictstart=0, shiftend=0, minlength=6, dictionary=None):
    import random

    # defaults
    if dictionary is None:
        dictionary = [list("bcdfglmnprstvz"), list("aeiou")]

    numdict = len(dictionary)
    st = ""
    length = 0

    i = (numdict - 1 + dictstart + shiftend) % numdict
    while not (i == (numdict - 1 + dictstart) % numdict and length >= minlength):
        r = random.randint(0, len(dictionary[i]) - 1)
        st = dictionary[i][r] + st
        i = (i - 1) % numdict
        length += 1

    return st


def isbanana(banana, dictstart=0, shiftend=0, dictionary=None):
    # defaults
    if dictionary is None:
        dictionary = [list("bcdfglmnprstvz"), list("aeiou")]  # , list("123456")

    numdict = len(dictionary)
    if (len(banana) - shiftend) % numdict != 0:
        return False
    for i in range(len(banana)):
        r = (numdict + i + dictstart) % numdict
        if banana[i] not in dictionary[r]:
            return False

    return True


if __name__ == "__main__":
    print("Ciao sono la libreria banana")
