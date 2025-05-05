import numpy as np
from cells_with_foci import cells_with_foci

def cell_metrics(fluorescent_img, cell_masks, cells_with_aggregates):
    '''
    makes use of the cells_with_foci.py module to compute various aggregtion metrics for cells both with and without foci
    '''
    
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

        # cell without aggregate metrics

        #TODO continue and try on an example image


if __name__ == '__main__':
    brightfield_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_t0_brightfield.png" 
    fluorescent_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_t0_fluorescent.png"
    cells_with_aggregates, cell_masks = cells_with_foci(brightfield_path, fluorescent_path)
    cell_metrics(fluorescent_path, cell_masks, cells_with_aggregates)





