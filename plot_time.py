import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from rsd_confidence_intervals import bin_values

def calculate_rsd_mean_ci(csv_path):
    """
    Calculate mean RSD and confidence intervals using existing bin_values function
    Returns: mean, lower_ci, upper_ci
    """
    try:
        df = pd.read_csv(csv_path)
        mean, lower_ci, upper_ci = bin_values(df, n_bins=100, confidence=0.05)
        return mean, lower_ci, upper_ci
    except FileNotFoundError:
        print(f"Warning: File not found - {csv_path}")
        return 0, 0, 0


# File paths for Series 1 RSD files
day1_s1_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series1_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series1_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series1_Zmax_fluorescent_cell_rsd.csv'
]
day2_s1_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series1_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series1_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series1_Zmax_fluorescent_cell_rsd.csv'
]
day3_s1_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series1_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series1_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series1_Zmax_fluorescent_cell_rsd.csv'
]
log_s1_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series1_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series1_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series1_Zmax_fluorescent_cell_rsd.csv'
]

# File paths for Series 2 RSD files
day1_s2_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series2_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series2_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series2_Zmax_fluorescent_cell_rsd.csv'
]
day2_s2_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series2_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series2_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series2_Zmax_fluorescent_cell_rsd.csv'
]
day3_s2_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series2_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series2_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series2_Zmax_fluorescent_cell_rsd.csv'
]
log_s2_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series2_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series2_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series2_Zmax_fluorescent_cell_rsd.csv'
]

# File paths for Series 3 RSD files
day1_s3_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series3_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series3_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series3_Zmax_fluorescent_cell_rsd.csv'
]
day2_s3_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series3_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series3_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series3_Zmax_fluorescent_cell_rsd.csv'
]
day3_s3_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series3_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series3_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series3_Zmax_fluorescent_cell_rsd.csv'
]
log_s3_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series3_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series3_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series3_Zmax_fluorescent_cell_rsd.csv'
]

# File paths for Series 4 RSD files
day1_s4_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series4_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series4_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series4_Zmax_fluorescent_cell_rsd.csv'
]
day2_s4_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series4_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series4_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series4_Zmax_fluorescent_cell_rsd.csv'
]
day3_s4_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series4_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series4_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series4_Zmax_fluorescent_cell_rsd.csv'
]
log_s4_rsd_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series4_Zmax_fluorescent_cell_rsd.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series4_Zmax_fluorescent_cell_rsd.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series4_Zmax_fluorescent_cell_rsd.csv'
]


protein_names = ['E3Q', 'Q10E', 'WT']
colors = ['blue', 'orange', 'green']

# Calculate means and CIs for each series
day1_s1_means, day1_s1_lowers, day1_s1_uppers = [], [], []
day2_s1_means, day2_s1_lowers, day2_s1_uppers = [], [], []
day3_s1_means, day3_s1_lowers, day3_s1_uppers = [], [], []
log_s1_means, log_s1_lowers, log_s1_uppers = [], [], []

day1_s2_means, day1_s2_lowers, day1_s2_uppers = [], [], []
day2_s2_means, day2_s2_lowers, day2_s2_uppers = [], [], []
day3_s2_means, day3_s2_lowers, day3_s2_uppers = [], [], []
log_s2_means, log_s2_lowers, log_s2_uppers = [], [], []

day1_s3_means, day1_s3_lowers, day1_s3_uppers = [], [], []
day2_s3_means, day2_s3_lowers, day2_s3_uppers = [], [], []
day3_s3_means, day3_s3_lowers, day3_s3_uppers = [], [], []
log_s3_means, log_s3_lowers, log_s3_uppers = [], [], []

day1_s4_means, day1_s4_lowers, day1_s4_uppers = [], [], []
day2_s4_means, day2_s4_lowers, day2_s4_uppers = [], [], []
day3_s4_means, day3_s4_lowers, day3_s4_uppers = [], [], []
log_s4_means, log_s4_lowers, log_s4_uppers = [], [], []

# Series 1
for path in day1_s1_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day1_s1_means.append(mean)
    day1_s1_lowers.append(lower)
    day1_s1_uppers.append(upper)

for path in day2_s1_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day2_s1_means.append(mean)
    day2_s1_lowers.append(lower)
    day2_s1_uppers.append(upper)

