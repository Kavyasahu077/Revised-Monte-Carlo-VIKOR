# bayesian/bn_model.py

import numpy as np

def bayesian_inference(df):
    """
    Vibration-aware probabilistic Bayesian approximation
    """

    probs = {}

    for _, row in df.iterrows():
        base = row["Failure_Prob"]
        vib = row["Vibration"]

        # Causal influence strength
        if row["Component"] == "Turbine":
            p = base + 0.70 * vib

        elif row["Component"] == "Pump":
            p = base + 0.65 * vib

        elif row["Component"] == "Valve":
            p = base + 0.2 * vib

        elif row["Component"] == "Sensor":
            p = base + 0.01 * vib

        probs[row["Component"]] = min(p, 0.99)

    return probs
