import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

'''
Input: csv files of the cell measurements for each mutant on the desired day
Output: bar plot showing the fractions of cells with foci for each mutant
'''

def calculate_foci_fraction(csv_path):
    '''
    calculates fraction of cells containing foci from the cell measurements csv file
    returns: cells_with_foci / total_cells fraction
    '''
    # read csv of cell measurements and get each number of cells
    df = pd.read_csv(csv_path)
    total_cells = len(df)
    cells_with_foci = df['has_aggregate'].sum()
    fraction = cells_with_foci / total_cells if total_cells > 0 else 0
    return fraction

# file paths for the cell measurements of each mutant (change depending on day)
file_paths = [']
