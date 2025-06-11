import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Input: paths to cell measurement csv of files for each series of every day
Output: individual series/series averaged plots showing the time evolution of the mean of the cell intensities excluding foci
'''

def rest_of_cell_mean(csv_path):
    '''
    Selects the rest of cell mean intensity from csv of cell measurements
    Returns: this value which is already calculated in the csv file
    '''
    df = pd.read_csv(csv_path)
    df['selected_intensity'] = df.apply(
        lambda row: row['rest_of_cell_mean_intensity'] if row['has_aggregate'] else row['cell_mean_intensity'],
        axis=1)

    # average
    average_intensity = df['selected_intensity'].mean()
    return average_intensity


# File paths for Series 1
day1_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series1_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series1_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series1_Zmax_fluorescent_cell_measurements.csv'
]
day2_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series1_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series1_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series1_Zmax_fluorescent_cell_measurements.csv'
]
day3_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series1_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series1_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series1_Zmax_fluorescent_cell_measurements.csv'
]
log_s1_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series1_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series1_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series1_Zmax_fluorescent_cell_measurements.csv'
]

# File paths for Series 2
day1_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series2_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series2_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series2_Zmax_fluorescent_cell_measurements.csv'
]
day2_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series2_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series2_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series2_Zmax_fluorescent_cell_measurements.csv'
]
day3_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series2_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series2_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series2_Zmax_fluorescent_cell_measurements.csv'
]
log_s2_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series2_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series2_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series2_Zmax_fluorescent_cell_measurements.csv'
]

# File paths for Series 3
day1_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series3_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series3_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series3_Zmax_fluorescent_cell_measurements.csv'
]
day2_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series3_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series3_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series3_Zmax_fluorescent_cell_measurements.csv'
]
day3_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series3_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series3_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series3_Zmax_fluorescent_cell_measurements.csv'
]
log_s3_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series3_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series3_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series3_Zmax_fluorescent_cell_measurements.csv'
]

# File paths for Series 4
day1_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/E3Q_Series4_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/Q10E_Series4_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day1/WT_Series4_Zmax_fluorescent_cell_measurements.csv'
]
day2_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/E3Q_Series4_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/Q10E_Series4_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day2/WT_Series4_Zmax_fluorescent_cell_measurements.csv'
]
day3_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/E3Q_Series4_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/Q10E_Series4_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_day3/WT_Series4_Zmax_fluorescent_cell_measurements.csv'
]
log_s4_paths = [
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/E3Q_Series4_Zmax_fluorescent_cell_measurements.csv',
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/Q10E_Series4_Zmax_fluorescent_cell_measurements.csv', 
    '/Users/nataliaionescu/Documents/PKM2/z_projection_results/nd2_log/WT_Series4_Zmax_fluorescent_cell_measurements.csv'
]

protein_names = ['E3Q', 'Q10E', 'WT']
colors = ['blue', 'orange', 'green']

# Calculate fractions for each series
day1_s1_means = [rest_of_cell_mean(path) for path in day1_s1_paths]
day2_s1_means = [rest_of_cell_mean(path) for path in day2_s1_paths]
day3_s1_means = [rest_of_cell_mean(path) for path in day3_s1_paths]
log_s1_means = [rest_of_cell_mean(path) for path in log_s1_paths]

day1_s2_means = [rest_of_cell_mean(path) for path in day1_s2_paths]
day2_s2_means = [rest_of_cell_mean(path) for path in day2_s2_paths]
day3_s2_means = [rest_of_cell_mean(path) for path in day3_s2_paths]
log_s2_means = [rest_of_cell_mean(path) for path in log_s2_paths]

day1_s3_means = [rest_of_cell_mean(path) for path in day1_s3_paths]
day2_s3_means = [rest_of_cell_mean(path) for path in day2_s3_paths]
day3_s3_means = [rest_of_cell_mean(path) for path in day3_s3_paths]
log_s3_means = [rest_of_cell_mean(path) for path in log_s3_paths]

day1_s4_means = [rest_of_cell_mean(path) for path in day1_s4_paths]
day2_s4_means = [rest_of_cell_mean(path) for path in day2_s4_paths]
day3_s4_means = [rest_of_cell_mean(path) for path in day3_s4_paths]
log_s4_means = [rest_of_cell_mean(path) for path in log_s4_paths]

# Series 1 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s1_means, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 1')
axes[0,1].bar(protein_names, day2_s1_means, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 1')
axes[1,0].bar(protein_names, day3_s1_means, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 1')
axes[1,1].bar(protein_names, log_s1_means, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 1')
plt.suptitle('Series 1: Mean cell intensities excluding foci')
plt.tight_layout()
plt.show()

# Series 2 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s2_means, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 2')
axes[0,1].bar(protein_names, day2_s2_means, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 2')
axes[1,0].bar(protein_names, day3_s2_means, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 2')
axes[1,1].bar(protein_names, log_s2_means, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 2')
plt.suptitle('Series 2: Mean cell intensities excluding foci')
plt.tight_layout()
plt.show()

# Series 3 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s3_means, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 3')
axes[0,1].bar(protein_names, day2_s3_means, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 3')
axes[1,0].bar(protein_names, day3_s3_means, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 3')
axes[1,1].bar(protein_names, log_s3_means, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 3')
plt.suptitle('Series 3: Mean cell intensities excluding foci')
plt.tight_layout()
plt.show()

# Series 4 - 2x2 plot
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes[0,0].bar(protein_names, day1_s4_means, color=colors, edgecolor='black')
axes[0,0].set_title('Day 1 - Series 4')
axes[0,1].bar(protein_names, day2_s4_means, color=colors, edgecolor='black')
axes[0,1].set_title('Day 2 - Series 4')
axes[1,0].bar(protein_names, day3_s4_means, color=colors, edgecolor='black')
axes[1,0].set_title('Day 3 - Series 4')
axes[1,1].bar(protein_names, log_s4_means, color=colors, edgecolor='black')
axes[1,1].set_title('Log - Series 4')
plt.suptitle('Series 4: Mean cell intensities excluding foci')
plt.tight_layout()
plt.show()

# Calculate averages across all 4 series
day1_avg = [(day1_s1_means[i] + day1_s2_means[i] + day1_s3_means[i] + day1_s4_means[i])/4 for i in range(3)]
day2_avg = [(day2_s1_means[i] + day2_s2_means[i] + day2_s3_means[i] + day2_s4_means[i])/4 for i in range(3)]
day3_avg = [(day3_s1_means[i] + day3_s2_means[i] + day3_s3_means[i] + day3_s4_means[i])/4 for i in range(3)]
log_avg = [(log_s1_means[i] + log_s2_means[i] + log_s3_means[i] + log_s4_means[i])/4 for i in range(3)]

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















  


