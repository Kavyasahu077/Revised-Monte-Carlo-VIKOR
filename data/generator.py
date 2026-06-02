# data/generator.py

import numpy as np
import pandas as pd
from config import COMPONENTS

def generate_data():

    data = [

        [
            "Pump",
            np.random.uniform(0.15, 0.30), # Failure_Prob
            np.random.uniform(0.80, 0.95), # Severity
            np.random.uniform(0.50, 0.70), # Detectability
            np.random.uniform(0.70, 1.00)  # Vibration
        ],

        [
            "Turbine",
            np.random.uniform(0.20, 0.35), # Failure_Prob
            np.random.uniform(0.90, 1.00), # Severity
            np.random.uniform(0.40, 0.60), # Detectability
            np.random.uniform(0.80, 1.00)  # Vibration
        ],

        [
            "Sensor",
            np.random.uniform(0.01, 0.05), # Failure_Prob
            np.random.uniform(0.20, 0.40), # Severity
            np.random.uniform(0.90, 0.99), # Detectability
            np.random.uniform(0.05, 0.20)  # Vibration
        ],

        [
            "Valve",
            np.random.uniform(0.10, 0.20), # Failure_Prob
            np.random.uniform(0.60, 0.80), # Severity
            np.random.uniform(0.60, 0.80), # Detectability
            np.random.uniform(0.30, 0.60)  # Vibration
        ]
    ]

    return pd.DataFrame(
        data,
        columns=[
            "Component",
            "Failure_Prob",
            "Severity",
            "Detectability",
            "Vibration"
        ]
    )
