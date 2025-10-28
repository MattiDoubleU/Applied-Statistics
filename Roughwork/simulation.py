import numpy as np
import matplotlib.pyplot as plt
from math import comb
import ipywidgets as widgets
from ipywidgets import interact

def plot_lady_tasting(n_total=8):
    """
    Interactive plot: show probabilities for the Lady Tasting Tea experiment
    as the number of cups varies.
    """
    n_milk = n_total // 2
    total_combos = comb(n_total, n_milk)
    
    # Probability: all correct
    p_all = 1 / total_combos
    
    # Probability: at least half correct
    p_half_or_more = 0
    for k in range(int(n_milk/2), n_milk + 1):
        p_k = comb(n_milk, k) * comb(n_total - n_milk, n_milk - k) / total_combos
        p_half_or_more += p_k

    # Create bar chart
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(['All Correct', '≥ Half Correct'], [p_all, p_half_or_more],
                  color=['steelblue', 'darkorange'], alpha=0.8)
    
    # Add text labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height * 1.1,
                f'{height:.4f}', ha='center', va='bottom', fontsize=11)

    ax.set_ylim(1e-5, 1)
    ax.set_yscale('log')
    ax.set_ylabel('Probability (log scale)', fontsize=12)
    ax.set_title(f'Lady Tasting Tea — n = {n_total} cups\n'
                 f'(8 Tea-first, 4 Milk-first shown for n=12)', fontsize=13)
    ax.grid(True, which='both', linestyle='--', alpha=0.6)
    plt.show()

# Create interactive slider
interact(plot_lady_tasting, n_total=widgets.IntSlider(value=8, min=4, max=20, step=2, description='Total Cups:'))