for path in day3_s1_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day3_s1_means.append(mean)
    day3_s1_lowers.append(lower)
    day3_s1_uppers.append(upper)

for path in log_s1_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    log_s1_means.append(mean)
    log_s1_lowers.append(lower)
    log_s1_uppers.append(upper)

# Series 2
for path in day1_s2_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day1_s2_means.append(mean)
    day1_s2_lowers.append(lower)
    day1_s2_uppers.append(upper)

for path in day2_s2_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day2_s2_means.append(mean)
    day2_s2_lowers.append(lower)
    day2_s2_uppers.append(upper)

for path in day3_s2_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day3_s2_means.append(mean)
    day3_s2_lowers.append(lower)
    day3_s2_uppers.append(upper)

for path in log_s2_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    log_s2_means.append(mean)
    log_s2_lowers.append(lower)
    log_s2_uppers.append(upper)

# Series 3
for path in day1_s3_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day1_s3_means.append(mean)
    day1_s3_lowers.append(lower)
    day1_s3_uppers.append(upper)

for path in day2_s3_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day2_s3_means.append(mean)
    day2_s3_lowers.append(lower)
    day2_s3_uppers.append(upper)

for path in day3_s3_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day3_s3_means.append(mean)
    day3_s3_lowers.append(lower)
    day3_s3_uppers.append(upper)

for path in log_s3_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    log_s3_means.append(mean)
    log_s3_lowers.append(lower)
    log_s3_uppers.append(upper)

# Series 4
for path in day1_s4_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day1_s4_means.append(mean)
    day1_s4_lowers.append(lower)
    day1_s4_uppers.append(upper)

for path in day2_s4_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day2_s4_means.append(mean)
    day2_s4_lowers.append(lower)
    day2_s4_uppers.append(upper)

for path in day3_s4_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    day3_s4_means.append(mean)
    day3_s4_lowers.append(lower)
    day3_s4_uppers.append(upper)

for path in log_s4_rsd_paths:
    mean, lower, upper = calculate_rsd_mean_ci(path)
    log_s4_means.append(mean)
    log_s4_lowers.append(lower)
    log_s4_uppers.append(upper)

# Function to create error bar plots
def plot_rsd_with_error_bars(axes, x_labels, means, lowers, uppers, colors, title):
    lower_errs = [abs(means[i] - lowers[i]) for i in range(len(means))]
    upper_errs = [abs(uppers[i] - means[i]) for i in range(len(means))]
    axes.bar(x_labels, means, color=colors, edgecolor='black')
    axes.errorbar(x_labels, means, yerr=[lower_errs, upper_errs], fmt='none', color='black', capsize=5)
    axes.set_title(title)
    axes.set_ylabel('Mean RSD')

# Series 1 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plot_rsd_with_error_bars(axes[0,0], protein_names, day1_s1_means, day1_s1_lowers, day1_s1_uppers, colors, 'Day 1 - Series 1')
plot_rsd_with_error_bars(axes[0,1], protein_names, day2_s1_means, day2_s1_lowers, day2_s1_uppers, colors, 'Day 2 - Series 1')
plot_rsd_with_error_bars(axes[1,0], protein_names, day3_s1_means, day3_s1_lowers, day3_s1_uppers, colors, 'Day 3 - Series 1')
plot_rsd_with_error_bars(axes[1,1], protein_names, log_s1_means, log_s1_lowers, log_s1_uppers, colors, 'Log - Series 1')
plt.suptitle('Series 1: Mean RSD with 95% Confidence Intervals')
plt.tight_layout()
plt.show()

# Series 2 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plot_rsd_with_error_bars(axes[0,0], protein_names, day1_s2_means, day1_s2_lowers, day1_s2_uppers, colors, 'Day 1 - Series 2')
plot_rsd_with_error_bars(axes[0,1], protein_names, day2_s2_means, day2_s2_lowers, day2_s2_uppers, colors, 'Day 2 - Series 2')
plot_rsd_with_error_bars(axes[1,0], protein_names, day3_s2_means, day3_s2_lowers, day3_s2_uppers, colors, 'Day 3 - Series 2')
plot_rsd_with_error_bars(axes[1,1], protein_names, log_s2_means, log_s2_lowers, log_s2_uppers, colors, 'Log - Series 2')
plt.suptitle('Series 2: Mean RSD with 95% Confidence Intervals')
plt.tight_layout()
plt.show()

