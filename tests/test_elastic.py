import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic.elastic import *
import sympy as sp
import numpy as np
import pytest

def test_array():
    epsilon = 0
    with pytest.raises(ValueError):
        stress_behavior(epsilon, 10, 10, 10)

def test_simple():
    epsilon = np.array([0, 0.1])
    known = np.array([0, 1])
    [found_iso, found_kin] = stress_behavior(epsilon, 10, 10, 10)
    assert np.all(known) == np.all(found_iso)
    assert np.all(known) == np.all(found_kin)
