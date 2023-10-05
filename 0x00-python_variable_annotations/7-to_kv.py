#!/usr/bin/env python3
"""function to_kv"""
from typing import List, Tuple, Union, Any
import math


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes a string k and an int OR float v as arguments
    returns a tuple."""
    return (k, float(math.pow(v, 2)))
