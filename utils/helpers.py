# utils/helpers.py

import numpy as np

def normalize(x):
    x = np.array(x)
    return (x - x.min()) / (x.max() - x.min() + 1e-9)