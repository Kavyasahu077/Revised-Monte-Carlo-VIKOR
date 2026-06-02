# vikor_engine.py

import numpy as np

def vikor(matrix, weights):

    # For risk assessment:
    # Higher values = higher risk
    best = matrix.max(axis=0)
    worst = matrix.min(axis=0)

    norm = (best - matrix) / (best - worst + 1e-9)

    S = np.sum(weights * norm, axis=1)
    R = np.max(weights * norm, axis=1)

    Q = (
        0.5 * (S - S.min()) / (S.max() - S.min() + 1e-9)
        + 0.5 * (R - R.min()) / (R.max() - R.min() + 1e-9)
    )

    return 1 - Q
