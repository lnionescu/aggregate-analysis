macro "Separate series and z-project in two different ways"{
	// get input file
	input = File.openDialog("Select nd2 file");
	
	// extract protein name from filename
	filename = File.getName(input);
	if (indexOf(filename, "E3Q") >= 0) {
		proteinName = "E3Q";
	} else if (indexOf(filename, "Q10E") >= 0) {
		proteinName = "Q10E";
	} else if (indexOf(filename, "WT") >= 0) {
		proteinName = "WT";
	} else {
		proteinName = "Unknown";
	}
	
	print("Processing protein: " + proteinName);
	
	// select output directory
	output = getDirectory("Select output directory");
	
	// use bioformats to open like in GUI
	run("Bio-Formats Macro Extensions");
	
	// initialize file
	Ext.setId(input);
	Ext.getSeriesCount(seriesCount);
	print("Series count: " + seriesCount);
	
	// loop through series
	for (s=0; s < seriesCount; s++){
		Ext.setSeries(s);
		Ext.getSizeZ(zSlices);
		Ext.getSizeC(channels);
		
		print("Processing series " + (s+1) + " with " + zSlices + "z-slices and " + channels + " channels");
		
		// import current series using bioformats
		run("Bio-Formats Importer", "open=[" + input + "] autoscale color_mode=Default view=Hyperstack stack_order=XYCZT series_"+ (s+1));
		
		// get image ID and title
		originalID = getImageID();
		originalTitle = getTitle();
		
		// split channels
		if (channels > 1){
			run("Split Channels");
		}
		
		// process each channel
		for (c=1; c <= channels; c++){
			if (channels > 1){
				channelTitle = "C" + c + "-" + originalTitle;
				print("Looking for window: " + channelTitle);
				if (isOpen(channelTitle)) {
					selectWindow(channelTitle);
					print("Selected: " + channelTitle);
				} else {
					print("Window not found: " + channelTitle);
					continue;
				}
			} else {
				selectWindow(originalTitle);
			}
			
			// create z-projections 
			if (zSlices > 1){
				
				if (c == 1) {
					// Channel 1 = Brightfield
					
					// Max projection
					run("Z Project...", "projection=[Max Intensity]");
					
					// convert to 8-bit for proper PNG saving
					run("8-bit");
					
					filename = output + proteinName + "_Series" + (s+1) + "_Zmax_brightfield.png";
					saveAs("PNG", filename);
					close();
					
					// Sum projection
					selectWindow(channelTitle);
					run("Z Project...", "projection=[Sum Slices]");
					
					// convert to 8-bit
					run("8-bit");
					
					filename = output + proteinName + "_Series" + (s+1) + "_Zsum_brightfield.png";
					saveAs("PNG", filename);
					close();
					
				} else if (c == 2) {
					// Channel 2 = Fluorescent
					
					// Max projection
					run("Z Project...", "projection=[Max Intensity]");
					run("Green");
					filename = output + proteinName + "_Series" + (s+1) + "_Zmax_fluorescent.png";
					saveAs("PNG", filename);
					close();
					
					// Sum projection
					selectWindow(channelTitle);
					run("Z Project...", "projection=[Sum Slices]");
					run("Green");
					filename = output + proteinName + "_Series" + (s+1) + "_Zsum_fluorescent.png";
					saveAs("PNG", filename);
					close();
				}
				
			} else {
				// if there is just one z-slice, save as-is
				if (c == 1) {
					filename = output + proteinName + "_Series" + (s+1) + "_brightfield.png";
				} else {
					run("Green");
					filename = output + proteinName + "_Series" + (s+1) + "_fluorescent.png";
				}
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
