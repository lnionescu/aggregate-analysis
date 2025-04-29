import cmd
import os
import numpy as np
import matplotlib.pyplot as plt
from cells_with_foci import cells_with_foci
from aggregate_detector import detect_aggregates
from cellpose_runner import run_cellpose_segmentation
from skimage import io

'''
this combines the three parts of the pipeline into one command-line interface where all the parameters that affect the end result (ie the detection of cells with foci) are set by the user
'''

class FociCLI(cmd.Cmd):
    '''
    note that all methods in this class have to start with do_ because that's what the cmd library wants
    '''
    prompt = '>>'
    intro = 'This is the protein aggregation analysis CLI. Type "help" for available commands.'

    def __init__(self):
        super().__init__()
        # all variables and parameters initialized here
        self.brightfield_path = None
        self.fluorescent_path = None
        self.output_dir = None
        self.cell_diameter = None
        self.structure_element_size = 7
        self.min_distance = 7
        self.threshold = 0.1

        # all results of the analysis 
        self.cell_masks = None
        self.cells_with_aggregates = None
        self.aggregate_coords = None
        self.fluorescent_img = None
        self.cell_measurements = None

    def do_set_brightfield(self, path):
        '''
        sets the path to the brightfield image
        '''
        self.brightfield_path = path
        print(f"Brightfield image set to: {self.brightfield_path}")

    def do_set_fluorescent(self, path):
        '''
        sets the path to the fluorescent image
        '''
        self.fluorescent_path = path
        print(f"Fluorescent image set to: {self.fluorescent_path}")

    def do_set_output(self, path):
        '''
        sets the output directory for the results
        '''
        self.output_dir = path
        print(f"Output directory set to: {self.output_dir}")

    def do_set_cell_diameter(self, line):
        '''
        sets the cell diameter used in the cellpose segmentation; if unknown, set to 0 to let cellpose calibrate internally and get the best results
        '''
        diameter = input("Enter the cell diameter, or 0 for auto-calibration: ")
        self.cell_diameter = None if diameter <=0 else diameter
        print(f"Cell diameter set to: {'auto-calibrated' if diameter <=0 else diameter}")

    def do_set_structure_element_size(self, line):
        # TODO explain how tweaking this parameter qualitatively changes the result
        
        '''
        sets the structure element size for the tophat filter used in aggregate detection
        '''
        size = input("Enter the structure element size for the tophat filter: ")
        self.structure_element_size = size
        print(f"Structure element size set to {size}")

    def do_set_min_distance(self, line):
        # TODO explain how tweaking this parameter qualitatively changes the result
        '''
        minimum distance between peaks, used in the aggregate detection 
        '''
        distance = input("Enter the minimum distance between bright spots for aggregate detection: ")
        self.min_distance = distance
        print(f"Minimum distance set to {distance}")

    def do_set_threshold(self, line):
        # TODO explain how tweaking this parameter qualitatively changes the result
        '''
        brightness threshold, used in the aggregate detection 
        '''
        threshold = input("Enter brightness threshold for aggregate detection: ")
        self.threshold = threshold
        print(f"Brightness threshold set to {threshold}")


    def do_segment_cells(self, line):
        # technically this is not necessary because the segmentation is already included in cells_with_foci
        '''
        segments cells in the brightfield image
        '''
        if not self.brightfield_path:
            print("Brightfield picture required, use that command first")
            return

        print("Segmenting cells...")
        self.cell_masks = run_cellpose_segmentation(self.brightfield_path, diameter=self.cell_diameter)
        number_of_cells = len(np.unique(self.cell_masks)) - 1  # exclude background
        print(f"Segmented {number_of_cells} cells")

        
    def do_cells_with_foci(self, line):
        '''
        finds cells containing protein aggregates
        '''
        if not self.brightfield_path or not self.fluorescent_path:
            print("Brightfield and fluorescent pictures required, use those commands first")
            return

        print("Finding cells with foci...")

        self.cells_with_aggregates, self.cell_masks = cells_with_foci(self.brightfield_path, self.fluorescent_path, cell_diameter=self.cell_diameter, structure_element_size=self.structure_element_size, min_distance=self.min_distance, threshold=self.threshold)






    def do_quit(self, line):
        '''
        exits the program
        '''
        return True







if __name__ == '__main__':
    FociCLI().cmdloop()









