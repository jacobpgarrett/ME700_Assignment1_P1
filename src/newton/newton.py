import numpy as np
from typing import Callable, Union

def newton(guess, f, df, tol=1e-9, max_iter=1000):
    # Function to find the root of a system of equations using Newton's method

    x = np.atleast_1d(np.array(guess, dtype=float)) # Initialize x as an array

    if np.all(f(*x) == 0): # If the initial guess is already a root
        return x
    
    for i in range(max_iter):
        J = np.atleast_2d(np.array(df(*x), dtype=float)) # Define the Jacobian
        if np.linalg.norm(J) == 0:
            raise ValueError('Jacobian is singular')
        
        F = np.atleast_1d(np.array(f(*x), dtype=float)) # Define the values of the function
        
        # # Print values for debugging
        # print(f"Iteration {i}:")
        # print("x:", x)
        # print("Jacobian J:", J)
        # print("Function F:", F)
        
        # Solve linear algebra equation
        delta_x = np.linalg.solve(J, -F)

        # print("Delta x:", delta_x) # for debugging

        x += delta_x.ravel() # Add the changes in x to the current x without changing the shape of x

        # print("Updated x:", x) # for debugging

        # Check for convergence
        if np.linalg.norm(F) < tol:
            return x
        
    # Error message if the function runs for too long
    raise RuntimeError('Newton method did not converge')