import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton import newton
from src.elastic import *
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