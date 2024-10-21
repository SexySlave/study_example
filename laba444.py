import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Defining the functions based on the provided methods

# Method 1: Using random.randint()
def my_rand1(start, end, n):
    return [random.randint(start, end) for _ in range(n)]

# Method 2: Using random.sample()
def my_rand2(start, end, n):
    return random.sample(range(start, end + 1), n)

# Method 3: Using list comprehension + randrange()
def my_rand3(start, end, n):
    return [random.randrange(start, end + 1) for _ in range(n)]

# Method 4: Using loop + random.randint()
def my_rand4(start, end, n):
    rand_list = []
    for _ in range(n):
        rand_list.append(random.randint(start, end))
    return rand_list

# Method 5: Using numpy.random.randint()
def my_rand5(low, high, n):
    return list(np.random.randint(low, high + 1, size=n))

# Method 6: Using random_sample
def my_rand6(n):
    return list(np.random.random_sample(size=n) * 6 + 1)  # Scale to [1, 6]

# Defining the number of rolls for each set of trials
rolls = [100, 1000, 10000, 1000000]

# Dictionary to store results
results = {}

# Perform each method for 100, 1000, 10 000, 1 000 000 dice rolls (range 1-6)
for num_rolls in rolls:
    results[f'method1_{num_rolls}_rolls'] = my_rand1(1, 6, num_rolls)
    results[f'method2_{num_rolls}_rolls'] = my_rand3(1, 6, num_rolls)
    results[f'method3_{num_rolls}_rolls'] = my_rand3(1, 6, num_rolls)
    results[f'method4_{num_rolls}_rolls'] = my_rand4(1, 6, num_rolls)
    results[f'method5_{num_rolls}_rolls'] = my_rand5(1, 6, num_rolls)
    results[f'method6_{num_rolls}_rolls'] = my_rand6(num_rolls)

# Convert results into a pandas DataFrame for better organization
df_results = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in results.items()]))

# Prepare to plot histograms with random colors
bins = range(1, 8)  # Bins for dice values 1-6

fig, axs = plt.subplots(6, 4, figsize=(20, 18))  # Now 6 methods, 4 different roll sets

for i, method in enumerate([f'method{i+1}_' for i in range(6)]):
    for j, num_rolls in enumerate(rolls):
        # Selecting the data for the given method and roll number
        column_name = f'{method}{num_rolls}_rolls'
        data = df_results[column_name].dropna()

        # Generate random colors for each bar (1 color per bin)
        num_bins = len(bins) - 1  # Number of bins (1-6) is 6
        colors = np.random.rand(num_bins, 4)  # Generate random RGBA colors

        # Plotting histogram with one random color per bin
        n, bins, patches = axs[i, j].hist(data, bins=bins, edgecolor='black', alpha=0.75)

        # Apply a random color to each bin
        for patch in patches:
            patch.set_facecolor(np.random.rand(4,))  # Random RGBA color for each bin

        axs[i, j].set_title(f'{method.strip("_")} {num_rolls} rolls')
        axs[i, j].set_xlabel('Dice Value')
        axs[i, j].set_ylabel('Frequency')
        axs[i, j].set_xticks(bins)

plt.tight_layout()
plt.show()
