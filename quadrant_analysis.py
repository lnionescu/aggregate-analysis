import numpy as np
from skimage.io import imread
import seaborn as sns
import matplotlib.pyplot as plt
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci 

'''
splits the image in four quadrants to quantify the spatial variation of the degree of protein aggregation
as first metrics, use mean cell intensity and cell variance intensity (calculated the same for all cells)
this is applied to the fluorescent image
'''

def get_quadrants(fluorescent_img_path):    
    '''
    input: path to fluorescent image
    output: numpy arrays corresponding to the four quadrants of the image
    '''

    fluorescent_img = imread(fluorescent_img_path)  
    print(fluorescent_img.shape)
    rows, columns, _ = fluorescent_img.shape
    
    # extract the four quadrants
    top_left = fluorescent_img[:rows//2, :columns//2]
    top_right = fluorescent_img[:rows//2, columns//2:]
    bottom_left = fluorescent_img[rows//2:, :columns//2]
    bottom_right = fluorescent_img[:rows//2, columns//2:]

    quadrants = {'top_left': top_left, 'top_right': top_right, 'bottom_left': bottom_left, 'bottom_right': bottom_right}

    return rows, columns, quadrants

def get_quadrant_metrics(fluorescent_img_path, brightfield_img_path):
    '''
    input: numpy arrays corresponding to the four quadrnts of the image under analysis
    purpose: using concentration_analysis (which already does all the segmentation and aggregate detection and whatever), extract the mean cell intensity and the
    cell variance (including foci)
    gets all metrics for the entire image and then assigns cells to quadrants based on the coordinates of their masks
    output: average of metrics within each quadrant???
    '''

    # use concentration_analysis.py to get all metrics for all cells in the image (can be changed later to only extract mean and variance, in case this is too slow)
    cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img_path, fluorescent_img_path)
    all_metrics = cell_metrics(fluorescent_img_path, cell_masks, cells_with_aggregates)
    
    # extract image dimensions
    fluorescent_img = imread(fluorescent_img_path)
    rows, columns, _ = fluorescent_img.shape

    # initialize dictionary for cell metrics separated by quadrant
    quadrant_metrics = {'top_left': [], 'top_right': [], 'bottom_left': [], 'bottom_right': []}

    # assign cells to quadrants based on the coordinates of the cell masks
    for cell_id, metrics in all_metrics.items():
        # get mask for current cell
        cell_mask = cell_masks == cell_id
        # get coordinates as the coordinates of the cell_mask matrix where cell_id is True (corresponds to coordinates of pixels belonging to the current cell)
        cell_coords = np.argwhere(cell_mask)
       
        # check if current cell belongs to each quadrant
        for coord in cell_coords:     # assign cells to a unique quadrant; if some cell happens to span multiple quadrants, just don't get the metrics for it because we can live without
            row, col = coord
            if row < rows//2 and col < columns//2:
                quadrant_metrics['top_left'].append(metrics)
                break
            elif row < rows//2 and col >= columns//2:
                quadrant_metrics['top_right'].append(metrics)
                break
            elif row >= rows//2 and col < columns//2:
                quadrant_metrics['bottom_left'].append(metrics)
                break
            elif row >= rows//2 and col >= columns//2:
                quadrant_metrics['bottom_right'].append(metrics)
                break
    
    return quadrant_metrics


def plot_metrics(quadrant_metrics):
    '''
    for testing: histogram for each metric with one bar for each quadrant
    '''
    # get total_intensity/total_area across the cells in each quadrant
    quadrants_average_intensities = {}
    for quadrant, metrics_list in quadrant_metrics.items():
        cell_intensities = [metrics['cell_total_intensity'] for metrics in metrics_list]
        cell_areas = [metrics['cell_area'] for metrics in metrics_list]
           

    






    pass

if __name__ == '__main__':
    fluorescent_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
    brightfield_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_brightfield.png' 
    quadrants = get_quadrants(fluorescent_img_path)
    quadrant_metrics = get_quadrant_metrics(fluorescent_img_path, brightfield_img_path)
    print(quadrant_metrics)
    #plot_metrics(summary)





