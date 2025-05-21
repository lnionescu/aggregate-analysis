'''
batch_process.py: saves csv files of all cell metrics for image pair in a specified directory
'''
import os
from skimage.io import imread
from cells_with_foci import cells_with_foci
from concentration_analysis import cell_metrics

# Directory containing your images
image_dir = "/Users/nataliaionescu/Documents/PKM2/complete/splitting_test" 
# Get all files in the directory
all_files = os.listdir(image_dir)

# Process each brightfield image and find its fluorescent pair
for filename in all_files:
    if '_brightfield.png' in filename:
        # Get the base name (E3Q_t1, Q10E_t2, etc.)
        base_name = filename.replace('_brightfield.png', '')
        
        # Construct the matching fluorescent filename
        fluorescent_filename = f"{base_name}_fluorescent.png"
        
        # Check if the fluorescent file exists
        if fluorescent_filename in all_files:
            print(f"Processing pair: {base_name}")
            
            # Construct full paths
            brightfield_path = os.path.join(image_dir, filename)
            fluorescent_path = os.path.join(image_dir, fluorescent_filename)
            
            try:
                # Load images
                brightfield_img = imread(brightfield_path)
                fluorescent_img = imread(fluorescent_path)
                
                # Process images using your existing functions
                cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img, fluorescent_img)
                cell_metrics(fluorescent_path, cell_masks, cells_with_aggregates)
                
                print(f"  Success: {base_name}")
            except Exception as e:
                print(f"  Error processing {base_name}: {str(e)}")
