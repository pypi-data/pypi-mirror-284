# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:28:45 2023

@author: Ben Nicholson
"""

from durhamspintronics.instruments.kepco import BOP
from durhamspintronics.instruments.rohdeandschwarz import ZNLE18_VNA
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

kepco_resource = 'GPIB0::6::INSTR'
vna_resource = 'GPIB0::20::INSTR'

# Initialise instruments
kepco = BOP(com_port=kepco_resource)
kepco.open_connection()
kepco.set_mode_constant_current()
kepco.output_on()

vna = ZNLE18_VNA(com_port=vna_resource)
vna.open_connection()
vna.reset()

# Magnet setpoints
background_voltage = -50
background_current = -5
magnet_currents = np.linspace(-5, 5, 121)

# Set up the VNA parameters
vna.mode = 'frequency sweep'
vna.power = 0 # dBm
vna.start_frequency = 2 # GHz
vna.stop_frequency = 18 # GHz
vna.sweep_time = 0.1 # seconds
vna.sweep_points = 161 #
vna.sweep_averages = 100 #
path = "C:\\Users\\Administrator\\Desktop\\Durham FMR Files\\FMR Data\\Jay\\2024\\KunleAFMSample_2-18GHz_pm5A-0deg_0.1s100avg"

# Set the magnet
kepco.voltage = background_voltage
kepco.current = background_current

# Run the frequency sweep to get the background
frequencies, background_s21 = vna.run_frequency_sweep()
np.savetxt(f'{path}/I=-20.txt', background_s21)

# Initialise the 2D arrays to plot frequency vs. magnet current
arr = np.zeros((len(background_s21), len(magnet_currents)))
arr_n = np.zeros((len(background_s21), len(magnet_currents)))

# Sweep over each desired current
for n, current in enumerate(magnet_currents):
    print(f'Starting measurement {n+1} of {len(magnet_currents)}.')
    # Set magnet
    if current < 0:
        kepco.voltage = -50
    else:
        kepco.voltage = 50
    kepco.current = current
    sleep(3) # wait for magnet to settle before starting frequency sweep (number not optimised)
    
    # Take measurement
    frequencies, s21 = vna.run_frequency_sweep()
    result = s21 - background_s21
    
    # Normalise the data so that each column is between -1 and 0 (sometimes improves the colour scheme)
    arr[:,n] = result
    result -= np.max(result)
    result /= np.min(result)
    result *= -1
    arr_n[:,n] = result
    
    np.savetxt(f'{path}/I={current:.4f}.txt', s21)

# Turn everything off
kepco.current = 0
kepco.voltge = 0
kepco.output_off()
vna.power = -10


plt.figure()
plt.title('Data - Background')
plt.imshow(arr, 
           aspect = (np.max(magnet_currents)-np.min(magnet_currents))/(vna.stop_frequency-vna.start_frequency),
           origin='lower', 
           extent=[np.min(magnet_currents), np.max(magnet_currents), vna.start_frequency, vna.stop_frequency])
plt.colorbar(label='S21 Difference (dB)')
plt.ylabel('Frequency (GHz)')
plt.xlabel('Magnet Current (A)')

plt.figure()
plt.title('Normalised color scheme')
plt.imshow(arr_n, 
           aspect = (np.max(magnet_currents)-np.min(magnet_currents))/(vna.stop_frequency-vna.start_frequency),
           origin='lower', 
           extent=[np.min(magnet_currents), np.max(magnet_currents), vna.start_frequency, vna.stop_frequency])
plt.colorbar(label='Normalised S21 (arbitrary units)')
plt.ylabel('Frequency (GHz)')
plt.xlabel('Magnet Current (A)')
plt.show()


vna.close_connection()
kepco.close_connection()
