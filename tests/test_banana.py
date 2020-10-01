#!/usr/bin/env python

"""Tests for `banana` package."""

from banana import banana2dec, dec2banana, dec2ribes, ribes2dec

banana_conversions = {
    "ba": 0,
    "baba": 0,
    "be": 1,
    "beba": 70,
    "zu": 69,
    "bezu": 139,
    "nana": 2485,
    "banana": 2485,
}

ribes_conversions = {
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


def test_banana_to_dec_known():
    for word, value in banana_conversions.items():
        assert banana2dec(word) == value


def test_banana2dec_prefix_ba():
    """un ba all'inizio non cambia nulla!"""
    for word in banana_conversions:
        value = banana2dec(word)
        for prefix in ("ba", "baba", "bababa"):
            assert banana2dec(prefix + word) == value


def test_dec_to_banana_known():
    for word, value in banana_conversions.items():
        if word.startswith("ba"):
            continue
        assert dec2banana(value) == word


def test_ribes_to_dec_known():
    for word, value in ribes_conversions.items():
        assert ribes2dec(word) == value


def test_dec_to_ribes_known():
    for word, value in ribes_conversions.items():
        assert dec2ribes(value) == word


def test_answer_to_life_the_universe_and_everything():
    banana = banana2dec("banana")
    assert banana != 42
    assert banana == 2485
