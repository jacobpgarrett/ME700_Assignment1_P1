import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.newton.newton import newton
import sympy as sp

# Initial Guess, function and derivative defined
guess = 1.5
x = sp.symbols('x')
f = lambda x: 2*1*(sp.sqrt(1+x**2)-1)*(x/sp.sqrt(1+x**2))-0.25

# Convert to numerical form
df = sp.lambdify(x, sp.diff(f(x), x))
f = sp.lambdify(x, f(x))

# Print out root of function
print('The root of this function is:')
print(newton(guess, f, df))