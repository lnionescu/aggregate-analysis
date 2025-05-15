import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def bin_values(df, n_bins=100, confidence=0.05):
    '''
    histogram with 50 bins and plot a normal distribution with data mean and standard deviation on top to check visually if the distribution is normal
    '''

    rsd_values = df['RSD'].values
    mean_val = np.mean(rsd_values)
    std_val = np.std(rsd_values)

    min_val = min(rsd_values)
    max_val = max(rsd_values)

    # bin boundaries
    bin_edges = np.linspace(min_val, max_val, n_bins+1)
    plt.figure(figsize=(12,6))
    hist, bins, _ = plt.hist(rsd_values, bins=bin_edges, color='blue', edgecolor='black')

    # confidence interval of mean using normal distribution
    # sample mean +- z_(alpha_2) * mean_standard_error
    mean_standard_error = std_val / np.sqrt(len(rsd_values))
    z_score = stats.norm.ppf(confidence/2)
    margin_of_error = z_score * mean_standard_error
    lower_ci = mean_val - margin_of_error
    upper_ci = mean_val + margin_of_error

    # add normal distribution on top
    x = np.linspace(min_val, max_val, 1000)
    bin_width = bins[1] - bins[0]
    y = stats.norm.pdf(x, mean_val, std_val) * len(rsd_values) * bin_width
    plt.plot(x, y, 'r-', label=f'Normal distribution with mean {mean_val:.4f} and standard deviation {std_val:.4f}')
    plt.xlabel('RSD Values')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.show()

    return mean_val, lower_ci, upper_ci



if __name__ == '__main__':
    file_path = '/Users/nataliaionescu/Documents/PKM2/prelim/day2/Formation/Q10E_fluorescent.png_cell_rsd.csv' 
    df = pd.read_csv(file_path)
    mean_val, lower_ci, upper_ci = bin_values(df, n_bins=100)
    print(mean_val, lower_ci, upper_ci)
    




