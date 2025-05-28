import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci
import os
import csv

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
        sd_intensity_whole = row['sd_intensity_whole']
        
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
        result = {'Cell ID': cell_id, 'has_aggregate': has_aggregate, 'RSD_whole_cell': rsd_whole_cell, 'RSD_excluding_foci': rsd_excluding_foci}
        results.append(result)

    # convert to dataframe and save in the input directory
    results_df = pd.DataFrame(results)
    results_df.to_csv(output_file)

    print(f'RSD values saved to: {output_file}')
    return results_df



def plot_distribution(rsd_values):
    '''
    input: dictionary of rsd values of all cells in the image under analysis
    '''

    plt.bar(rsd_values.keys(), rsd_values.values())
    plt.xlabel('Cell index')
    plt.ylabel('RSD of intensity')
    plt.title('Distribution of relative standard deviations of cell intensities')
    plt.show()


if __name__ == '__main__':
    fluorescent_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
    brightfield_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_brightfield.png' 

    cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img_path, fluorescent_img_path)
    cell_measurements = cell_metrics(fluorescent_img_path, cell_masks, cells_with_aggregates)



