import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci
import os
import csv
import pandas as pd



def batch_process_folder(folder_path):
    '''
    Process all CSV files ending with '_measurements.csv' in the specified folder
    Calculate RSD values and save results in the same folder with _rsd.csv suffix
    '''
    # Get all files in the directory
    all_files = os.listdir(folder_path)
    
    # Count of processed files
    processed_count = 0
    
    # Process each CSV file in the directory ending with _measurements.csv
    for filename in all_files:
        if filename.endswith('_measurements.csv'):
            print(f"Processing: {filename}")
            
            # Construct full path
            input_csv_path = os.path.join(folder_path, filename)
            
            try:
                # Get RSD values and save to CSV in the same directory
                rsd_values = get_distribution(input_csv_path)
                
                processed_count += 1
                print(f"  Success: {filename}")
            except Exception as e:
                print(f"  Error processing {filename}: {str(e)}")
    
    print(f"Processed {processed_count} measurement files")
    
    return processed_count 

def get_distribution(input_csv_file):
    # input: CSV file containing cell measurements (ending with measurements.csv)
    # computes the relative standard deviation (sd/mean) for the intensity of each cell
    # output: dictionary of cell RSDs and saves the values to a CSV file with _rsd.csv suffix in the same directory

    rsd_values = {}     # initialize dict for rsd values
    
    # Read cell measurements from CSV file
    df = pd.read_csv(input_csv_file)
    
    # Get the directory of the input file to save output in the same place
    output_dir = os.path.dirname(input_csv_file)
    
    # Create output filename based on the input filename, replacing 'measurements.csv' with 'rsd.csv'
    input_filename = os.path.basename(input_csv_file)
    base_filename = input_filename.replace('_measurements.csv', '')
    output_filename = f'{base_filename}_rsd.csv'
    output_file = os.path.join(output_dir, output_filename)

    # plot filename and saving
    plot_filename = f'{base_filename}_rsd_plot.png'
    plot_file = os.path.join(output_dir, plot_filename)

   
    # Extract cell measurements from the CSV
    for _, row in df.iterrows():
        cell_id = row['Cell ID']
        mean_intensity = row['cell_mean_intensity']
        sd_intensity = row['cell_sd_intensity']
        
        if mean_intensity > 0:
            rsd = sd_intensity / mean_intensity
            rsd_values[cell_id] = rsd
  
    plot_distribution(rsd_values, plot_file)
    

    # Save RSD values with the full path name of the file
    with open(output_file, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Cell Index', 'RSD', 'Source File'])   # table header
        for cell_id, rsd in rsd_values.items():
            writer.writerow([cell_id, rsd, input_csv_file])  # Include full path of input file

    return rsd_values


def plot_distribution(rsd_values, output_path):
    '''
    input: dictionary of rsd values of all cells in the image under analysis
    '''
    plt.figure()
    plt.bar(rsd_values.keys(), rsd_values.values())
    plt.xlabel('Cell index')
    plt.ylabel('RSD of intensity')
    plt.title('Distribution of relative standard deviations of cell intensities')
    
    if output_path:
        plt.savefig(output_path)

    


if __name__ == '__main__':
    data_folder = '/Users/nataliaionescu/Documents/PKM2/prelim/log'  # Update this path
    batch_process_folder(data_folder)

