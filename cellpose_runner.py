'''
script to run the cyto3 cellpose model and get cell masks for brightfield images directly from the terminal; the goal is simply to reproduce the results of calibrated cyto3 applied from inside the cellpose GUI, but it's better to write a module for automation purposes
'''
from cellpose import models, io
import numpy as np
import matplotlib.pyplot as plt
from cellpose import plot
from skimage import exposure
def calibrate_size(image, channels=[0, 0]):
    """
    Function to estimate cell diameter using the cyto3 model.
    
    Parameters:
        image (numpy.ndarray): The input image (grayscale or RGB).
        channels (list): The channels to use for segmentation (default: [0, 0] for grayscale).
        
    Returns:
        float: Estimated cell diameter in pixels.
    """
    # Initialize the cellpose model with the "cyto3" model
    model = models.Cellpose(gpu=False, model_type="cyto3")
    
    # Run the model to estimate diameters
    diameters, _ = model.sz.eval(image, channels=channels)

    # Ensure a minimum diameter of 5.0 pixels
    estimated_diameter = max(5.0, diameters)
    print(f"Estimated cell diameter: {estimated_diameter} pixels")
    
    return estimated_diameter

def run_cellpose_segmentation(image_path, diameter=None):
    '''
    run cellpose on a single image using the cyto3 model; gives same result as cellpose GUI with calibration
    inputs: image_path, diameter (if None it is estimated on a per image basis) 
    outputs: numpy array masks (each cell has an integer ID)
    '''
    # load image
    img = io.imread(image_path)

    # note that the GUI automatically preprocesses images, which is pretty problematic for me but TODO find exactly what it does and imitate
    # TODO on second thought, this might be done automatically in model.eval or something, and might not even be so important (check/justify if true)
    # what is really important though is getting the calibration to work TODO !!!
    # img = exposure.rescale_intensity(img)   # check if toggling on/off even makes a difference

    estimated_diameter = calibrate_size(img)

    # create model
    model = models.CellposeModel(gpu=False, model_type='cyto3')
    channels = [0,0]

    # run segmentation
    print("Running segmentation...")
    masks, flows, styles = model.eval(img, diameter=diameter, channels=channels)
   

    estimated_diameter = model.diam_labels.item()
    print("Used diameter", estimated_diameter)

    # note on "masks": cellpose makes this into a numpy array with the same dimensions as the image, where each component (corresponding to each pixel) is an integer that gives the cell number the pixel is in

    # plot masks to make sure they're the same for an example picture as from the GUI
    fig = plt.figure()
    plot.show_segmentation(fig, img, masks, flows[0], channels=channels)
    plt.tight_layout()
    plt.show()


    return masks

# test with some brightfield image
if __name__ == '__main__':
    image_path = "/Users/nataliaionescu/Documents/project/pngs_for_experimenting/Q10E_log_brightfield.png" 
    run_cellpose_segmentation(image_path)



