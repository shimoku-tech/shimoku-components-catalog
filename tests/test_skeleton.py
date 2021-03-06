# -*- coding: utf-8 -*-

import pytest
from shimoku_components_catalog.skeleton import fib

__author__ = "capitan-ariete"
__copyright__ = "capitan-ariete"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
