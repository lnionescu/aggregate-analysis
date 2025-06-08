import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Input: csv files of the cell measurements for each mutant on the desired day
Output: bar plot showing the fractions of cells with foci for each mutant
'''

def calculate_foci_fraction(csv_path):
    '''
    calculates fraction of cells containing foci from the cell measurements csv file
    returns: cells_with_foci / total_cells fraction
    '''
    # read csv of cell measurements and get each number of cells
    df = pd.read_csv(csv_path)
    total_cells = len(df)
    cells_with_foci = df['has_aggregate'].sum()
    fraction = cells_with_foci / total_cells if total_cells > 0 else 0
    return fraction

# file paths for each day and mutant, write all of them in order to subtract the baseline values
# currently doing: series 1, z-slice 1
day1_paths = ['/Users/nataliaionescu/Documents/PKM2/jobs_results/day1/E3Q_all_data/Series1_Z1_fluorescent.png_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/day1/Q10E_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/day1/WT_all_data/Series1_Z1_fluorescent_cell_measurements.csv']

day2_paths = ['/Users/nataliaionescu/Documents/PKM2/jobs_results/day2/E3Q_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/day2/Q10E_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/day2/WT_all_data/Series1_Z1_fluorescent_cell_measurements.csv']

day3_paths = ['/Users/nataliaionescu/Documents/PKM2/jobs_results/day3/E3Q_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/day3/Q10E_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/day3/WT_all_data/Series1_Z1_fluorescent_cell_measurements.csv']

log_paths = ['/Users/nataliaionescu/Documents/PKM2/jobs_results/log/E3Q_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/log/Q10E_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/log/WT_all_data/Series1_Z1_fluorescent_cell_measurements.csv']   

protein_names = ['E3Q', 'Q10E', 'WT']
colors = ['blue', 'orange', 'green']

# fractions for each day
day1_fractions = [calculate_foci_fraction(path) for path in day1_paths]
day2_fractions = [calculate_foci_fraction(path) for path in day2_paths]
day3_fractions = [calculate_foci_fraction(path) for path in day3_paths]
log_fractions = [calculate_foci_fraction(path) for path in log_paths]

# plot day 1 
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, day1_fractions, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Day 1: Fraction of cells containing foci')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()

# plot day 2
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, day2_fractions, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Day 2: Fraction of cells containing foci')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()

# plot day 3
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, day3_fractions, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Day 3: Fraction of cells containing foci')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()

# plot log
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, log_fractions, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Log: Fraction of cells containing foci')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()

# get differences day - log
day1_diff = [day1_fractions[i] - log_fractions[i] for i in range(3)]
day2_diff = [day2_fractions[i] - log_fractions[i] for i in range(3)]
day3_diff = [day3_fractions[i] - log_fractions[i] for i in range(3)]

# plot day 1 - log
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, day1_diff, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Day 1: Fraction of cells containing foci, subtracting baseline values')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()

# plot day 2 - log
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, day2_diff, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Day 2: Fraction of cells containing foci, subtracting baseline values')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()

# plot day 3 - log
plt.figure(figsize=(8,6))
bars = plt.bar(protein_names, day3_diff, color=colors, edgecolor='black')
x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
plt.title('Day 3: Fraction of cells containing foci, subtracting baseline values')
plt.xticks(x, protein_names)
plt.tight_layout()
plt.show()
















  