# Series 3 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plot_rsd_with_error_bars(axes[0,0], protein_names, day1_s3_means, day1_s3_lowers, day1_s3_uppers, colors, 'Day 1 - Series 3')
plot_rsd_with_error_bars(axes[0,1], protein_names, day2_s3_means, day2_s3_lowers, day2_s3_uppers, colors, 'Day 2 - Series 3')
plot_rsd_with_error_bars(axes[1,0], protein_names, day3_s3_means, day3_s3_lowers, day3_s3_uppers, colors, 'Day 3 - Series 3')
plot_rsd_with_error_bars(axes[1,1], protein_names, log_s3_means, log_s3_lowers, log_s3_uppers, colors, 'Log - Series 3')
plt.suptitle('Series 3: Mean RSD with 95% Confidence Intervals')
plt.tight_layout()
plt.show()

# Series 4 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plot_rsd_with_error_bars(axes[0,0], protein_names, day1_s4_means, day1_s4_lowers, day1_s4_uppers, colors, 'Day 1 - Series 4')
plot_rsd_with_error_bars(axes[0,1], protein_names, day2_s4_means, day2_s4_lowers, day2_s4_uppers, colors, 'Day 2 - Series 4')
plot_rsd_with_error_bars(axes[1,0], protein_names, day3_s4_means, day3_s4_lowers, day3_s4_uppers, colors, 'Day 3 - Series 4')
plot_rsd_with_error_bars(axes[1,1], protein_names, log_s4_means, log_s4_lowers, log_s4_uppers, colors, 'Log - Series 4')
plt.suptitle('Series 4: Mean RSD with 95% Confidence Intervals')
plt.tight_layout()
plt.show()

# Calculate averages across all 4 series
day1_avg_means = [(day1_s1_means[i] + day1_s2_means[i] + day1_s3_means[i] + day1_s4_means[i])/4 for i in range(3)]
day2_avg_means = [(day2_s1_means[i] + day2_s2_means[i] + day2_s3_means[i] + day2_s4_means[i])/4 for i in range(3)]
day3_avg_means = [(day3_s1_means[i] + day3_s2_means[i] + day3_s3_means[i] + day3_s4_means[i])/4 for i in range(3)]
log_avg_means = [(log_s1_means[i] + log_s2_means[i] + log_s3_means[i] + log_s4_means[i])/4 for i in range(3)]

day1_avg_lowers = [(day1_s1_lowers[i] + day1_s2_lowers[i] + day1_s3_lowers[i] + day1_s4_lowers[i])/4 for i in range(3)]
day2_avg_lowers = [(day2_s1_lowers[i] + day2_s2_lowers[i] + day2_s3_lowers[i] + day2_s4_lowers[i])/4 for i in range(3)]
day3_avg_lowers = [(day3_s1_lowers[i] + day3_s2_lowers[i] + day3_s3_lowers[i] + day3_s4_lowers[i])/4 for i in range(3)]
log_avg_lowers = [(log_s1_lowers[i] + log_s2_lowers[i] + log_s3_lowers[i] + log_s4_lowers[i])/4 for i in range(3)]

day1_avg_uppers = [(day1_s1_uppers[i] + day1_s2_uppers[i] + day1_s3_uppers[i] + day1_s4_uppers[i])/4 for i in range(3)]
day2_avg_uppers = [(day2_s1_uppers[i] + day2_s2_uppers[i] + day2_s3_uppers[i] + day2_s4_uppers[i])/4 for i in range(3)]
day3_avg_uppers = [(day3_s1_uppers[i] + day3_s2_uppers[i] + day3_s3_uppers[i] + day3_s4_uppers[i])/4 for i in range(3)]
log_avg_uppers = [(log_s1_uppers[i] + log_s2_uppers[i] + log_s3_uppers[i] + log_s4_uppers[i])/4 for i in range(3)]

# Average 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
plot_rsd_with_error_bars(axes[0,0], protein_names, day1_avg_means, day1_avg_lowers, day1_avg_uppers, colors, 'Day 1 - Average')
plot_rsd_with_error_bars(axes[0,1], protein_names, day2_avg_means, day2_avg_lowers, day2_avg_uppers, colors, 'Day 2 - Average')
plot_rsd_with_error_bars(axes[1,0], protein_names, day3_avg_means, day3_avg_lowers, day3_avg_uppers, colors, 'Day 3 - Average')
plot_rsd_with_error_bars(axes[1,1], protein_names, log_avg_means, log_avg_lowers, log_avg_uppers, colors, 'Log - Average')
plt.suptitle('AVERAGE: Mean RSD with 95% Confidence Intervals (across all 4 series)')
plt.tight_layout()
plt.show()

