'''
Script to run the cyto3 cellpose model and get cell masks for brightfield images directly from the terminal. The goal is simply to reproduce the results of calibrated cyto3 applied via the cellpose GUI. This is written for automation purposes.
'''
   
from cellpose import models, io, plot
import numpy as np
import matplotlib.pyplot as plt

def calibrate_size(image, channels=[0, 0]):
    # initialize cyto3 model
    model = models.Cellpose(gpu=False, model_type="cyto3")
    
    # run the model to estimate diameters
    diameters, _ = model.sz.eval(image, channels=channels)

    # ensure a minimum diameter of 5.0 pixels
    estimated_diameter = max(5.0, diameters)
    print(f"Estimated cell diameter: {estimated_diameter} pixels")
    
    return estimated_diameter

def run_cellpose_segmentation(image_path, diameter=None):
    '''
    Run cellpose on a single image using the cyto3 model. Produces the same result as the cellpose GUI with calibration
    outputs: numpy array masks (each cell has an integer ID)
    '''

    # load image
    image = io.imread(image_path)

    if diameter is None:
        diameter = calibrate_size(image)

    # create model
    model = models.CellposeModel(gpu=False, model_type='cyto3')
    channels = [0,0]

    # run segmentation
    print("Running segmentation...")
    masks, flows, styles = model.eval(image, diameter=diameter, channels=channels)
   
    print("Used diameter", diameter)

    if __name__ == '__main__':
        # plot masks to make sure they're the same for an example picture as from the GUI
        fig = plt.figure()
        plot.show_segmentation(fig, image, masks, flows[0], channels=channels)
        plt.tight_layout()
        plt.show()

    return masks

# test with some brightfield image
if __name__ == '__main__':
    image_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_brightfield.png' 
    run_cellpose_segmentation(image_path)



