# Original setup parameters:

no_cups = 8                  # Total number of cups (N). 
no_cups_milk_first = 4       # Number of 'correct' milk-first cups (K).
no_guesses = 4               # Number of cups selected correctly (milk-first).
no_trials = 100000           # Number of trials.

# Define the labels:
# Array with 4 'correct' correct cups: [1] 
# Array with 4 'incorrect' cups: [0]
cup_labels = np.array([1] * no_cups_milk_first + [0] * (no_cups - no_cups_milk_first))

# Simulation.
perfect_matches = 0

# For loop.

for _ in range(no_trials):
    # Randomly shuffle the 8 cup labels.
    shuffled_labels = np.random.permutation(cup_labels)

    # Simulate the lady picking 4 cups (the first 4 positions).
    selections = shuffled_labels[:no_guesses]

    # A perfect match occurs if all 4 selections were 'correct' cups (sum == 4).
    if np.sum(selections) == no_cups_milk_first:
        perfect_matches += 1

# Calculate the simulated probability.
simulated_probability = perfect_matches / no_trials

# Calculate theoretical_combinations using itertools.
theoretical_combinations = len(list(itertools.combinations(range(no_cups), no_cups_milk_first)))

# Calculate the theoretical probability.
theoretical_probability = 1 / theoretical_combinations

# Print.
print(f"Total Cups (N): {no_cups}, Correct Cups (K): {no_cups_milk_first}")
print(f"Total Trials: {no_trials}")
print(f"Successes: {perfect_matches}")
print("-" * 50)
print(f"Simulated Probability (by chance): {simulated_probability:.8f}")
print(f"Theoretical Combinations (8 choose 4): {theoretical_combinations}")
print(f"Theoretical Probability (1/{theoretical_combinations}): {theoretical_probability:.8f}")