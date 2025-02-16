# Simple tutorial to show functionality of algorithm

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic.elastic import *
import sympy as sp
import numpy as np
import matplotlib as mpl

# Define variables
epsilon = np.linspace(0, 0.05, int(0.05/0.001) + 1)  # Strain vector from 0 to 0.075 in increments of 0.001
E= 100
Y0 = 2
H = 111.11

# Compute stress-strain behavior
[found_iso, found_kin] = stress_behavior(epsilon, E, H, Y0)