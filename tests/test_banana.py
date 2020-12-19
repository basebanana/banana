#!/usr/bin/env python

"""Tests for `banana` package."""
import random

import pytest

from banana import BananaCodec

banana_conversions = {
    "be": 1,
    "da": 10,
    "bema" : 100,
    "duga": 1000,
    "bibiva": 10000,
    "galopa": 100000,
    "bivucasa": 1000000,
    "beba": 70,
    "zu": 69,
    "bezu": 139,
    "nana": 2485,
}


@pytest.fixture(params=banana_conversions.items())
def banana_known(request):
    yield request.param


banana_codec = BananaCodec()




def test_banana_to_dec_known(banana_known):
    word, value = banana_known
    assert banana_codec.decode(word) == value


def test_dec_to_banana_known(banana_known):
    word, value = banana_known
    assert banana_codec.encode(value) == word


def test_banana_is_banana(banana_known):
    assert banana_codec.is_valid(banana_known[0])


def test_banana2dec_prefix_ba(banana_known):
    """un ba all'inizio non cambia nulla!"""
    word, value = banana_known
    for prefix in ("ba", "baba", "bababa"):
        assert banana_codec.decode(prefix + word) == value


def test_answer_to_life_the_universe_and_everything():
    banana = banana_codec.decode("banana")
    assert banana != 42
    assert banana == 2485


def test_random_len_0():
    assert banana_codec.random(minlength=0) == ""
    
