#!/usr/bin/env python

"""Tests for `banana` package."""

import pytest


from banana import bananalib


def test_answer_to_life_the_universe_and_everything():
    banana = bananalib.banana2dec("banana")
    assert banana != 42
    assert banana == 2485
