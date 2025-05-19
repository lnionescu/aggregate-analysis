macro "Separate ND2 file dimensions" {
	// get input file
	input = File.openDialog("Select ND2 file to analyze");
	
	// get output directory
	output = getDirectory("Select Output Directory");
	
	// use bioformats
	run("Bio-Formats Macro Extensions");
	
	// initialize file
	Ext.setId(input);
	Ext.getSeriesCount(seriesCount);
	print("Series count: " + seriesCount);

	// loop through series
	for (s=0; s < seriesCount; s++){
		Ext.setSeries(s);
		Ext.getZSections(zSlices);
		Ext.getSizeC(channels);
		
		print("Processing series " + (s+1) + " with " + zSlices + " z-slices and " + channels + " channels");
		
		// import current series using bioformats
		run("Bio-Formats importer", "open=[" + input + "] autoscale color_mode=Default view=Hyperstack stack_order=XYCZT series_" + (s+1));
		
		// get image ID of the stack
		originalID = getImageID();
		originalTitle = getTitle();
		
		// split channels
		if (channels > 1){
			run("Split channels");
			}
			
		// process each channel
		for (c=1; c <= channels; c++){
			if (channels > 1){
				channelTitle = "C" + c + "-" + originalTitle;
				selectWindow(channelTitle);
				} else {
					selectWindow(originalTitle);
				}
				
			// process each z-slice
			if (zSlices > 1){
				for (z=1; z <= zSlices; z++){
					Stack.setSlice(z);
					
					// make duplicate of current slice
					run("Duplicate...", "title=temp");
					
					// save as png
					filename = output + "Series" + (s+1) + "_Channel" + c + "_Z" + z + ".png";
					saveAs("PNG", filename)
					close();
				}
			} else {
				// if there is just one z-slice
				filename = output + "Series" + (s+1) + "_Channel" + c + ".png";
				saveAs("PNG", filename);
			}
			
			// close channel window
			close();
			
			}
		}
		
		// close bioformats
		Ext.close();
		
		showMessage("Complete!");
}
