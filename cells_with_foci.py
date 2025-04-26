import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection
import numpy as np
from aggregate_detector import detect_aggregates
from cellpose_runner import run_cellpose_segmentation
from cellpose import plot


def cells_with_foci(brightfield_path, fluorescent_path):
    
    # get cell masks from brightfield image
    print("Segmenting")
    cell_masks = run_cellpose_segmentation(brightfield_path)

    # detect aggregates in the fluorescent image
    print("Detecting")
    fluorescent_img, tophat, aggregate_coords = detect_aggregates(fluorescent_path)

    # keep track of which cell IDs contain aggregates
    cells_with_aggregates = []

    # for each aggregate coordinate, check which cell mask it falls within
    for y,x in aggregate_coords:
        cell_id = cell_masks[y,x]
        if cell_id > 0:    # ie not background - this shouldn't happen anyway but just in case
            cells_with_aggregates.append(cell_id)

    print(f"Found {len(cells_with_aggregates)} cells containing aggregates out of {len(np.unique(cell_masks)) - 1} total cells")

    # visualize
    visualize_results(cell_masks, cells_with_aggregates, fluorescent_img)

    return cells_with_aggregates, cell_masks


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
    # brightfield_path = '/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_log_brightfield.png' 
    # fluorescent_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/enhanced_E3Q_log_fluorescent.png" 
    # fluorescent_path = '/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_log_fluorescent.png' 
    brightfield_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_t0_brightfield.png" 
    fluorescent_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/E3Q_t0_fluorescent.png" 


    cells_with_aggregates, cell_masks = cells_with_foci(brightfield_path, fluorescent_path)











