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

# file paths for the cell measurements of each mutant (change depending on day)
file_paths = ['/Users/nataliaionescu/Documents/PKM2/jobs_results/log/E3Q_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/log/Q10E_all_data/Series1_Z1_fluorescent_cell_measurements.csv', '/Users/nataliaionescu/Documents/PKM2/jobs_results/log/WT_all_data/Series1_Z1_fluorescent_cell_measurements.csv']   
protein_names = ['E3Q', 'Q10E', 'WT']
fractions = []

for file_path in file_paths:
    fraction = calculate_foci_fraction(file_path)
    fractions.append(fraction)
    print(f'Fraction of cells with foci {fraction:.3f}')

# plot
plt.figure(figsize=(8,6))
colors = ['blue', 'orange', 'green']
bars = plt.bar(protein_names, fractions, color=colors, edgecolor='black')

x = range(len(protein_names))
plt.xlabel('Protein')
plt.ylabel('Fraction of cells containing foci')
ax = plt.gca()
#ax.set_ylim([1.2, 1.4])
plt.title('Log: Comparison of fractions of cells containing foci')
plt.xticks(x, protein_names)

plt.tight_layout()
plt.show()

  

