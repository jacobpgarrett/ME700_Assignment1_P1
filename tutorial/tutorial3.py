# Example of Newton's Method used in greater than 2D

# Import Libraries
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton.newton import newton
import sympy as sp
import numpy as np

# Initial Guess, functions defined
guess = [1, 1, 1, 1, 1]
x, y, z, w, v = sp.symbols('x y z w v')
f1 = x + y + z + w + v - 15
f2 = 2*x -y + 3*z - 2*w + v - 7
f3 = x + 2*y - z + w - 3*v + 4
f4 = 3*x - 4*y +2*z + 5*w - v - 12
f5 = x - y - z + w + v - 1

f = sp.Matrix([f1, f2, f3, f4, f5]) # Function vector

df = f.jacobian([x, y, z, w, v]) # Define Jacobian matrix

# Return functions to numerical form
f = sp.lambdify((x, y, z, w, v), f, 'numpy')
df = sp.lambdify((x, y, z, w, v), df, 'numpy')

# Print out roots of system of equations
print('The roots of this function [u, v] are:')
print(newton(guess, f, df))