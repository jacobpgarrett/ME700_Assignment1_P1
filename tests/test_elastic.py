import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic.elastic import *
import sympy as sp
import numpy as np
import pytest

def test_zeros():
    epsilon = [0, 0.1]
    known = [0, 1]
    [found_iso, found_kin] = stress_behavior(epsilon, 10, 10, 10)
    assert known == found_iso
    assert known == found_kin
