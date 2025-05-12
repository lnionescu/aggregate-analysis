import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from concentration_analysis import cell_metrics
from cells_with_foci import cells_with_foci
''' 
uses dictionary of cell metrics to get the distribution of relative standard deviation of cell intensities
'''


fluorescent_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_fluorescent.png' 
brightfield_img_path = '/Users/nataliaionescu/Documents/PKM2/pngs_for_experimenting/E3Q_t0_brightfield.png' 

cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img_path, fluorescent_img_path)
cell_measurements = cell_metrics(fluorescent_img_path, cell_masks, cells_with_aggregates)