# Calculate differences from log (average) - following the pattern from foci_fraction.py
day1_diff_avg_means = [day1_avg_means[i] - log_avg_means[i] for i in range(3)]
day2_diff_avg_means = [day2_avg_means[i] - log_avg_means[i] for i in range(3)]
day3_diff_avg_means = [day3_avg_means[i] - log_avg_means[i] for i in range(3)]

# Propagate uncertainty for differences (assuming independent errors)
day1_diff_avg_lowers = [np.sqrt((day1_avg_means[i] - day1_avg_lowers[i])**2 + (log_avg_uppers[i] - log_avg_means[i])**2) for i in range(3)]
day1_diff_avg_uppers = [np.sqrt((day1_avg_uppers[i] - day1_avg_means[i])**2 + (log_avg_means[i] - log_avg_lowers[i])**2) for i in range(3)]

day2_diff_avg_lowers = [np.sqrt((day2_avg_means[i] - day2_avg_lowers[i])**2 + (log_avg_uppers[i] - log_avg_means[i])**2) for i in range(3)]
day2_diff_avg_uppers = [np.sqrt((day2_avg_uppers[i] - day2_avg_means[i])**2 + (log_avg_means[i] - log_avg_lowers[i])**2) for i in range(3)]

day3_diff_avg_lowers = [np.sqrt((day3_avg_means[i] - day3_avg_lowers[i])**2 + (log_avg_uppers[i] - log_avg_means[i])**2) for i in range(3)]
day3_diff_avg_uppers = [np.sqrt((day3_avg_uppers[i] - day3_avg_means[i])**2 + (log_avg_means[i] - log_avg_lowers[i])**2) for i in range(3)]

# Differences plots with error bars
plt.figure(figsize=(8,6))
plt.bar(protein_names, day1_diff_avg_means, color=colors, edgecolor='black')
plt.errorbar(protein_names, day1_diff_avg_means, yerr=[day1_diff_avg_lowers, day1_diff_avg_uppers], fmt='none', color='black', capsize=5)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.xlabel('Protein')
plt.ylabel('Difference in Mean RSD (Day 1 - Log)')
plt.title('AVERAGE: Day 1 - Log (across all 4 series)')
plt.show()

plt.figure(figsize=(8,6))
plt.bar(protein_names, day2_diff_avg_means, color=colors, edgecolor='black')
plt.errorbar(protein_names, day2_diff_avg_means, yerr=[day2_diff_avg_lowers, day2_diff_avg_uppers], fmt='none', color='black', capsize=5)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.xlabel('Protein')
plt.ylabel('Difference in Mean RSD (Day 2 - Log)')
plt.title('AVERAGE: Day 2 - Log (across all 4 series)')
plt.show()

plt.figure(figsize=(8,6))
plt.bar(protein_names, day3_diff_avg_means, color=colors, edgecolor='black')
plt.errorbar(protein_names, day3_diff_avg_means, yerr=[day3_diff_avg_lowers, day3_diff_avg_uppers], fmt='none', color='black', capsize=5)
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.xlabel('Protein')
plt.ylabel('Difference in Mean RSD (Day 3 - Log)')
plt.title('AVERAGE: Day 3 - Log (across all 4 series)')
plt.show()

print("Average RSD results:")
print("Day 1 avg means:", [f"{f:.3f}" for f in day1_avg_means])
print("Day 2 avg means:", [f"{f:.3f}" for f in day2_avg_means])
print("Day 3 avg means:", [f"{f:.3f}" for f in day3_avg_means])
print("Log avg means:", [f"{f:.3f}" for f in log_avg_means])

print("\nDifferences from Log:")
print("Day 1 - Log:", [f"{f:.3f}" for f in day1_diff_avg_means])
print("Day 2 - Log:", [f"{f:.3f}" for f in day2_diff_avg_means])
print("Day 3 - Log:", [f"{f:.3f}" for f in day3_diff_avg_means])












