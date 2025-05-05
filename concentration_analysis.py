import numpy as np
from cells_with_foci import cells_with_foci
from skimage.io import imread

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
        # select the pixels from the cell masks that belong to the current cell, to perform measurements on
        cell_mask = cell_masks == cell_id
        print(cell_mask)
        
        # different metrics are important depending on whether the cell contains an aggregate or not
        has_aggregate = cell_id in cells_with_aggregates

        # cell area - number of pixels in the mask
        cell_area = np.sum(cell_mask)

        # mean and total intensity across cell - from fluorescent image pixel values
        cell_mean_intensity = np.mean(fluorescent_img[cell_mask])
        cell_total_intensity = cell_area * cell_mean_intensity

        cell_measurements[cell_id] = {'has_aggregate': has_aggregate, 'cell_area': cell_area, 'mean_intensity': cell_mean_intensity, 'total_intensity': cell_total_intensity}
        agg_count = sum(1 for cell_data in cell_measurements.values() if cell_data.get('has_aggregate') is True)
        print('Dictionary says that',agg_count, 'cells have aggregates')


        #TODO continue and try on an example image

    print(cell_measurements)
    return cell_measurements


if __name__ == '__main__':
    # compre mutant E3Q at the beginning and end
    brightfield_path = '/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_log_brightfield.png' 
    fluorescent_path = '/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_log_fluorescent.png' 
    # brightfield_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_t0_brightfield.png" 
    # fluorescent_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_t0_fluorescent.png"
    cells_with_aggregates, cell_masks = cells_with_foci(brightfield_path, fluorescent_path)
    cell_metrics(fluorescent_path, cell_masks, cells_with_aggregates)





