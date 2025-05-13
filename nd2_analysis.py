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

nd2_file_path = '/Users/nataliaionescu/Documents/PKM2/PKM2_WT_ChannelBrightfield,GFP_Seq0000.nd2' 

def process_nd2_file(nd2_file_path):
    with nd2.ND2File(nd2_file_path) as nd2_file:
        metadata = nd2_file.metadata
        dimensions = nd2_file.sizes
        print(dimensions)

process_nd2_file(nd2_file_path)






