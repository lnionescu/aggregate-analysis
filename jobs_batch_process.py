'''
batch_process.py: saves csv files of all cell metrics for image pair in a specified directory
'''
import os
import sys
from skimage.io import imread
from cells_with_foci import cells_with_foci
from concentration_analysis import cell_metrics

# Get directory from command line argument or use default
if len(sys.argv) > 1:
    image_dir = sys.argv[1]
else:
    image_dir = "/Users/nataliaionescu/Documents/PKM2/complete/splitting_test"

# Get all files in the directory
all_files = os.listdir(image_dir)

# Process each brightfield image and find its fluorescent pair
for filename in all_files:
    if '_brightfield.png' in filename:
        base_name = filename.replace('_brightfield.png', '')
        fluorescent_filename = f"{base_name}_fluorescent.png"
        
        if fluorescent_filename in all_files:
            brightfield_path = os.path.join(image_dir, filename)
            fluorescent_path = os.path.join(image_dir, fluorescent_filename)
            
            try:
                brightfield_img = imread(brightfield_path)
                fluorescent_img = imread(fluorescent_path)
                
                cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img, fluorescent_img)
                cell_metrics(fluorescent_path, cell_masks, cells_with_aggregates)
            except:
                pass
