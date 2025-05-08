import numpy as np
from skimage.io import imread
import seaborn as sns
import matplotlib.pyplot as plt

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

    return quadrants
    pass

def get_metrics(quadrants):
    '''
    input: numpy arrays corresponding to the four quadrnts of the image under analysis
    purpose: using concentration_analysis (which already does all the segmentation and aggregate detection and whatever), extract the mean cell intensity and the
    cell variance (including foci)
    output: average of metrics within each quadrant???
    '''

    return summary
    pass

def plot_metrics(summary):
    '''
    i guess a histogram for each metric with one bar for each quadrant
    '''

    pass

if __name__ == '__main__':
    fluorescent_img_path = '/Users/nataliaionescu/Documents/PKM2 aggregation/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
    quadrants = get_quadrants(fluorescent_img_path)
    summary = get_metrics(quadrants)
    plot_metrics(summary)





