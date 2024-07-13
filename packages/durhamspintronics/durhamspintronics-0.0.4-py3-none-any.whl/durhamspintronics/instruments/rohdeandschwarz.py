# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:01:53 2023

@author: Ben Nicholson
"""

import pyvisa as visa
import numpy as np

class ZNLE18_VNA():
	"""
 	Rohde and Schwarz Vector Network Analyser.
  """
    def __init__(self, com_port):
        self._com_port = com_port
        self._vna = None
        
        self._power = None # [dBm] Output power
        self._start_frequency = None # [GHz] Starting frequency of the frequency sweep
        self._stop_frequency = None # [GHz] Stopping frequency of the frequency sweep
        self._sweep_time = None # [seconds] Total time to sweep from start to stop frequency
        self._sweep_points = None # Number of data points between start and stop frequencies
        self._sweep_averages = None # Number of sweeps to average
        self._mode = None # Either 'frequency sweep' or 'field sweep' mode. Only frequency sweep is implemented at present.
        
        self.post_sweep_delay_time = 3 # [seconds] Time to wait after the sweep before querying the data
        
    def open_connection(self):
        self._vna = visa.ResourceManager().open_resource(self._com_port, write_termination = '\n', read_termination='\n')

            
    def close_connection(self):
        if self._vna:
            self._vna.close()
            print(r'VNA connection closed')
            
    def get_idn(self):
        message = self._vna.query(r'*IDN?')
        return message
    
    def reset(self):
        self._vna.write("*RST")
        self._vna.write(r'FORM:DATA ASCII') # Set the output data format to ASCII
        self._vna.write(r'SYST:DISP:UPD ON') # Sets the display to update while in remote mode
    
    @property
    def mode(self):
        return self._mode
    
    @mode.setter
    def mode(self, mode):
        if mode.lower() in ['frequency', 'frequency sweep']:
            self._mode = 'frequency sweep'
            self._vna.write(r'INIT:CONT OFF') # Continuous sampling OFF
            self._vna.write(r'SWE:COUN 1') # Set sweep count to 1 (averages is set by a different command)
            self._vna.write(r'SWE:TYPE LIN') # Set the sweep type to linear spacing (other options are logarithmic etc)
            # If the sweep mode is set to anything other than linear, the frequencies array in the "frequency sweep" function will need to be changed!
            self._vna.write(r"CALC1:PAR:SDEF 'Trace1', 'S21'") # Add a new trace for the S21 parameter
            self._vna.write(r"CALC1:PAR:SEL 'Trace1' ") # The above should become the active trace, otherwise explicitly select it
            self._vna.write(r"DISP:WIND:TRAC1:Y:AUTO ONCE") # Set the Y scale for the trace
            print('Instrument mode set to "frequency sweep".')
        else:
			raise NotImplementedError("Unrecognised measurement mode, the only current option is 'frequency sweep'.")
        
    @property
    def power(self):
        message = self._vna.query(r'SOUR:POW?')
        self._power = float(message)
        return self._power
    
    @power.setter
    def power(self, power):
        self._vna.write(f'SOUR:POW {power:.2f}')
        message = self._vna.query(r'SOUR:POW?')
        self._power = float(message)
        print(f'Output power set to {power:.2f} dBm (actual = {float(message):.2f} dBm).')  
        
    @property
    def start_frequency(self):
        message = self._vna.query('FREQ:STAR?')
        self._start_frequency = float(message)/10**9
        return self._start_frequency
    
    @start_frequency.setter
    def start_frequency(self, frequency):
        self._vna.write(f'FREQ:STAR {frequency:.4f} GHz')
        message = self._vna.query('FREQ:STAR?')
        self._start_frequency = float(message)/10**9
        print(f'Sweep start frequency set to {self._start_frequency:.4f} GHz.')
        
    @property
    def stop_frequency(self):
        message = self._vna.query('FREQ:STOP?')
        self._stop_frequency = float(message)/10**9
        return self._stop_frequency
    
    @stop_frequency.setter
    def stop_frequency(self, frequency):
        self._vna.write(f'FREQ:STOP {frequency:.4f} GHz')
        message = self._vna.query('FREQ:STOP?')
        self._stop_frequency = float(message)/10**9
        print(f'Sweep stop frequency set to {self._stop_frequency:.4f} GHz.')
        
    @property
    def sweep_time(self):
        message = self._vna.query('SWE:TIME?')
		self._sweep_time = float(message)
        return float(message)
    
    @sweep_time.setter
    def sweep_time(self, sweep_time):
        self._vna.write(f'SWE:TIME {sweep_time:.0f}')
        message = self._vna.query('SWE:TIME?')
        self._sweep_time = float(message)
        print(f'Sweep time set to {self._sweep_time:.3f} seconds.')
        
    @property
    def sweep_points(self):
        message = self._vna.query('SWE:POIN?')
        self._sweep_points = int(message)
        return self._sweep_points
    
    @sweep_points.setter
    def sweep_points(self, sweep_points):
        self._vna.write(f'SWE:POIN {sweep_points:.0f}')
        message = self._vna.query('SWE:POIN?')
        self._sweep_points = int(message)
        print(f'Total sweep points set to {self._sweep_points:.0f}')
        
    @property
    def sweep_averages(self):
        message = self._vna.query('SENS:AVER:COUN?')
        self._sweep_averages = int(message)
        return self._sweep_averages
    
    @sweep_averages.setter
    def sweep_averages(self, sweep_averages):
        if int(sweep_averages) == 1:
            self._vna.write('SENS:AVER:STAT OFF')
            self._vna.write('SENS:AVER:COUN 1; CLE')
            self._sweep_averages = 1
        else:
            self._vna.write(f'SWE:COUN {int(sweep_averages)}')
            # self._vna.write('SENS:AVER:COUN CLE')
            self._vna.write('SENS:AVER:STAT ON')
            self._vna.write(f'SENS:AVER:COUN {int(sweep_averages)}')
            message = self._vna.query('SENS:AVER:COUN?')
            self._sweep_averages = int(message)
        print(f'Number of sweep averages set to {self._sweep_averages}.')

	def get_formatted_data(self):
		data = np.array(self._vna.query(r"CALC1:DATA? FDATA ").split(','), dtype=float)
		return data

	def get_unformatted_data(self):
		# Data is 2 points per measurement, real and imaginary part
		data = np.array(self._vna.query(r"CALC1:DATA? SDATA ").split(','), dtype=float)
		return data
        
    def run_frequency_sweep(self):
        print('Starting frequency sweep...')
        self._vna.write(f'SENS:AVER:COUN {int(self._sweep_averages)}; CLE')
        self._vna.write(r'INIT') # Start the frequency sweep
        sleep(self._sweep_time*self._sweep_averages + self.post_sweep_delay_time) # Wait for the sweep to finish
		
        s21 = self.get_formatted_data() # Get the S21 data
        frequencies = np.linspace(self._start_frequency, self._stop_frequency, self._sweep_points) # Generate an array of the frequencies
        print('Finished frequency sweep!\n')
		
        return frequencies, s21
