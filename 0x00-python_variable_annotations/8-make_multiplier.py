#!/usr/bin/env python3
"""function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a string k and an int OR float v as arguments
    returns a tuple."""
    def mul(x: float) -> float:
        return x * multiplier
    return mul
