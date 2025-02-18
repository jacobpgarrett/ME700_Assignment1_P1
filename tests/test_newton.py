import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton import newton
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

# Test to test that function works in 2D
def test_2D():
    guess = [1, 1]
    u, v = sp.symbols('u v')
    f1 = -((10+u)/sp.sqrt(v**2+(10+u)**2))*100*(sp.sqrt(v**2+(10+u)**2)-10)+((10-u)/sp.sqrt(v**2+(10-u)**2))*200*(sp.sqrt(v**2+(10-u)**2)-10)
    f2 = (v/sp.sqrt(v**2+(10+u)**2))*100*(sp.sqrt(v**2+(10+u)**2)-10)+(v/sp.sqrt(v**2+(10-u)**2))*200*(sp.sqrt(v**2+(10-u)**2)-10)-0.1

    f = sp.Matrix([f1, f2]) # Function vector

    df = f.jacobian([u, v]) # Define Jacobian matrix

    f = sp.lambdify((u, v), f, 'numpy')
    df = sp.lambdify((u, v), df, 'numpy')

    found = newton(guess, f, df)
    known = [0.00296803, 0.42190384]
    assert np.allclose(found, known)

# Test runtime error
def test_runtime_error():
    guess = 100
    x = sp.symbols('x')
    f = lambda x: x
    df = sp.lambdify(x, sp.diff(f(x), x))
    f = sp.lambdify(x, f(x))
    with pytest.raises(RuntimeError):
        newton(guess, f, df, 1e-9, 1)

# Return given value when guess is root
def test_return():
    guess = 0
    x = sp.symbols('x')
    f = lambda x: x
    df = sp.lambdify(x, sp.diff(f(x), x))
    f = sp.lambdify(x, f(x))
    found = newton(guess, f, df)
    assert np.isclose(found, guess)