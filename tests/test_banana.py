#!/usr/bin/env python

"""Tests for `banana` package."""

from banana import banana2dec, dec2banana

known_conversions = {
    "ba": 0,
    "baba": 0,
    "be": 1,
    "beba": 70,
    "zu": 69,
    "bezu": 139,
    "nana": 2485,
    "banana": 2485,
}


def test_banana_to_dec_known():
    for word, value in known_conversions.items():
        assert banana2dec(word) == value


def test_banana2dec_prefix_ba():
    """un ba all'inizio non cambia nulla!"""
    for word in known_conversions:
        value = banana2dec(word)
        for prefix in ("ba", "baba", "bababa"):
            assert banana2dec(prefix + word) == value


def test_dec_to_banana_known():
    for word, value in known_conversions.items():
        if word.startswith("ba"):
            continue
        assert dec2banana(value) == word


def test_answer_to_life_the_universe_and_everything():
    banana = banana2dec("banana")
    assert banana != 42
    assert banana == 2485
