import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.elastic.elastic import *
import sympy as sp
import numpy as np
import matplotlib as mpl

epsilon = np.array([0, 0.1])
print(isinstance(epsilon, np.ndarray))
known = [0, 1]
[found_iso, found_kin] = stress_behavior(epsilon, 10, 10, 10)
print(known == found_iso)
print(known == found_kin)