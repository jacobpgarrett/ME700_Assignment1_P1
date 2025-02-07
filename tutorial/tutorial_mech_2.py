import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton.newton import newton
import sympy as sp
import numpy as np

# Initial Guess, function and derivative defined
guess = 78
x = sp.symbols('x')
f = lambda x: 11.5*(3000000-2430000+(64-x**2)/2)-6520000

# Convert to numerical form
df = sp.lambdify(x, sp.diff(f(x), x))
f = sp.lambdify(x, f(x))

# Print out root of function
print('The root of this function is:')
print(newton(guess, f, df))