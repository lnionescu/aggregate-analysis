import matplotlib.pyplot as plt
import seaborn as sns
from mean_ci import bin_values
import pandas as pd
import numpy as np

file_paths = ['/Users/nataliaionescu/Documents/PKM2/prelim/day1/Formation/E3Q_fluorescent.png_cell_rsd.csv', '/Users/nataliaionescu/Documents/PKM2/prelim/day1/Formation/Q10E_fluorescent.png_cell_rsd.csv', '/Users/nataliaionescu/Documents/PKM2/prelim/day1/Formation/WT_fluorescent.png_cell_rsd.csv'   ]


protein_names = ['E3Q', 'Q10E', 'WT']
means = []
lower_cis = []
upper_cis = []


# process all files and plot on the same figure
for i, file_path in enumerate(file_paths):
    df = pd.read_csv(file_path)
    mean, lower_ci, upper_ci = bin_values(df, n_bins=100)
    means.append(mean)
    lower_cis.append(lower_ci)
    upper_cis.append(upper_ci)

plt.figure(figsize=(10,6))
x = range(len(protein_names))
plt.bar(x, means, color='skyblue', edgecolor='navy')

for i, (mean, lower, upper) in enumerate(zip(means, lower_cis, upper_cis)):
    lower_err = np.abs(mean - lower)
    upper_err = np.abs(upper - mean)
    plt.errorbar(i, mean, yerr=[[lower_err], [upper_err]], color='black')

plt.xlabel('Protein')
plt.ylabel('Mean RSD value of cell intensities')
ax = plt.gca()
ax.set_ylim([1.2, 1.4])
plt.title('Day 1: Comparison of mean RSD values with 95% confidence intervals')
plt.xticks(x, protein_names)

plt.tight_layout()
plt.show()













