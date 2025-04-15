# aggregate-analysis
Scripts to quantify degree of protein aggregation from fluorescence and brightfield microscopy pictures. The script aggregate\_detector.py identifies foci in fluorescence pictures using tophat filtering and running\_cellpose.py segments the cells in the corresponding brightfield picture using a calibrated cyto3 model. Then aggregation\_statistics.py computes various statistics for the protein aggregation inside cells with foci. 
really a WIP
