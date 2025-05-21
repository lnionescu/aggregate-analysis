# aggregate-analysis
Scripts to quantify degree of protein aggregation from fluorescence and brightfield microscopy pictures. The script aggregate\_detector.py identifies foci in fluorescence pictures using tophat filtering and running\_cellpose.py segments the cells in the corresponding brightfield picture using a calibrated cyto3 model. 
The parameters affecting the aggregate detection (structure element size, minimum peak distance, intensity threshold) and the cell segmentation (cell diameter) can be set by the user using the command line interface cli\_foci.py. 
Cell metrics (mean/variance/std of pixel intensities within the cell mask, both including and excluding the aggregate mask) are calculated with concentration\_analysis.py, which returns all these values in a csv file.


