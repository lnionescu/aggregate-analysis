import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def calculate_foci_fraction(csv_path):
    """
    Calculates fraction of cells containing foci from the cell measurements csv file
    Returns: cells_with_foci / total_cells fraction
    """
    df = pd.read_csv(csv_path)
    total_cells = len(df)
    cells_with_foci = df['has_aggregate'].sum()
    fraction = cells_with_foci / total_cells if total_cells > 0 else 0
    return fraction

# File paths for Series 1
day1_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series1_Zsum_fluorescent_cell_measurements.csv'
]
day2_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series1_Zsum_fluorescent_cell_measurements.csv'
]
day3_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series1_Zsum_fluorescent_cell_measurements.csv'
]
log_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series1_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series1_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series1_Zsum_fluorescent_cell_measurements.csv'
]

# File paths for Series 2
day1_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series2_Zsum_fluorescent_cell_measurements.csv'
]
day2_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series2_Zsum_fluorescent_cell_measurements.csv'
]
day3_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series2_Zsum_fluorescent_cell_measurements.csv'
]
log_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series2_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series2_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series2_Zsum_fluorescent_cell_measurements.csv'
]

# File paths for Series 3
day1_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series3_Zsum_fluorescent_cell_measurements.csv'
]
day2_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series3_Zsum_fluorescent_cell_measurements.csv'
]
day3_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series3_Zsum_fluorescent_cell_measurements.csv'
]
log_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series3_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series3_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series3_Zsum_fluorescent_cell_measurements.csv'
]

# File paths for Series 4
day1_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series4_Zsum_fluorescent_cell_measurements.csv'
]
day2_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series4_Zsum_fluorescent_cell_measurements.csv'
]
day3_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series4_Zsum_fluorescent_cell_measurements.csv'
]
log_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series4_Zsum_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series4_Zsum_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series4_Zsum_fluorescent_cell_measurements.csv'
]

protein_names = ['E3Q', 'Q10E', 'WT']
colors = ['blue', 'orange', 'green']

# Calculate fractions for each series
day1_s1_fractions = [calculate_foci_fraction(path) for path in day1_s1_paths]
day2_s1_fractions = [calculate_foci_fraction(path) for path in day2_s1_paths]
day3_s1_fractions = [calculate_foci_fraction(path) for path in day3_s1_paths]
log_s1_fractions = [calculate_foci_fraction(path) for path in log_s1_paths]

day1_s2_fractions = [calculate_foci_fraction(path) for path in day1_s2_paths]
day2_s2_fractions = [calculate_foci_fraction(path) for path in day2_s2_paths]
day3_s2_fractions = [calculate_foci_fraction(path) for path in day3_s2_paths]
log_s2_fractions = [calculate_foci_fraction(path) for path in log_s2_paths]

day1_s3_fractions = [calculate_foci_fraction(path) for path in day1_s3_paths]
day2_s3_fractions = [calculate_foci_fraction(path) for path in day2_s3_paths]
day3_s3_fractions = [calculate_foci_fraction(path) for path in day3_s3_paths]
log_s3_fractions = [calculate_foci_fraction(path) for path in log_s3_paths]

day1_s4_fractions = [calculate_foci_fraction(path) for path in day1_s4_paths]
day2_s4_fractions = [calculate_foci_fraction(path) for path in day2_s4_paths]
day3_s4_fractions = [calculate_foci_fraction(path) for path in day3_s4_paths]
log_s4_fractions = [calculate_foci_fraction(path) for path in log_s4_paths]

# Series 1 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s1_fractions, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 1')
axes[0,1].bar(protein_names, day2_s1_fractions, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 1')
axes[1,0].bar(protein_names, day3_s1_fractions, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 1')
axes[1,1].bar(protein_names, log_s1_fractions, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 1')
plt.suptitle('Series 1: Fraction of cells with foci')
plt.tight_layout()
plt.show()

# Series 2 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s2_fractions, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 2')
axes[0,1].bar(protein_names, day2_s2_fractions, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 2')
axes[1,0].bar(protein_names, day3_s2_fractions, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 2')
axes[1,1].bar(protein_names, log_s2_fractions, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 2')
plt.suptitle('Series 2: Fraction of cells with foci')
plt.tight_layout()
plt.show()

# Series 3 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s3_fractions, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 3')
axes[0,1].bar(protein_names, day2_s3_fractions, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 3')
axes[1,0].bar(protein_names, day3_s3_fractions, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 3')
axes[1,1].bar(protein_names, log_s3_fractions, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 3')
plt.suptitle('Series 3: Fraction of cells with foci')
plt.tight_layout()
plt.show()

# Series 4 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s4_fractions, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 4')
axes[0,1].bar(protein_names, day2_s4_fractions, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 4')
axes[1,0].bar(protein_names, day3_s4_fractions, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 4')
axes[1,1].bar(protein_names, log_s4_fractions, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 4')
plt.suptitle('Series 4: Fraction of cells with foci')
plt.tight_layout()
plt.show()

# Calculate averages across all 4 series
day1_avg = [(day1_s1_fractions[i] + day1_s2_fractions[i] + day1_s3_fractions[i] + day1_s4_fractions[i])/4 for i in range(3)]
day2_avg = [(day2_s1_fractions[i] + day2_s2_fractions[i] + day2_s3_fractions[i] + day2_s4_fractions[i])/4 for i in range(3)]
day3_avg = [(day3_s1_fractions[i] + day3_s2_fractions[i] + day3_s3_fractions[i] + day3_s4_fractions[i])/4 for i in range(3)]
log_avg = [(log_s1_fractions[i] + log_s2_fractions[i] + log_s3_fractions[i] + log_s4_fractions[i])/4 for i in range(3)]

# Average 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_avg, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Average')
axes[0,1].bar(protein_names, day2_avg, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Average')
axes[1,0].bar(protein_names, day3_avg, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Average')
axes[1,1].bar(protein_names, log_avg, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Average')
plt.suptitle('AVERAGE: Fraction of cells with foci (across all 4 series)')
plt.tight_layout()
plt.show()

# Calculate differences from log (average)
day1_diff_avg = [day1_avg[i] - log_avg[i] for i in range(3)]
day2_diff_avg = [day2_avg[i] - log_avg[i] for i in range(3)]
day3_diff_avg = [day3_avg[i] - log_avg[i] for i in range(3)]

# Differences plot
plt.figure(figsize=(8,6))
plt.bar(protein_names, day1_diff_avg, color=colors, edgecolor='black')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.xlabel('Protein')
plt.ylabel('Difference in fraction (Day 1 - Log)')
plt.title('AVERAGE: Day 1 - Log (across all 4 series)')
plt.show()

plt.figure(figsize=(8,6))
plt.bar(protein_names, day2_diff_avg, color=colors, edgecolor='black')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.xlabel('Protein')
plt.ylabel('Difference in fraction (Day 2 - Log)')
plt.title('AVERAGE: Day 2 - Log (across all 4 series)')
plt.show()

plt.figure(figsize=(8,6))
plt.bar(protein_names, day3_diff_avg, color=colors, edgecolor='black')
plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
plt.xlabel('Protein')
plt.ylabel('Difference in fraction (Day 3 - Log)')
plt.title('AVERAGE: Day 3 - Log (across all 4 series)')
plt.show()

print("Average results:")
print("Day 1 avg:", [f"{f:.3f}" for f in day1_avg])
print("Day 2 avg:", [f"{f:.3f}" for f in day2_avg])
print("Day 3 avg:", [f"{f:.3f}" for f in day3_avg])
print("Log avg:", [f"{f:.3f}" for f in log_avg])















  

