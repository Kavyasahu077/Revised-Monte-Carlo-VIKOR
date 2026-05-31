# simulation/monte_carlo.py

import numpy as np
from bayesian.bn_model import bayesian_inference
from ahp.ahp_weights import ahp_weights
from vikor.vikor_engine import vikor
from config import COMPONENTS

def run_monte_carlo(df, n_sim=10000):

    rank_store = np.zeros((len(COMPONENTS), len(COMPONENTS)))
    q_store = []

    for _ in range(n_sim):

        # Step 1: Bayesian probabilities
        probs = bayesian_inference(df)

        # Step 2: AHP weights
        weights = ahp_weights()

        matrix = []

        for _, row in df.iterrows():

            # stochastic severity + detectability
            severity = row["Severity"] * np.random.uniform(0.9, 1.1)
            detect = (1 - row["Detectability"]) * np.random.uniform(0.9, 1.1)

            matrix.append([
                probs[row["Component"]],
                severity,
                detect
            ])

        matrix = np.array(matrix)

        # Step 3: VIKOR
        Q = vikor(matrix, weights)
        q_store.append(Q)

        ranking = np.argsort(Q)

        for pos, idx in enumerate(ranking):
            rank_store[idx, pos] += 1

    return np.array(q_store), rank_store