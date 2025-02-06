import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton.newton import newton
import sympy as sp
import numpy as np
import pytest

# Simple test to test that function works in 1D
def test_simple():
    guess = 1
    x = sp.symbols('x')
    f = lambda x: x
    df = sp.lambdify(x, sp.diff(f(x), x))
    f = sp.lambdify(x, f(x))
    found = newton(guess, f, df)
    known = 0
    assert np.isclose(found, known)

