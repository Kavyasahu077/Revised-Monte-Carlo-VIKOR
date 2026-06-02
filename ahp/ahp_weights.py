# ahp/ahp_weights.py

import numpy as np

def ahp_weights():
    return np.array([
        0.50,  # Failure Probability
        0.35,  # Severity
        0.15   # Non Detectability
    ])
