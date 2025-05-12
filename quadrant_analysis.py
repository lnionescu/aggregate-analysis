import numpy as np
from skimage.io import imread
import seaborn as sns
import matplotlib.pyplot as plt
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci 
import os

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
    quadrant_aggregate_counts = {'top_left': 0, 'top_right': 0, 'bottom_left': 0, 'bottom_right': 0}

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
                quadrant = 'top_left'
                break
            elif row < rows//2 and col >= columns//2:
                quadrant = 'top_right'
                break
            elif row >= rows//2 and col < columns//2:
                quadrant = 'bottom_left'
                break
            elif row >= rows//2 and col >= columns//2:
                quadrant = 'bottom_right'
                break
            
            # append metrics of current cell to the quadrant it resides in
            quadrant_metrics[quadrant].append(metrics)
            if metrics['has_aggregate']:
                quadrant_aggregate_counts[quadrant] += 1

    return quadrant_metrics, quadrant_aggregate_counts


def plot_metrics(quadrant_metrics, quadrant_aggregate_counts, save_path = 'testing_plots'):
    '''
    for testing: histogram for each metric with one bar for each quadrant
    '''
    os.makedirs(save_path, exist_ok = True)




    # get total_intensity/total_area across the cells in each quadrant
    quadrants_average_intensities = {}
    for quadrant, metrics_list in quadrant_metrics.items():
        total_intensity = sum([metrics['cell_total_intensity'] for metrics in metrics_list])
        total_area = sum([metrics['cell_area'] for metrics in metrics_list]) 
        if total_area > 0:       # avoid division by 0, if there is some empty quadrant
            quadrants_average_intensities[quadrant] = total_intensity / total_area
        else:
            quadrants_average_intensities[quadrant] = 0

     # compute average mean intensity across cells in each quadrant
    quadrants_average_mean_intensities = {}
    for quadrant, metrics_list in quadrant_metrics.items():
        total_mean_intensity = sum([metrics['cell_mean_intensity'] for metrics in metrics_list])
        cell_count = len(metrics_list)
        if cell_count > 0:      # avoid division by 0 if there is an empty quadrant
            quadrants_average_mean_intensities[quadrant] = total_mean_intensity / cell_count
        else:
            quadrants_average_mean_intensities[quadrant] = 0

    plt.bar(quadrants_average_intensities.keys(), quadrants_average_intensities.values(), color = ['blue', 'red', 'green', 'yellow'])
    plt.xlabel('Quadrants')
    plt.ylabel('Total intensity / total area')
    plt.title('Total cell intensity divided by total cell area for the cells in each quadrant')
    plt.savefig(os.path.join(save_path, 'mean_intensity.png'))


    plt.bar(quadrants_average_mean_intensities.keys(), quadrants_average_mean_intensities.values(), color = ['blue', 'red', 'green', 'yellow'])
    plt.xlabel('Quadrants')
    plt.ylabel('Average mean intensity')
    plt.title('Sum of mean intensities averaged by the number of cells')
    plt.savefig(os.path.join(save_path, 'avg_mean_intensity.png'))

    # plot distribution of mean cell intensities for all cells within a quadrant
    quadrant_names = ['top_left', 'top_right', 'bottom_left', 'bottom_right']
    plt.figure(figsize=(12,10))
    
    for index, quadrant in enumerate(quadrant_names, start=1):
        plt.subplot(2, 2, index)
        # get mean cell intensity for each cell in the quadrant
        mean_intensities = [metrics['cell_mean_intensity'] for metrics in metrics_list]
    
        plt.bar(range(len(mean_intensities)), mean_intensities)
        plt.xlabel('Cell index')
        plt.ylabel('Mean intensity')
        plt.title(f'Distribution of mean cell intensities in ({quadrant}) quadrant')

    plt.tight_layout()
    plt.savefig(os.path.join(save_path, 'mean_intensity_distribution.png'))

    # plot distribution of cell variances for all cells within a quadrant
    plt.figure(figsize=(12,10))
    for index, quadrant in enumerate(quadrant_names, start=1):
        plt.subplot(2, 2, index)
        variances = [metrics['cell_variance_intensity'] for metrics in quadrant_metrics[quadrant]]
        plt.bar(range(len(variances)), variances)
        plt.xlabel('Cell index')
        plt.ylabel('Variance of intensity')
        plt.title(f'Distribution of intensity variances in {quadrant} quadrant')

    plt.tight_layout()
    plt.savefig(os.path.join(save_path, 'variances_distribution.png'))

    
    # plot distribution of aggregate counts across quadrants
    plt.bar(quadrant_aggregate_counts.keys(), quadrant_aggregate_counts.values())
    plt.xlabel('Quadrants')
    plt.ylabel('Number of cells with aggregates')
    plt.title('Distribution of cells with foci across quadrants')




if __name__ == '__main__':
    fluorescent_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
    brightfield_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_brightfield.png' 
    quadrants = get_quadrants(fluorescent_img_path)
    quadrant_metrics, quadrant_aggregate_counts = get_quadrant_metrics(fluorescent_img_path, brightfield_img_path)
    #print(quadrant_metrics)
    plot_metrics(quadrant_metrics)











