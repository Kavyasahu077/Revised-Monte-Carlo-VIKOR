# data/generator.py

import numpy as np
import pandas as pd
from config import COMPONENTS

def generate_data():
    data = []

    for c in COMPONENTS:
        data.append([
            c,
            np.random.uniform(0.05, 0.3),   # base failure prob
            np.random.uniform(0.6, 0.95),   # severity
            np.random.uniform(0.5, 0.9),    # detectability
            np.random.uniform(0.1, 1.0)     # vibration
        ])

    return pd.DataFrame(data, columns=[
        "Component", "Failure_Prob", "Severity", "Detectability", "Vibration"
    ])