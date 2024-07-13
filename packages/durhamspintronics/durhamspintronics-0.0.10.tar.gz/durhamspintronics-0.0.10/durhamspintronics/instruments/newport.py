# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:01:53 2023

@author: Ben Nicholson
"""

import serial
from time import time, sleep




class ESP300():
    def __init__(self, com_port, timeout=5):
        self.com_port = com_port
        self.timeout = timeout
        self.terminator = '\r'
        
        
    def query(self, command):
        command += self.terminator
        with serial.Serial(self.com_port, baudrate=19200, timeout=self.timeout) as stage:
            stage.write(command.encode())
            # Check to see if return bytes are available
            start_time = time()
            while stage.inWaiting() == 0:
                sleep(0.3)
                if time() > start_time+self.timeout:
                    print(stage.read_all())
                    raise TimeoutError('No return bytes available after write command.')
            sleep(0.3)
            message = stage.read_all().decode().strip()
        return message
    
    def write(self, command):
        command += self.terminator
        with serial.Serial(self.com_port, baudrate=19200, timeout=self.timeout) as stage:
            stage.write(command.encode())
    
    
    def get_target_position(self, axis):
        return self.query('{}DP'.format(axis))
       
    def get_position(self, axis):
        return self.query('{}TP'.format(axis))
        
    
    def move_relative(self, axis, distance, wait_until_done=False, timeout=30):
        self.write('{}PR{}'.format(axis, distance))
        if wait_until_done:     
            start_time = time()
            while (self.query('1MD') == '0'):
                if time() < start_time+timeout:
                    sleep(1)
                else:
                    raise TimeoutError(f'Stage took longer than {timeout}s to move.')
        
    def move_absolute(self, axis, position, wait_until_done=False, timeout=30):
        self.write('{}PA{}'.format(axis, position))
        if wait_until_done:
            start_time = time()
            while (self.query('1MD') == '0'):
                if time() < start_time+timeout:
                    sleep(1)
                else:
                    raise TimeoutError(f'Stage took longer than {timeout}s to move.')
        
        
    def set_acceleration(self, axis, acceleration):
        self.write('{}AC{}'.format(axis, acceleration))
        
    def get_acceleration(self, axis):
        return self.query('{}AC?'.format(axis))
    
            
    def set_velocity(self, axis, velocity):
        self.write('{}VA{}'.format(axis, velocity))
        
    def get_velocity(self, axis):
        return self.query('{}VA?'.format(axis))
    
        
    def set_home(self, axis, position):
        self.write('{}DH{}'.format(axis, position))
        print('''The current position of axis {axis} is now the axis home, 
              the position has been renamed to {position}.''')

    def move_home(self, axis):
        self.write('{}OR1'.format(axis))
        
       
    def motor_off(self, axis):
        self.write('{}MF'.format(axis))
        
    def motor_on(self, axis):
        self.write('{}MO'.format(axis))
        
        
    def abort_motion(self):
        self.write('AB'.encode())
        
        
    def get_stage_id(self, axis):
        return self.query('{}ID'.format(axis))
