import numpy as np
import os
import csv
import nd2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from concentration_analysis import cell_metrics, save_measurements_to_csv
from cells_with_foci import cells_with_foci, visualize_results

'''
NOT WORKING !!!!!! IGNORE

'''

# start by understanding the dimensions of the nd2 files and how to extract what i need to apply previous methods

def separate_channels(nd2_file_path, output_dir='./output'):
    os.makedirs(output_dir, exist_ok=True)

    with nd2.ND2File(nd2_file_path) as nd2_file:

        brightfield_img = nd2_file.asarray()[0, 0, 0, :, :]   # [series, z, channel, y, x]
        fluorescent_img = nd2_file.asarray()[0, 0, 1, :, :]   # [series, z, channel, y, x]
        print(fluorescent_img.shape)



    return brightfield_img, fluorescent_img

if __name__ == '__main__':
    nd2_file_path = '/Users/nataliaionescu/Documents/PKM2/PKM2_E3Q_ChannelBrightfield,GFP_Seq0001.nd2' 
    brightfield_img, fluorescent_img = separate_channels(nd2_file_path)
    cells_with_aggregates, cell_masks, _ = cells_with_foci(brightfield_img, fluorescent_img) 
    visualize_results(cell_masks, cells_with_aggregates, fluorescent_img)




