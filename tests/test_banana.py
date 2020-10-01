#!/usr/bin/env python

"""Tests for `banana` package."""
import pytest

from banana import (ananas2dec, avocado2dec, banana2dec, dec2ananas,
                    dec2avocado, dec2banana, dec2ribes, ribes2dec)

banana_conversions = {"be": 1, "beba": 70, "zu": 69, "bezu": 139, "nana": 2485}


@pytest.fixture(params=banana_conversions.items())
def banana_known(request):
    yield request.param


avocado_conversions = {
    "a": 0,
    "aca": 5,
    "ada": 10,
    "afa": 15,
    "aga": 20,
    "ala": 25,
    "ama": 30,
    "ana": 35,
    "apa": 40,
    "ara": 45,
    "asa": 50,
    "ata": 55,
    "ava": 60,
    "aza": 65,
    "eba": 70,
    "eca": 75,
    "eda": 80,
    "efa": 85,
    "ega": 90,
}


@pytest.fixture(params=avocado_conversions.items())
def avocado_known(request):
    yield request.param


ribes_conversions = {"b": 0, "c": 1, "z": 13, "beb": 14, "bec": 15}


@pytest.fixture(params=ribes_conversions.items())
def ribes_known(request):
    yield request.param


ananas_conversions = {
    "ac": 1,
    "al": 5,
    "as": 10,
    "ec": 15,
    "em": 20,
    "et": 25,
    "id": 30,
    "in": 35,
    "iv": 40,
    "of": 45,
    "op": 50,
    "oz": 55,
    "ug": 60,
    "ur": 65,
    "acab": 70,
    "acal": 75,
    "acas": 80,
    "acec": 85,
    "acem": 90,
}


@pytest.fixture(params=ananas_conversions.items())
def ananas_known(request):
    yield request.param


def test_banana_to_dec_known(banana_known):
    word, value = banana_known
    assert banana2dec(word) == value


def test_dec_to_banana_known(banana_known):
    word, value = banana_known
    assert dec2banana(value) == word


def test_banana2dec_prefix_ba(banana_known):
    """un ba all'inizio non cambia nulla!"""
    word, value = banana_known
    for prefix in ("ba", "baba", "bababa"):
        assert banana2dec(prefix + word) == value


def test_ribes_to_dec_known(ribes_known):
    word, value = ribes_known
    assert ribes2dec(word) == value


def test_dec_to_ribes_known(ribes_known):
    word, value = ribes_known
    assert dec2ribes(value) == word


def test_avocado_to_dec_known(avocado_known):
    word, value = avocado_known
    assert avocado2dec(word) == value


def test_dec_to_avocado_known(avocado_known):
    word, value = avocado_known
    assert dec2avocado(value) == word


def test_ananas_to_dec_known(ananas_known):
    word, value = ananas_known
    assert ananas2dec(word) == value


def test_dec_to_ananas_known(ananas_known):
    word, value = ananas_known
    assert dec2ananas(value) == word


def test_answer_to_life_the_universe_and_everything():
    banana = banana2dec("banana")
    assert banana != 42
    assert banana == 2485
