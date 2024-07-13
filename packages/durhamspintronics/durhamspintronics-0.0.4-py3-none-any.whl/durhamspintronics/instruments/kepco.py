# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:01:53 2023

@author: Ben Nicholson
"""

import pyvisa as visa

class BOP():
    """
    KEPCO BOP power supply.
    """
    def __init__(self, com_port):
        """
        Initialises the power supply object with the given communication port.

        Args:
            com_port (str): The communication port of the instrument.
        """
        self.com_port = com_port
        self._kepco = None
        self._voltage = 50
        self._current = 0
        
        
    def open_connection(self):
        self._kepco = visa.ResourceManager().open_resource(self.com_port, write_termination = '\n', read_termination='\n')

    def close_connection(self):
        if self._kepco:
            self._kepco.close()
            print(r'Kepco connection closed')
            
    def get_idn(self):
        message = self._kepco.query(r'*IDN?')
        return message
    
    @property
    def voltage(self):
        message = self._kepco.query(r'VOLT?')
        self._voltage = float(message)
        return self._voltage
    
    @voltage.setter
    def voltage(self, voltage):
        self._kepco.write(f'VOLT {voltage:.4f}')
        message = self._kepco.query(r'VOLT?')
        print(f'Kepco voltage set to {voltage:.4f} V (actual = {float(message):.4f} V).')
        self._voltage = float(message)
        return self._voltage
        
    @property
    def current(self):
        message = self._kepco.query(r'CURR?')
        self._current = float(message)
        return self._current
    
    @current.setter
    def current(self, current):
        self._kepco.write(f'CURR {current:.4f}')
        message = self._kepco.query(r'CURR?')
        print(f'Kepco current set to {current:.4f} A (actual = {float(message):.4f} A).')
        self._current = float(message)
        return self._current
        
    def set_mode_constant_current(self):
        self._kepco.write(r'FUNC:MODE CURR')
        
    def set_mode_constant_voltage(self):
        self._kepco.write(r'FUNC:MODE VOLT')
        
    def output_on(self):
        self._kepco.write(r'OUTP 1')
        
    def output_off(self):
        self._kepco.write(r'OUTP OFF')
        
    def reset(self):
        self._kepco.write(r'*RST')
