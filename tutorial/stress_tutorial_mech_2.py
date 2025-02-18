# Second Mechanics-Based tTutorial for plastic hardening

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic import *
import sympy as sp
import numpy as np
import matplotlib as mpl

# Define cyclic load
epsilon_a = np.linspace(0, 0.002, int(0.002/0.00001)+1)
epsilon_b = np.linspace(0.002, -0.002, int(0.004/0.00001)+1)
epsilon = np.concatenate((epsilon_a, epsilon_b))

# Define mechanics parameters
E= 200000000000
Y0 = 200000000
H = 25000000000

# Compute stress-strain behavior
[found_iso, found_kin] = stress_behavior(epsilon, E, H, Y0)