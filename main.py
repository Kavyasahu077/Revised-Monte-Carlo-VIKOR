# main.py

import pandas as pd
from config import COMPONENTS, N_SIM

from data.generator import generate_data
from simulation.monte_carlo import run_monte_carlo
from results_visualisation.plots import (
    plot_risk,
    plot_rank_probability,
    plot_distribution
)

def main():

    # Step 1: Data
    df = generate_data()
    print("\nINPUT DATA:\n", df)

    # Step 2: Monte Carlo Pipeline
    q_store, rank_store = run_monte_carlo(df, N_SIM)

    # Step 3: Results aggregation
    mean_q = q_store.mean(axis=0)

    result_df = pd.DataFrame({
        "Component": COMPONENTS,
        "Risk Score": mean_q,
        "Rank1 Probability": rank_store[:, 0] / N_SIM
        }).sort_values("Risk Score", ascending=False)

    print("\nFINAL RISK RANKING:\n", result_df)

    # Step 4: Visualization
    plot_risk(result_df)
    plot_rank_probability(rank_store, COMPONENTS)
    plot_distribution(q_store, COMPONENTS)

if __name__ == "__main__":
    main()
