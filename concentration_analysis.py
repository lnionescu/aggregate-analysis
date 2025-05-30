import numpy as np
from cells_with_foci import cells_with_foci
from skimage.io import imread
from aggregate_detector import detect_aggregates
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def cell_metrics(fluorescent_img_path, cell_masks, cells_with_aggregates, intensity_threshold=None, threshold_method='absolute'):
    '''
    makes use of the cells_with_foci.py module to compute various aggregtion metrics for cells both with and without foci
    Arguments: 
    fluorescent_img_path: path to fluorescent image (str)
    cell_masks: masks given by the cell segmentation, as in cellpose_runner.py (numpy array)
    cells_with_aggregates: list of cell IDs (corresponding to masks) that contain aggregates, as in cells_with_foci.py (list)
    intensity_threshold: intensity threshold for pixel inclusion in the calculations on the masks; if None, all pixels are included (float, optional)
    threshold_method: how to eliminate pixels by thresholding (str, 'absolute'/'percentile')
    '''
    
    # load fluorescent image as numpy array to be able to perform calculations on it
    fluorescent_img = imread(fluorescent_img_path)
    print(fluorescent_img.shape) 

    # get unique cells IDs and explicitly exclude the background
    unique_cells = np.unique(cell_masks)
    unique_cells = unique_cells[unique_cells > 0]

    # dictionary to store measurements for each cell id
    cell_measurements = {}

    # process the cells
    for cell_id in unique_cells:
    # for cell_id in range(1,2):
     
       # select the pixels from the cell masks that belong to the current cell, to perform measurements on
        cell_mask = cell_masks == cell_id

       # apply thresholding to refine the mask
       # to compare pixel values, average over the rgb channels of the fluorescent image
        avg_fluorescent = np.mean(fluorescent_img, axis=2)
        if intensity_threshold is not None:

            if threshold_method == 'absolute':
                threshold_value = intensity_threshold
            elif threshold_method == 'percentile':
                threshold_value = np.percentile(pixel_intensities, intensity_threshold)

            # discard pixels that are below the chosen threshold
            intensity_mask = avg_fluorescent >= threshold_value
            # get the refined cell mask by only including the pixels that satisfy both conditions: inside the mask of the cell under analysis and exceeding the threshold
            refined_cell_mask = cell_mask & intensity_mask

        else:
            refined_cell_mask = cell_mask
            threshold_value = None

       
        # identify whether the current cell is among cells_with_aggregates
        has_aggregate = cell_id in cells_with_aggregates

        # cell area - number of pixels in the mask
        cell_area = np.sum(refined_cell_mask)

        # mean and total intensity across cell - from fluorescent image pixel values
        cell_mean_intensity = np.mean(fluorescent_img[refined_cell_mask])
        cell_total_intensity = cell_area * cell_mean_intensity

        # variance and standard deviation of the intensity across the entire cell
        cell_variance_intensity = np.var(fluorescent_img[refined_cell_mask])
        cell_sd_intensity = np.std(fluorescent_img[refined_cell_mask])

        # for cells with foci: quantify the mean and total intensity of the aggregate
        if has_aggregate:
           _, _, aggregate_coords = detect_aggregates(fluorescent_img)

           # mask that contains the aggregate in the current cell
           aggregate_mask = np.zeros_like(cell_mask, dtype=bool)
           for y, x in aggregate_coords:
               if refined_cell_mask[y, x]:     # is the aggregate within the current cell?
                   aggregate_mask[y, x] = True

            # total and mean intensity of the foci
           aggregate_total_intensity = np.sum(fluorescent_img[aggregate_mask])
           aggregate_mean_intensity = np.mean(fluorescent_img[aggregate_mask])

           # mask out aggregates to get metrics about the rest of the cell, bitwise
           remaining_cell_mask = refined_cell_mask & ~aggregate_mask

           # for cells with foci, make it such that cell metrics exclude the aggregates
           rest_of_cell_mean_intensity = np.mean(fluorescent_img[remaining_cell_mask])
           rest_of_cell_total_intensity = np.sum(fluorescent_img[remaining_cell_mask])
           rest_of_cell_variance_intensity = np.var(fluorescent_img[remaining_cell_mask])
           rest_of_cell_sd_intensity = np.std(fluorescent_img[remaining_cell_mask])


           cell_measurements[cell_id] = {'has_aggregate': has_aggregate, 'cell_area': cell_area, 'cell_mean_intensity': cell_mean_intensity, 'cell_total_intensity': cell_total_intensity, 'cell_variance_intensity': cell_variance_intensity, 'cell_sd_intensity': cell_sd_intensity, 'aggregate_total_intensity': aggregate_total_intensity, 'aggregate_mean_intensity': aggregate_mean_intensity, 'rest_of_cell_mean_intensity': rest_of_cell_mean_intensity, 'rest_of_cell_total_intensity': rest_of_cell_total_intensity, 'rest_of_cell_variance_intensity': rest_of_cell_variance_intensity, 'rest_of_cell_sd_intensity': rest_of_cell_sd_intensity}

            
        # metrics to store for cells without foci
        if not has_aggregate:    
            cell_measurements[cell_id] = {'has_aggregate': has_aggregate, 'cell_area': cell_area, 'cell_mean_intensity': cell_mean_intensity, 'cell_total_intensity': cell_total_intensity, 'cell_variance_intensity': cell_variance_intensity, 'cell_sd_intensity': cell_sd_intensity}
        
        # agg_count = sum(1 for cell_data in cell_measurements.values() if cell_data.get('has_aggregate') is True)

        # print('Dictionary says that',agg_count, 'cells have aggregates')

    save_measurements_to_csv(fluorescent_img_path, cell_measurements)

    return cell_measurements

def save_measurements_to_csv(fluorescent_img_path, cell_measurements):
    '''
    saves the dictionary of cell measurements as a csv file
    '''
    # extract the base name of the fluorescent image file that's being processed: include this in the csv file name to not get things confused later
    base_name = os.path.splitext(os.path.basename(fluorescent_img_path))[0]

    # define/create an output directory
    input_dir = os.path.dirname(fluorescent_img_path)

    # define output file path
    output_file = os.path.join(input_dir, f'{base_name}_cell_measurements.csv')

    # convert dictionary to dataframe and save as csv
    df = pd.DataFrame.from_dict(cell_measurements, orient='index')
    df.to_csv(output_file, index_label='Cell ID')


if __name__ == '__main__':
   
    brightfield_path = '/Users/nataliaionescu/Documents/PKM2/thresholding/Series1_Z5_brightfield.png' 
    fluorescent_path = '/Users/nataliaionescu/Documents/PKM2/thresholding/Series1_Z5_fluorescent.png' 



    brightfield_img = imread(brightfield_path)
    fluorescent_img = imread(fluorescent_path)

    cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img, fluorescent_img)
    cell_metrics(fluorescent_path, cell_masks, cells_with_aggregates, intensity_threshold=5, threshold_method = 'absolute')




