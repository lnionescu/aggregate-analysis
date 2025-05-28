import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci
import os
import csv
import pandas as pd

''' 
Input: csv file of all cell measurements for a certain image
Output: csv file of RSD values for each cell in the image, calculated both including and excluding foci
'''

def get_rsd_csv(csv_file_path):
    '''
    Input: path to csv of cell measurements
    Function: computes the relative standard deviation (sd/mean) for the intensities within each cell
    Output: Saves a csv of the RSD values in the same directory and returns dataframe for plotting
    '''
    # read csv file of cell measurements
    df = pd.read_csv(csv_file_path)

    # get the directory of the input csv file
    input_dir = os.path.dirname(csv_file_path)

    # extract base name of cell measurements csv
    base_name = os.path.splitext(os.path.basename(csv_file_path))[0]
    output_file = os.path.join(input_dir, f'{base_name}_rsd_values.csv')

    # list to store results
    results = []

    # process each cell in the cell measurements csv
    for _, row in df.iterrows():
        cell_id = row['Cell ID']
        has_aggregate = row['has_aggregate']

        # calculate RSD including foci (pixels of the whole cell)
        mean_intensity_whole = row['cell_mean_intensity']
        sd_intensity_whole = row['cell_sd_intensity']
        
        if mean_intensity_whole > 0:
            rsd_whole = sd_intensity_whole / mean_intensity_whole
        else:
            rsd_whole = 0

        rsd_excluding_foci = None
        # for cells with aggregates, calculate RSD excluding foci
        if has_aggregate:
            mean_intensity_rest = row['rest_of_cell_mean_intensity']
            sd_intensity_rest = row['rest_of_cell_sd_intensity']

            if mean_intensity_rest > 0:
                rsd_excluding_foci = sd_intensity_rest / mean_intensity_rest
            else:
                rsd_excluding_foci = 0

        # store all results
        result = {'Cell ID': cell_id, 'has_aggregate': has_aggregate, 'RSD_whole_cell': rsd_whole, 'RSD_excluding_foci': rsd_excluding_foci}
        results.append(result)

    # convert to dataframe and save in the input directory
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file)

    print(f'RSD values saved to: {output_file}')
    return results_df



def plot_rsd_distribution(results_df):
    '''
    Input: dataframe of rsd values (output of get_rsd_csv() function)
    Output: two plots of RSD distributions, both including and excluding foci 
    '''

    # plot 1: RSD for the whole cell (all cells)
    plt.figure(figsize=(12,4))
    plt.bar(results_df['Cell ID'], results_df['RSD_whole_cell'])
    plt.xlabel('Cell index')
    plt.ylabel('RSD of intensity')
    plt.title('RSD - Whole cell')
    plt.show()

    # plot 2: RSD excluding foci (from the cells that have them)
    rsd_to_plot = []
    for _, row in results_df.iterrows():
        if row['has_aggregate'] and pd.notna(row['RSD_excluding_foci']):
            rsd_to_plot.append(row['RSD_excluding_foci'])
        else:
            rsd_to_plot.append(row['RSD_whole_cell'])
    plt.figure(figsize=(12,4))
    plt.bar(results_df['Cell ID'], rsd_to_plot)
    plt.xlabel('Cell index')
    plt.ylabel('RSD of intensity')
    plt.title('RSD - excluding foci')
    plt.show()


if __name__ == '__main__':
    cell_measurements_csv_path = '/Users/nataliaionescu/Documents/PKM2/thresholding/no_thresholdSeries1_Z5_fluorescent_cell_measurements.csv' 
    results_df = get_rsd_csv(cell_measurements_csv_path)
    plot_rsd_distribution(results_df)




