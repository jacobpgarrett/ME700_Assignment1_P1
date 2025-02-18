# First Mechanics-Based tTutorial for plastic hardening

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic.elastic import *
import sympy as sp
import numpy as np
import matplotlib as mpl

# Define cyclic load
epsilon_a = np.linspace(0, 0.05, int(0.05/0.001) + 1)  # Initial Tension
epsilon_b = np.linspace(0.05, -0.05, 101) # Compression
epsilon_c = np.linspace(-0.05, -0.001, 50) # Tension reapplied to initial strain
epsilon_singular = np.concatenate((epsilon_a, epsilon_b, epsilon_c)) # Define full strain cycle
epsilon_cyclic = np.concatenate((epsilon_singular, epsilon_singular, epsilon_singular, epsilon_singular, epsilon_singular)) # 5 Cycles of strain
epsilon = epsilon_cyclic

# Define mechanics parameters
E= 100
Y0 = 2
H = 111.11

# Compute stress-strain behavior
[found_iso, found_kin] = stress_behavior(epsilon, E, H, Y0)