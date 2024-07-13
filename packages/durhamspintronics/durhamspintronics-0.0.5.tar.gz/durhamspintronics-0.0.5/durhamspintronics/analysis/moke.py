# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 18:37:14 2024

@author: Ben Nicholson
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
import lmfit




def langevin_singlesweep(field, coercivity, shape):
    """
    Modified Langevin equation for fitting hysteresis loops, suggested by T.P. Hase.
    Example use case: https://journals.aps.org/prb/pdf/10.1103/PhysRevB.103.014440
    """
    return 1/(np.tanh((field + coercivity)/shape)) - 1/((field + coercivity)/shape)




def langevin_dualshape_singlesweep(field, coercivity, shape1, shape2, vertical_offset, vertical_scale, shape_width, background):
    """
    Calculates one up (or down) sweep of a hysteresis loop.
    For the full sweep , see the langevin_dualshape function.
    """
    # Create the smoothed shape array from an error function
    shape_arr = erf((field+coercivity)/shape_width)
    shape_arr *= (shape2-shape1)/2
    shape_arr += (shape2-shape1)/2 + shape1
    
    # Original function, now with the modifed shape array instead of a single value
    result = langevin_singlesweep(field, coercivity, shape_arr)
    #result = 1/(np.tanh((field + coercivity)/shape_arr)) - 1/((field + coercivity)/shape_arr)
    
    # Result isn't always between -1 and 1, so re-normalise the result
    result -= np.min(result)
    result /= np.max(result)*0.5
    result -= 1
    
    #Add any offset in the Kerr Voltage
    result = result*vertical_scale + vertical_offset
    return result + field*background




def langevin_dualshape(field, coercivity, shape1, shape2, vertical_offset, horizontal_offset, vertical_scale, shape_width, background):
    """
    Extends the basic langevin function to include two shape parameters in order to fit
    curves which are not symmetric immediately above/below the coercive field.
    """
    # Split the hysteresis loop into its up and down sweep
    # Currently assumes that the first half of the array is the up sweep, and the second half is the down sweep
    halfindex = int(len(field)/2)
    
    result_up = langevin_dualshape_singlesweep(field[:halfindex], 
                                  coercivity+horizontal_offset, 
                                  shape1, 
                                  shape2, 
                                  vertical_offset, 
                                  vertical_scale, 
                                  shape_width, 
                                  background)
    
    result_down = langevin_dualshape_singlesweep(field[halfindex:], 
                                    -coercivity+horizontal_offset,  # Coercivity is flipped, although h_offset is not
                                    shape2, # shape parameters are also flipped
                                    shape1, 
                                    vertical_offset, # Remaining parameters are the same sign for up/down sweeps
                                    vertical_scale, 
                                    shape_width, 
                                    background)
    
    return np.concatenate((result_up, result_down))




def fit_langevin_dualshape(field, kerr, plot=False):
	"""
 	Performs a quick lmfit of a lagenvin shaped hysteresis loop with two shape factors.
  	"""
    model = lmfit.Model(langevin_dualshape, independent_variables=['field'])
    
    params = model.make_params(coercivity = {'value':10.0, 'min':0.0, 'max':50.0, 'vary':True},
                               shape1 = {'value':0.5, 'min':0.001, 'max':5, 'vary':True},
                               shape2 = {'value':0.7, 'min':0.001, 'max':5, 'vary':True},
                               vertical_offset = {'value':0.01, 'min':-0.3, 'max':0.3, 'vary':True},
                               horizontal_offset = {'value':0.01, 'min':-10.0, 'max':10.0, 'vary':True},
                               vertical_scale = {'value':1.0, 'min':-0.001, 'max':1.4, 'vary':True},
                               shape_width = {'value':2.0, 'min':0.5, 'max':10.0, 'vary':True},
                               background = {'value':0.0, 'min':-0.5, 'max':0.5, 'vary':True},)

    result = model.fit(kerr, params, field=field)
    result.params.pretty_print()

	if plot:
	    # Generate a list to use for plotting
	    plot_result = [item.value for key, item in result.params.items()]
	
	    plt.figure(dpi=300)
	    plt.plot(data[:,0], data[:,1], color='black')
	    plt.plot(data[:,0], langevin_dualshape(data[:,0], *plot_result))
	    plt.xlabel('Field (Oe)')
	    plt.ylabel('Kerr Signal (arbitrary)')
	    plt.show()
    
    return result.params
