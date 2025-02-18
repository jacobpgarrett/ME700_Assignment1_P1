# Simple use of Newton's Method in 2D

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton import newton
import sympy as sp
import numpy as np

# Initial Guess, functions defined
guess = [1, 1]
u, v = sp.symbols('u v')
f1 = u+v
f2 = u-v

f = sp.Matrix([f1, f2]) # Function vector

df = f.jacobian([u, v]) # Define Jacobian matrix

# Return functions to numerical form
f = sp.lambdify((u, v), f, 'numpy')
df = sp.lambdify((u, v), df, 'numpy')

# Print out roots of system of equations
print('The roots of this function [u, v] are:')
print(newton(guess, f, df))