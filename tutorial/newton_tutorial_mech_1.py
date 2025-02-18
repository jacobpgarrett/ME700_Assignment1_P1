import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton import newton
import sympy as sp
import numpy as np

# Initial Guess, functions defined
guess = [1, 1]
u, v = sp.symbols('u v')
f1 = -((10+u)/sp.sqrt(v**2+(10+u)**2))*100*(sp.sqrt(v**2+(10+u)**2)-10)+((10-u)/sp.sqrt(v**2+(10-u)**2))*200*(sp.sqrt(v**2+(10-u)**2)-10)
f2 = (v/sp.sqrt(v**2+(10+u)**2))*100*(sp.sqrt(v**2+(10+u)**2)-10)+(v/sp.sqrt(v**2+(10-u)**2))*200*(sp.sqrt(v**2+(10-u)**2)-10)-0.1

f = sp.Matrix([f1, f2]) # Function vector

df = f.jacobian([u, v]) # Define Jacobian matrix

# Return functions to numerical form
f = sp.lambdify((u, v), f, 'numpy')
df = sp.lambdify((u, v), df, 'numpy')

# Print out roots of system of equations
print('The roots of this function [u, v] are:')
print(newton(guess, f, df))