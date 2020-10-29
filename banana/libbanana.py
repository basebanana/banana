"""Main module."""
import logging
import random

log = logging.getLogger("libbanana")


class Codec:
    def __init__(self, shiftalpha=0, alphaend=0, minlength=0, alphabets=None):
        self.shiftalpha = shiftalpha
        self.alphaend = alphaend
        if alphabets is None:
            self.alphabets = [list("bcdfglmnprstvz"), list("aeiou")]
        else:
            self.alphabets = alphabets

    def encode(self, num, minlength=1):
        alphabets = self.alphabets
        numalpha = len(alphabets)
        v = num
        st = ""
        length = 0

        idx = (numalpha - 1 + self.shiftalpha + self.alphaend) % numalpha
        while not (
            v == 0
            and idx == (numalpha - 1 + self.shiftalpha) % numalpha
            and length >= minlength
        ):
            r = v % len(alphabets[idx])
            v = int(v / len(alphabets[idx]))
            st = alphabets[idx][r] + st
            idx = (idx - 1) % numalpha
            length += 1

        return st

    def decode(self, word):
        alphabets = self.alphabets

        numalpha = len(alphabets)
        if (len(word) - self.alphaend) % numalpha != 0:
            raise ValueError("Invalid banana")
        v = 0
        for i in range(len(word)):
            r = (numalpha + i + self.shiftalpha) % numalpha
            try:
                v = v * len(alphabets[r]) + alphabets[r].index(word[i])
            except (ValueError, KeyError):
                raise ValueError("Invalid character in position %d" % i + 1)

        return v

    def is_valid(self, word):
        alphabets = self.alphabets

        numalpha = len(alphabets)
        if (len(word) - self.alphaend) % numalpha != 0:
            return False
        for i in range(len(word)):
            r = (numalpha + i + self.shiftalpha) % numalpha
            if word[i] not in alphabets[r]:
                return False

        return True

    def random(self, minlength=6, prng=random.Random()):
        numalpha = len(self.alphabets)
        word = ""

        if minlength < 1:
            return ""

        curr_alpha = (numalpha - 1 + self.shiftalpha + self.alphaend) % numalpha
        final_alpha = (numalpha - 1 + self.shiftalpha) % numalpha
        while curr_alpha != final_alpha or len(word) < minlength:
            word = prng.choice(self.alphabets[curr_alpha]) + word
            curr_alpha = (curr_alpha - 1) % numalpha

        return word


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


if __name__ == "__main__":
    print("Hi I'm the basebanana library")
