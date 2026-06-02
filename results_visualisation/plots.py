# results_visualisation/plots.py

import matplotlib.pyplot as plt
import numpy as np

def plot_risk(result_df):

    plt.figure()
    plt.bar(result_df["Component"], result_df["Risk Score"])
    plt.title("VIKOR Risk Score")
    plt.show()

def plot_rank_probability(rank_store, components):

    rank1 = rank_store[:, 0] / rank_store[:, 0].sum()

    plt.figure()
    plt.bar(components, rank1)
    plt.title("Probability of Being Most Risky")
    plt.show()

def plot_distribution(q_store, components):

    plt.figure()
    for i, c in enumerate(components):
        plt.hist(q_store[:, i], alpha=0.5, label=c)

    plt.legend()
    plt.title("Monte Carlo Risk Distribution")
    plt.show()
