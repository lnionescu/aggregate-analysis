import numpy as np
from skimage.io import imread

'''
splits the image in four quadrants to quantify the spatial variation of the degree of protein aggregation
as first metrics, use mean cell intensity and cell variance intensity (calculated the same for all cells)
this is applied to the fluorescent image
'''

def get_quadrants(fluorescent_img_path):
    
    fluorescent_img = imread(fluorescent_img_path)

    return quadrants
    pass

def get_metrics(quadrants):

    return summary
    pass

def plot_metrics(summary):

    pass

if __name__ == '__main__':
    fluorescent_img_path = '/Users/nataliaionescu/Documents/PKM2 aggregation/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
    quadrants = get_quadrants(fluorescent_img_path)
    summary = get_metrics(quadrants)
    plot_metrics(summary)





