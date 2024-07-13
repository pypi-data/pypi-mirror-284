# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 16:16:19 2023

@author: Ben Nicholson
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math



def get_symbols():
    """"
    Prints a list of commonly used symbols and which chr() value to use.
    """
    print('Greek letters:')
    for n in range(945,970):
        print(f'chr({n}) = {chr(n)}, chr({n-32}) = {chr(n-32)}')
    print('Additional Symbols:')
    print(r'\u212B = '+'\u212B')
    return None




def format_uncertainty(value, error):
    """
    Nicely format a value with its associated uncertainty, including rounding to 1 significant figure.

    Args:
        value (float): The value to format.
        error (float): The uncertainty/error associated with the value.

    Returns:
        str: A formatted string in the form "value ± error", e.g. "8.67 ± 0.03".
    """
    # Special case when the error is zero
    if error == 0:
        return f'{round(value, 0)} ± 0'
    
    order_of_magnitude = int(math.floor(math.log10(abs(error))))
    factor = 10 ** (-order_of_magnitude)
    rounded_error = round(error * factor) / factor
    precision = -order_of_magnitude 
    formatted_value = round(value, precision)
    
    if rounded_error.is_integer():
        # If the error is an integer, show no decimal places
        rounded_error = int(rounded_error)
        formatted_value = int(formatted_value)
    
    return f'{formatted_value} ± {rounded_error}'




class GenerateSampleDiagram():
    """
    Generates a sample diagram showing the layer structure for posters, reports, presentations etc.
    """
    def __init__(self):
        # Relative height for each layer
        self.layer_height = [3, 3, 1, 3, 1] 
        # The gap in between each layer
        self.layer_spacing = 0.15 
        # Horizontal width of the front face of each layer
        self.layer_width = 1.0 
        # Defines the height/width of the 3D portion on the right hand side
        self.projection_height = 1.55
        self.projection_width = 0.25
        
        # Self explanatory variables
        self.edge_colour = 'black'
        self.layer_colours = ['skyblue', 'darksalmon', 'palegreen', 'darksalmon', 'palegreen']
        self.layer_text = ['Silicon\nWafer', 'CoFeB(9nm)', 'Pt(3nm)', 'CoFeB(9nm)', 'Pt(3nm)']
        self.font_size = 24
        self.figsize = (4,7)
        self.dpi = 100


    def generate_sample(self):
        # Create a '3D' figure in a 2D graph
        self.fig = plt.figure(figsize=self.figsize, dpi=self.dpi)
        self.ax = self.fig.add_subplot(111)
        
        # Loop over each layer
        for n, height in enumerate(self.layer_height):
            # Calculate heights
            lower_y = np.sum(self.layer_height[:n])+n*self.layer_spacing
            upper_y = lower_y + self.layer_height[n]
        
            # Define the coordinates of the vertices of the box
            front_face_vertices = [(0.0, lower_y), 
                                   (self.layer_width, lower_y), 
                                   (self.layer_width, upper_y), 
                                   (0.0, upper_y)]
            
            right_face_vertices = [(self.layer_width, lower_y), 
                                   (self.layer_width+self.projection_width, lower_y+self.projection_height), 
                                   (self.layer_width+self.projection_width, upper_y+self.projection_height), 
                                   (self.layer_width, upper_y)]
            
            upper_face_vertices = [(0.0, upper_y), 
                                   (self.layer_width, upper_y), 
                                   (self.layer_width+self.projection_width, upper_y+self.projection_height), 
                                   (self.projection_width, upper_y+self.projection_height)]
            
            # Generate the face
            front_face_patch = patches.Polygon(front_face_vertices, closed=True, edgecolor=self.edge_colour, facecolor=self.layer_colours[n])
            right_face_patch = patches.Polygon(right_face_vertices, closed=True, edgecolor=self.edge_colour, facecolor=self.layer_colours[n])
            upper_face_patch = patches.Polygon(upper_face_vertices, closed=True, edgecolor=self.edge_colour, facecolor=self.layer_colours[n])
            
            # Add the face to the plot window
            self.ax.add_patch(front_face_patch)
            self.ax.add_patch(right_face_patch)
            self.ax.add_patch(upper_face_patch)
            
            # Add the layer label
            plt.text(0.5*self.layer_width, 
                     lower_y+0.5*self.layer_height[n], 
                     self.layer_text[n], 
                     horizontalalignment='center', 
                     verticalalignment='center', 
                     fontsize=self.font_size)
    
    
        self.ax.axis('off')
        plt.xlim(-0.01, self.layer_width+self.projection_width+0.01)
        plt.ylim(-0.01, upper_y+self.projection_height+0.01)
        plt.subplots_adjust(left=0.001, right=0.999, bottom=0.001, top=0.999)
        plt.show()
