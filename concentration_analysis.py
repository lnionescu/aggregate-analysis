import numpy as np
from cells_with_foci import cells_with_foci
from skimage.io import imread
from aggregate_detector import detect_aggregates
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def cell_metrics(fluorescent_img_path, cell_masks, cells_with_aggregates):
    '''
    makes use of the cells_with_foci.py module to compute various aggregtion metrics for cells both with and without foci
    '''
    
    # load fluorescent image as numpy arrat to be able to perform calculations on it
    fluorescent_img = imread(fluorescent_img_path)

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
       
        # identify whether the current cell is among cells_with_aggregates
        has_aggregate = cell_id in cells_with_aggregates

        # cell area - number of pixels in the mask
        cell_area = np.sum(cell_mask)

        # mean and total intensity across cell - from fluorescent image pixel values
        cell_mean_intensity = np.mean(fluorescent_img[cell_mask])
        cell_total_intensity = cell_area * cell_mean_intensity

        # variance and standard deviation of the intensity across the entire cell
        cell_variance_intensity = np.var(fluorescent_img[cell_mask])
        cell_sd_intensity = np.std(fluorescent_img[cell_mask])

        # for cells with foci: quantify the mean and total intensity of the aggregate
        if has_aggregate:
           _, _, aggregate_coords = detect_aggregates(fluorescent_img_path)

           # mask that contains the aggregate in the current cell
           aggregate_mask = np.zeros_like(cell_mask, dtype=bool)
           for y, x in aggregate_coords:
               if cell_mask[y, x]:     # is the aggregate within the current cell?
                   aggregate_mask[y, x] = True

            # total and mean intensity of the foci
           aggregate_total_intensity = np.sum(fluorescent_img[aggregate_mask])
           aggregate_mean_intensity = np.mean(fluorescent_img[aggregate_mask])

           # mask out aggregates to get metrics about the rest of the cell, bitwise
           remaining_cell_mask = cell_mask & ~aggregate_mask

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

    if __name__ == '__main__':
        print(cell_measurements)
    
    return cell_measurements



if __name__ == '__main__':
    # compre mutant E3Q at the beginning and end
    brightfield_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_brightfield.png' 
    fluorescent_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
    cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_path, fluorescent_path)
    cell_metrics(fluorescent_path, cell_masks, cells_with_aggregates)
    #visualize_metrics(fluorescent_path)




