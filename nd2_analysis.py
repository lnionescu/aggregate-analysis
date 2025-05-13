import numpy as np
import os
import csv
import nd2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from concentration_analysis import cell_metrics, save_measurements_to_csv

'''
this doesn't have any extra functions, it is simply meant to process nd2 files and save the measurements of their cells as a csv file
'''

# start by understanding the dimensions of the nd2 files and how to extract what i need to apply previous methods

def separate_channels(nd2_file_path, output_dir='./output'):
    os.makedirs(output_dir, exist_ok=True)

    with nd2.ND2File(nd2_file_path) as nd2_file:

        brightfield_img = nd2_file.asarray()[0, 0, 0]   # [series, z, channel, y, x]
        fluorescent_img = nd2_file.asarray()[0, 0, 1]   # [series, z, channel, y, x]

        brightfield_path = os.path.join(output_dir, 'brightfield.png')
        fluorescent_path = os.path.join(output_dir, 'fluorescent.png')

        plt.imsave(brightfield_path, brightfield_img, cmap='gray')
        plt.imsave(fluorescent_path, fluorescent_img, cmap='gray')

if __name__ == '__main__':
    nd2_file_path = '/Users/nataliaionescu/Documents/PKM2/PKM2_E3Q_ChannelBrightfield,GFP_Seq0001.nd2' 
    separate_channels(nd2_file_path)






