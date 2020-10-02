"""Main module."""


class Codec:
    def __init__(self, dictstart=0, shiftend=0, minlength=0, dictionary=None):
        self.dictstart = dictstart
        self.shiftend = shiftend
        if dictionary is None:
            self.dictionary = [list("bcdfglmnprstvz"), list("aeiou")]
        else:
            self.dictionary = dictionary

    def encode(self, num, minlength=0):
        dictionary = self.dictionary
        numdict = len(dictionary)
        v = num
        st = ""
        length = 0

        idx = (numdict - 1 + self.dictstart + self.shiftend) % numdict
        while not (
            v == 0
            and idx == (numdict - 1 + self.dictstart) % numdict
            and length >= minlength
        ):
            r = v % len(dictionary[idx])
            v = int(v / len(dictionary[idx]))
            st = dictionary[idx][r] + st
            idx = (idx - 1) % numdict
            length += 1

        return st

    def decode(self, word):
        dictionary = self.dictionary

        numdict = len(dictionary)
        if (len(word) - self.shiftend) % numdict != 0:
            raise ValueError("Banana non valida")
        v = 0
        for i in range(len(word)):
            r = (numdict + i + self.dictstart) % numdict
            try:
                v = v * len(dictionary[r]) + dictionary[r].index(word[i])
            except (ValueError, KeyError):
                raise ValueError("Carattere non valido in posizione %d" % i + 1)

        return v

    def is_valid(self, word):
        dictionary = self.dictionary

        numdict = len(dictionary)
        if (len(word) - self.shiftend) % numdict != 0:
            return False
        for i in range(len(word)):
            r = (numdict + i + self.dictstart) % numdict
            if word[i] not in dictionary[r]:
                return False

        return True


class BananaCodec(Codec):
    def __init__(self):
        super().__init__()


class RibesCodec(Codec):
    def __init__(self):
        super().__init__(0, 1)


class AnanasCodec(Codec):
    def __init__(self):
        super().__init__(1, 0)


class AvocadoCodec(Codec):
    def __init__(self):
        super().__init__(1, 1)


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


if __name__ == "__main__":
    print("Ciao sono la libreria banana")
