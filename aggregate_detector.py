import matplotlib.pyplot as plt
import numpy as np
from skimage import feature, io, color, filters
from skimage.morphology import disk, white_tophat
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

'''
program to detect aggregates in the picture by their distincitve characteristics: small size and much brighter than surroundings
'''

# idea: top hat filter to identify small, compact bright spots
# top hat filteting an image isolates features that are brighter than their surroundings


def detect_aggregates(image_path, structure_element_size=7, min_distance=7, threshold=0.1):
    img = io.imread(image_path)
    gray = color.rgb2gray(img)


    # white top-hat
    str_element = disk(structure_element_size)
    tophat = white_tophat(gray, str_element)

    # local peaks in the top hat filtered image: exclude border because it gives edge artifacts
    coords = feature.peak_local_max(tophat, min_distance=min_distance, threshold_abs=threshold, exclude_border=True)

    return img, tophat, coords

def visualize_results(img, tophat, coords):
    fig, axes = plt.subplots(1, 2)

    axes[0].imshow(img)
    axes[0].set_title('Fluorescent image')
    axes[0].set_axis_off()

    axes[1].imshow(img)

    avg_radius=7
    for y, x in coords:
        circle=Circle((x,y), avg_radius, color='red', fill=False)
        axes[1].add_patch(circle)

    axes[1].set_title(f'Detected Protein Aggregates: {len(coords)} spots')
    axes[1].set_axis_off()

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # load an example fluorescent image
    image_path = "pngs_for_experimenting/log_fluorescent.png"

    img, tophat, coords = detect_aggregates(image_path)
    visualize_results(img, tophat, coords)
