import pandas as pd
import numpy as np
import glob

# Read all CSV files and collect intensities
csv_files = glob.glob("/Users/nataliaionescu/Documents/PKM2/complete/day1/E3Q_all_data/*_cell_measurements.csv")
all_intensities = []

for file in csv_files:
    df = pd.read_csv(file)
    all_intensities.extend(df['cell_mean_intensity'].values)

# Calculate RSD
all_intensities = np.array(all_intensities)
mean_intensity = np.mean(all_intensities)
std_intensity = np.std(all_intensities)
rsd_percent = (std_intensity / mean_intensity) * 100

# Print results
print(f"Total cells analyzed: {len(all_intensities)}")
print(f"Mean intensity: {mean_intensity:.2f}")
print(f"Standard deviation: {std_intensity:.2f}")
print(f"RSD: {rsd_percent:.2f}%")
