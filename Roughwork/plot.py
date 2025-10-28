import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Range of total cups to explore
total_cups = np.arange(4, 21, 2)  # even numbers: 4, 6, 8, ..., 20

# Assume half are tea-first and half milk-first (rounded down if odd)
probs = []
for n in total_cups:
    n_milk = n // 2
    p = 1 / comb(n, n_milk)
    probs.append(p)

# Plot the results
plt.figure(figsize=(8, 5))
plt.plot(total_cups, probs, marker='o', linestyle='-', color='steelblue')
plt.title('Probability of Perfect Guess by Chance\n(Lady Tasting Tea Extended)', fontsize=14)
plt.xlabel('Total Number of Cups', fontsize=12)
plt.ylabel('Probability (All Correct by Chance)', fontsize=12)
plt.yscale('log')  # log scale to show rapid decay
plt.grid(True, which='both', linestyle='--', alpha=0.6)
plt.show()