import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nd2

'''
should be able to extract all necessary data from a .nd2 file: ie separate z-slices and channels
test this for one mutant before i get to the full automation script
'''

from quadrant_analysis import get_quadrants, get_quadrant_metrics
def get_time_evolution(nd2_file_path):
    '''
    input: path to nd2 file
    output: dictionary containing the time evolution of some metric for each quadrant
    '''
    # open the entire nd2 file
    with nd2.ND2File(nd2_file_path) as nd2_file:
        print(nd2_file.sizes)
        # dictionary with time evolution of chosen metric for each quadrant
        time_evolution = {'top_left': [], 'top_right': [], 'bottom_left': [], 'bottom_right': []}
  
  
if __name__ == '__main__':
    nd2_file_path = '/Users/nataliaionescu/Documents/PKM2/PKM2_E3Q_ChannelBrightfield,GFP_Seq0001.nd2' 
    get_time_evolution(nd2_file_path)



