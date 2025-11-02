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



'''
import numpy as np
import itertools
import math
from ipywidgets import interact, IntSlider
from IPython.display import display, clear_output

# --- Experiment Parameters (Original 8-Cup Setup) ---
N_CUPS = 8          # Total number of cups
K_CORRECT = 4       # Number of 'correct' type cups
N_GUESSES = 4       # Number of cups the Lady selects as 'correct'

# Calculate Theoretical Probability (Done once)
theoretical_combinations = math.factorial(N_CUPS) / (math.factorial(K_CORRECT) * math.factorial(N_CUPS - K_CORRECT))
theoretical_probability = 1 / theoretical_combinations

# --- Simulation Function ---
def run_simulation(N_TRIALS):
    """Runs the Lady Tasting Tea simulation for the given number of trials."""
    
    # Define the cup labels (4 correct, 4 incorrect)
    CUP_LABELS = np.array([1] * K_CORRECT + [0] * (N_CUPS - K_CORRECT))
    
    perfect_matches = 0
    
    for _ in range(N_TRIALS):
        # 1. Randomly shuffle the 8 cup labels.
        shuffled_labels = np.random.permutation(CUP_LABELS)

        # 2. A perfect match occurs if all 4 selections were 'correct' cups.
        if np.sum(shuffled_labels[:N_GUESSES]) == K_CORRECT:
            perfect_matches += 1

    # Calculate Simulated Probability
    simulated_probability = perfect_matches / N_TRIALS

    # --- Print Results ---
    clear_output(wait=True) # Clears the previous output before printing new results
    print(f"--- Lady Tasting Tea Simulation (N=8, K=4) ---")
    print(f"Total Trials Run: {N_TRIALS:,}")
    print(f"Perfect Matches (Successes): {perfect_matches:,}")
    print("-" * 30)
    print(f"Simulated Probability (by chance): {simulated_probability:.8f}")
    print(f"Theoretical Probability (1/{int(theoretical_combinations)}): {theoretical_probability:.8f}")
    print("-" * 30)
    
# --- Create the Interactive Widget ---
# Creates a slider ranging from 1,000 to 1,000,000, starting at 10,000.
interact(run_simulation, 
         N_TRIALS=IntSlider(min=1000, max=1000000, step=1000, value=10000, description='Trials:'));
'''

# Simulation with prompt:

'''
import numpy as np
import itertools
import math
from ipywidgets import Text, Button, VBox, HBox, Output
from IPython.display import display, clear_output

# --- Experiment Parameters (Original 8-Cup Setup: N=8, K=4) ---
N_CUPS = 8
K_CORRECT = 4
N_GUESSES = 4

# Calculate Theoretical Probability (Done once)
theoretical_combinations = math.factorial(N_CUPS) / (math.factorial(K_CORRECT) * math.factorial(N_CUPS - K_CORRECT))
theoretical_probability = 1 / theoretical_combinations

# --- Widget Setup ---
# 1. Input Field
trials_input = Text(
    value='100000',
    description='Enter Trials:',
    disabled=False,
    style={'description_width': 'initial'}
)

# 2. Button
run_button = Button(description="Run Simulation")

# 3. Output Area (Where results will be printed)
output_area = Output()

# --- Simulation Function ---
def run_simulation(N_TRIALS):
    """Runs the Lady Tasting Tea simulation for the given number of trials."""
    
    # Ensure N_TRIALS is an integer
    try:
        N_TRIALS = int(N_TRIALS)
        if N_TRIALS <= 0:
            raise ValueError
    except ValueError:
        print("Please enter a valid, positive integer for the number of trials.")
        return

    # Define the cup labels (4 correct, 4 incorrect)
    CUP_LABELS = np.array([1] * K_CORRECT + [0] * (N_CUPS - K_CORRECT))
    
    perfect_matches = 0
    
    # Run the simulation loop
    for _ in range(N_TRIALS):
        shuffled_labels = np.random.permutation(CUP_LABELS)
        if np.sum(shuffled_labels[:N_GUESSES]) == K_CORRECT:
            perfect_matches += 1

    # Calculate Simulated Probability
    simulated_probability = perfect_matches / N_TRIALS

    # --- Print Results ---
    with output_area:
        clear_output(wait=True) 
        print(f"--- Simulation Results (N=8, K=4) ---")
        print(f"Total Trials Run: {N_TRIALS:,}")
        print(f"Perfect Matches (Successes): {perfect_matches:,}")
        print("-" * 30)
        print(f"Simulated Probability (by chance): {simulated_probability:.8f}")
        print(f"Theoretical Probability (1/{int(theoretical_combinations)}): {theoretical_probability:.8f}")
        print("-" * 30)

# --- Define the Button Click Action ---
def on_button_click(b):
    """Callback function executed when the button is clicked."""
    run_simulation(trials_input.value)

# Link the button to the action
run_button.on_click(on_button_click)

# --- Display Widgets ---
# Use VBox and HBox to organize the layout
controls = HBox([trials_input, run_button])
display(VBox([controls, output_area]))
'''
