import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic import *
import sympy as sp
import numpy as np
import pytest

# Test that the function checks that the input is an array
def test_array():
    epsilon = 0
    with pytest.raises(ValueError):
        stress_behavior(epsilon, 10, 10, 10)

# Checks to ensure that the function works
def test_simple():
    epsilon = np.array([0, 0.1])
    known = np.array([0, 1])
    [found_iso, found_kin] = stress_behavior(epsilon, 10, 10, 10)
    assert np.all(known) == np.all(found_iso)
    assert np.all(known) == np.all(found_kin)

# Tests that the function can accurately predict deformation using a sample deformation
def test_plastic():
    epsilon = np.linspace(0, 0.05, int(0.05/0.001) + 1)
    known = [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1., 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.,
            2.05263133, 2.10526266, 2.15789399, 2.21052532, 2.26315665, 2.31578798, 2.36841931, 2.42105064, 2.47368197,
            2.5263133,  2.57894463, 2.63157596, 2.68420729, 2.73683861, 2.78946994, 2.84210127, 2.8947326,  2.94736393,
            2.99999526, 3.05262659, 3.10525792, 3.15788925, 3.21052058, 3.26315191, 3.31578324, 3.36841457, 3.4210459,
            3.47367723, 3.52630856, 3.57893989]
    [found_iso, found_kin] = stress_behavior(epsilon, 100, 2, 111.11)
    assert np.all(known) == np.all(found_iso)
    assert np.all(known) == np.all(found_kin)

# Tests that the function can ensure that the initial strain is 0
def test_initial_state():
    epsilon = np.linspace(1, 2, 100)
    with pytest.raises(ValueError):
        stress_behavior(epsilon, 5, 5, 5)