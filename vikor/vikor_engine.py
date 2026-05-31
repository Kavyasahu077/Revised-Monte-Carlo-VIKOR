# vikor/vikor_engine.py

import numpy as np

def vikor(matrix, weights):
    best = matrix.min(axis=0)
    worst = matrix.max(axis=0)

    norm = (matrix - best) / (worst - best + 1e-9)

    S = np.sum(weights * norm, axis=1)
    R = np.max(weights * norm, axis=1)

    Q = 0.5 * (S - S.min()) / (S.max() - S.min() + 1e-9) + \
        0.5 * (R - R.min()) / (R.max() - R.min() + 1e-9)

    return Q