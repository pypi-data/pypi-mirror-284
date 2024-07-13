# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:34:27 2023

@author: Ben Nicholson
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib_scalebar.scalebar import ScaleBar
import cv2




def add_scale_bar(filename, 
                  lens=None, 
                  border_pad=0.5, 
                  location='lower left',
                  fontsize=48,
                  scale_bar_width=0.02,
                  scale_bar_length=0.5,
                  ):
    """
    For use with photos taken using the ThorLabs camera on the microscope in Ph58. 
    
    Any other setup will have different calibration values!
    """

    if lens not in ["plan5", "plan10", "plan40"]:
        print('To add the correct scale bar, you need to know which lens you used.')
        print('The microscope has three lenses, "plan5", "plan10", "plan40".')
        return 0
    else:
        # Load image
        im = Image.open(filename)
        imarray = np.array(im)
        
        # Start figure
        plt.figure(figsize=(imarray.shape[1]/100, imarray.shape[0]/100), dpi=75, frameon=False)
        ax = plt.subplot(111)
        ax.set_axis_off()
        plt.imshow(imarray)
        
        # Depending on the lens used, add a scale bar of the correct size
        if lens == 'plan5':
            calibration = 1/634 # Calibrated by Ben Nicholson, 2023
            units = 'mm'
        elif lens == 'plan10':
            calibration = 109/138 # Calibrated by Ben Nicholson, 2023
            units = 'um'
        elif lens == 'plan40':
            calibration = 160/810 # Calibrated by Ben Nicholson, 2023
            units = 'um'
            
        scalebar = ScaleBar(calibration,
                            units, 
                            border_pad=border_pad, 
                            length_fraction=scale_bar_length, 
                            width_fraction=scale_bar_width, 
                            font_properties={'size':fontsize}, 
                            box_alpha=0, 
                            label_loc='top', 
                            location=location)
            
        ax.add_artist(scalebar)
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        output_fname = filename.split('.')[0]+'_WithScaleBar.png'
        plt.savefig(output_fname, dpi=150)
        plt.show()




def reduce_saturation(filename, factor=0.5):
	"""
	Reduces the image saturation, which makes it easier to view on some projectors/screens.
	"""
	# Load image
	img = cv2.imread(filename)
	
	# Convert from BGR to HSV
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	
	# Reduce the saturation
	hsv_img[:, :, 1] = np.clip(hsv_img[:, :, 1] * factor, 0, 255)
	
	# Convert back from HSV to BGR
	output_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
	
	cv2.imwrite(image_path.split('.')[0]+'_Desaturated.png', output_img)
	return output_img
