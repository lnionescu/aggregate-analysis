import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import numpy as np
from aggregate_detector import detect_aggregates
from cellpose_runner import run_cellpose_segmentation
from cellpose import plot
from skimage import io

def cells_with_foci(brightfield_img, fluorescent_img):
    
    # get cell masks from brightfield image
    #print("Segmenting")
    cell_masks = run_cellpose_segmentation(brightfield_img)

    # detect aggregates in the fluorescent image
    #print("Detecting")
    fluorescent_img, tophat, aggregate_coords = detect_aggregates(fluorescent_img)

    # keep track of which cell IDs contain aggregates
    cells_with_aggregates = []

    # for each aggregate coordinate, check which cell mask it falls within
    for y,x in aggregate_coords:
        cell_id = cell_masks[y,x]
        if cell_id > 0:    # ie not background - this shouldn't happen anyway but just in case
            cells_with_aggregates.append(cell_id)

    #print(f"Found {len(cells_with_aggregates)} cells containing aggregates out of {len(np.unique(cell_masks)) - 1} total cells")


    return cells_with_aggregates, cell_masks, fluorescent_img


def visualize_results(cell_masks, cells_with_aggregates, fluorescent_img):
    # create mask for cells with aggregates
    agg_mask = np.isin(cell_masks, cells_with_aggregates)

    # show fluorescent image with this mask on top
    plt.figure()
    plt.imshow(fluorescent_img)
    plt.contour(agg_mask, colors='yellow', linewidths=1.5)
    plt.title(f"Cells with aggregates: {len(cells_with_aggregates)}")
    plt.axis("off")
    plt.show()
    return 0




if __name__ == "__main__":
    brightfield_path = '/Users/nataliaionescu/Documents/PKM2/complete/day3/E3Q_all_data/Series1_Z1_brightfield.png' 
    fluorescent_path = '/Users/nataliaionescu/Documents/PKM2/complete/day3/E3Q_all_data/Series1_Z1_fluorescent.png' 

    brightfield_img = io.imread(brightfield_path)
    fluorescent_img = io.imread(fluorescent_path)

    cells_with_aggregates, cell_masks, fluorescent_img = cells_with_foci(brightfield_img, fluorescent_img)
    visualize_results(cell_masks, cells_with_aggregates, fluorescent_img)

    random_cell_mask = cell_masks == 1
    # average over rgb channels to be consistent with concentration_analysis.py
    fluorescent_img_grayscale = np.mean(fluorescent_img[:, :, :3], axis=2)
    pixel_values = fluorescent_img_grayscale[random_cell_mask]
    # print(fluorescent_img_grayscale[random_cell_mask])
    plt.figure(figsize=(10,6))
    plt.hist(pixel_values.flatten(), bins=50, color='purple')
    plt.title('Pixel intensity distribution in a typical cell mask')
    plt.xlabel('Intensity')
    plt.ylabel('Frequency')
    plt.show()







