import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci
import os
import csv

''' 
uses dictionary of cell metrics to get the distribution of relative standard deviation of cell intensities
'''

def get_distribution(cell_measurements, output_folder):
    '''
    input: dictionary of cell measurements obtained using cell_metrics
    computes the relative standard deviation (sd/mean) for the intensity of each cell
    output: dictionary of cell RSDs
    '''

    # TODO modify this function such that it takes a csv file as argument
    # TODO save csv of RSD values with the full path name of the file

    rsd_values = {}     # initialize dict for rsd values
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, 'rsd_values.csv')

    # get mean and standard deviation of intensity within each cell
    for cell_id, metrics in cell_measurements.items():
        mean_intensity = metrics.get('cell_mean_intensity')
        sd_intensity = metrics.get('cell_sd_intensity')
        if mean_intensity > 0:
            rsd = sd_intensity / mean_intensity
            rsd_values[cell_id] = rsd
    
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Cell Index', 'RSD'])   # table header
        for cell_id, rsd in rsd_values.items():
            writer.writerow([cell_id, rsd])


    return rsd_values



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
    output_folder = 'rsd_results'
    rsd_values = get_distribution(cell_measurements, output_folder)
    plot_distribution(rsd_values)



