# Tutorial to highlight full functionality, showing the differences between the kinematic and isotropic hardening

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic.elastic import *
import sympy as sp
import numpy as np
import matplotlib as mpl

# Strain Map
epsilon_a = np.linspace(0, 0.05, int(0.05/0.001) + 1)  # Vector from 0 to 0.075 in increments of 0.001
epsilon_b = np.linspace(0.05, -0.05, 2*int(0.075/0.001) + 2)  # Vector from 0.075 to 0 in increments of 0.001
epsilon_c = np.linspace(-0.05, 0.075, int(.125/0.001)+1) # etc.
epsilon_d = np.linspace(0.075, -0.03, int(0.105/0.001)+1) # etc.
epsilon = np.concatenate((epsilon_a, epsilon_b, epsilon_c, epsilon_d))  # Combine the vectors

E= 100 # Young's Modulus
Y0 = 2 # Initial Yield Stress
H = 111.11 # Hardening Modulus

# Compute stress-strain behavior
[found_iso, found_kin] = stress_behavior(epsilon, E, H, Y0)