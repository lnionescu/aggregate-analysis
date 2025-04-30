# aggregate-analysis
Scripts to quantify degree of protein aggregation from fluorescence and brightfield microscopy pictures. The script aggregate\_detector.py identifies foci in fluorescence pictures using tophat filtering and running\_cellpose.py segments the cells in the corresponding brightfield picture using a calibrated cyto3 model. 
The parameters affecting the aggregate detection (structure element size, minimum peak distance, intensity threshold) and the cell segmentation (cell diameter) can be set by the user using the command line interface cli\_foci.py. 
Metrics about the cells (concentration of solved protein, or degree of aggregation if that is the case) are computed using concentration\_analysis.py (in progress).
Coming up later: statistics of protein aggregation throughout the picture by either splitting it into quadrants or by randomly sampling subsets of cells.
Also coming up later: full automation script for all the mutants of PKM2 and all the timestamps they were analyzed.  


