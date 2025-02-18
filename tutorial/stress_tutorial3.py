# Tutorial to expand upon differences between isotropic and kinematic hardening

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic import *
import sympy as sp
import numpy as np
import matplotlib as mpl

# Strain Map
epsilon_a = np.linspace(0, 1, 1001)  # Vector from 0 to 0.075 in increments of 0.001
epsilon_b = np.linspace(1, -1, 2001)  # Vector from 0.075 to 0 in increments of 0.001
epsilon_c = np.linspace(-1, 4, 4001) # etc.
epsilon_d = np.linspace(4, -3, 7001) # etc.
epsilon = np.concatenate((epsilon_a, epsilon_b, epsilon_c, epsilon_d))  # Combine the vectors

E= 5 # Young's Modulus
Y0 = 2 # Initial Yield Stress
H = 10/3 # Hardening Modulus

# Compute stress-strain behavior
[found_iso, found_kin] = stress_behavior(epsilon, E, H, Y0)