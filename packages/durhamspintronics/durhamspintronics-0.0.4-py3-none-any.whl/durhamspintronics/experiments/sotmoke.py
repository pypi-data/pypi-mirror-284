# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:01:53 2023

@author: Ben Nicholson
"""

from durhamspintronics.instruments.ni import NI_pci6713, NI_pci6034E
import numpy as np
import matplotlib.pyplot as plt
from time import sleep, strftime, localtime
import os


FIELD_CALIBRATION = [0.1955, -29.073, 114.1] # Debi March 2024

CURRENT_CALIBRATION = [0.5, 0] # slope, intercept


class BaseExperiment:
    MIN_SIGNAL_FREQUENCY = 0.01 # Hz
    MAX_SIGNAL_FREQUENCY = 50 # Hz
    HALL_DRIVE_VOLTAGE = 8.0 # V
    
    CALIBRATED_X_AXIS_TITLE = r'Magnetic Field (mT)' # Strictly speaking, it should be... r'$\mu_0$H (mT)'
    RAW_X_AXIS_TITLE = 'Hall Voltage (V)'
    
    DEFAULT_REBIN_SIZE = 0.05 # mT
    DEFAULT_NORM_FRACTION = 0.9
    
    def __init__(self):
        self.output_device = NI_pci6713()
        self.input_device = NI_pci6034E()
        
        self.output_device.reset()
        self.input_device.reset()
        self._start_delay = 2
        
        self._frequency = 1
        
        self._x_calibration = None
        self.y_calibration = None
        
        self.y_label = 'Kerr Signal (V)'
        
        self._standard_setup()
        
      
    def _standard_setup(self):
        self.x_nickname = 'Hall Probe'
        self.y_nickname = 'Kerr'
        self.output_device.add_ao_channel('Hall Probe', 'ao1', 'DC', self.HALL_DRIVE_VOLTAGE)
        self.output_device.add_ao_channel('Magnet', 'ao2', 'Triangle', 5.0) 
        self.input_device.add_ai_channel(self.y_nickname, 'ai1')
        self.input_device.add_ai_channel(self.x_nickname, 'ai3')
        
    def standard_setup(self):
        '''for compatibility...'''
        pass     
      
      
    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, freq):
        if self.MIN_SIGNAL_FREQUENCY <= freq <= self.MAX_SIGNAL_FREQUENCY:
            self._frequency = freq
            self.output_device.frequency = freq
            self.input_device.frequency = freq
        else:
            print(f'ERROR. Frequency must be between {self.MIN_SIGNAL_FREQUENCY} and {self.MAX_SIGNAL_FREQUENCY} Hz.')
            print('The frequency has not been changed.\n')
            
            
    @property
    def start_delay(self):
        return self._start_delay
    
    @start_delay.setter
    def start_delay(self, start_delay):
        self._start_delay = start_delay 
            
            
    def set_amplitude(self, nickname=None, amplitude=None):
        if (not nickname) or (not amplitude):
            print('ERROR. To set an output amplitude, use "set_amplitude("magnet", 3.0)".')
            print('Where "magnet" is the channel nickname, and 3.0 is the new amplitude.')
            print('The amplitude must be between -10 and +10 V.')
            print('The available channel nicknames are:')
            for chan in self.output_device._channel_list:
                print(chan['nickname'])
            print('The amplitude has not been changed\n')
        elif abs(amplitude) > self.output_device.MAX_AMPLITUDE:
            print(f'ERROR. The amplitude must be between -{self.output_device.MAX_AMPLITUDE} and +{self.output_device.MAX_AMPLITUDE} V.')
            print('The amplitude has not been changed\n')
        elif nickname.lower() not in self.output_device._nickname_list:
                print('ERROR. Nickname not found, the available channel nicknames are:')
                for chan in self.output_device._channel_list:
                    print(chan['nickname'])
                print('The amplitude has not been changed\n')
        else:
            self.output_device.set_amplitude(nickname, amplitude) 
        
    
    def _patch_file_header(self, header=''):
        return header.replace('CALIBRATION', 'field calibration: {}'.format(self._x_calibration))
        
     
    def save_last_result(self, file_name=None, comment=None):
        if not file_name:
            print('ERROR. No file name provided.')
            return False
            
        header = '\n'.join([f'Data Saved on {strftime("%d.%m.%Y", localtime())} at {strftime("%H:%M:%S", localtime())}',
                            f'Number of averages: {self._nloops}',
                            f'Frequency: {self.frequency} Hz',
                            'CALIBRATION\n'])
        for n, chan in enumerate(self.output_device._channel_list):
            header += 'Output {}: nickname={}, channel={}, mode={}, amplitude={}, max_val={}\n'.format(n+1, chan['nickname'], chan['channel'], chan['mode'], chan['amplitude'], chan['max_val'])
        for n, chan in enumerate(self.input_device._channel_list):
            header += 'Input {}: nickname={}, channel={}, max_val={}\n'.format(n+1, chan['nickname'], chan['channel'], chan['max_val'])
        header += f'User comment: {comment}\n' if comment else 'No user comment entered.\n' 
        header += f'{self.CALIBRATED_X_AXIS_TITLE}, {self.y_label}'
        
        np.savetxt(str(file_name), np.column_stack((self.x, self.y)), header=self._patch_file_header(header))
     
    
    def _run(self, nloops):    
        self._nloops = nloops
        self.datapoints = int(self.input_device.sampling_rate/self.frequency)
        
        self.output_device.start()
        self.input_device.start() 
        
        sleep(self.start_delay)
        data = self.input_device.read(int(nloops*self.datapoints), timeout=120)
        
        self.input_device.stop()
        self.output_device.stop()
        
        split_data = self._separate_data(data)
        
        return split_data
        
    
    def _separate_data(self, data):
        for n, chan in enumerate(self.input_device.channel_list):
            if 'dummy' not in chan['nickname'].lower():
                if self.x_nickname.lower() in chan['nickname'].lower():
                    x = data[n]
                if self.y_nickname.lower() in chan['nickname'].lower():
                    y = data[n]
        return x, y
        
    
    def run(self, nloops, rebin=True, normalise=True, plot=True, file_name=None, comment=None):
        amplitude_set = False
        for chan in self.output_device.channel_list:
            if chan['nickname'].lower() != 'hall probe' and chan['amplitude'] > 0: 
                amplitude_set = True
        if not amplitude_set: 
            print('No outputs are being driven with a time varying signal - is this what you intended?')

        self.raw_x, self.raw_y = self._run(nloops)
        
        self.process_data(rebin=rebin, 
                          normalise=normalise, 
                          plot=plot, 
                          file_name=file_name, 
                          comment=comment)   
        

    def process_data(self, rebin=True, rebin_size=None, normalise=True, norm_fraction=None, plot=True, file_name=None, comment=None):   
        if normalise:
            self.y_label = 'Normalised Kerr Signal'
        else: 
            self.y_label = 'Kerr Signal (V)'
        
        folded_x, folded_y = self._fold_data(self.raw_x, self.raw_y)
        
        self.x = self._apply_calibration(folded_x, self._x_calibration)
        self.y = self._apply_calibration(folded_y, self.y_calibration)
       
        if rebin:                
            rebin_x = rebin_size if rebin_size else self.DEFAULT_REBIN_SIZE
            self.x, self.y = self._rebin_data(self.x, self.y, rebin_x)
        if normalise: 
            norm_frac = norm_fraction if norm_fraction else self.DEFAULT_NORM_FRACTION
            self.x, self.y =  self._normalise_data(self.x, self.y, norm_frac)
        
        if plot:
            plt.figure(figsize=(9,7))
            plt.subplot2grid((3,3), (0,0), rowspan=2, colspan=2)
            plt.plot(self.x, self.y)
            plt.ylabel(self.y_label, fontsize=16)
            plt.xlabel(self.CALIBRATED_X_AXIS_TITLE, fontsize=16)
    
            plt.subplot2grid((3,6), (2,0), colspan=3)
            plt.title('Kerr Signal (V) vs. Time')
            plt.plot(self.raw_y)
            plt.xticks([])
    
            plt.subplot2grid((3,6), (2,3), colspan=3)
            plt.title(f'{self.RAW_X_AXIS_TITLE} vs. Time')
            plt.plot(self.raw_x)
            plt.xticks([])
    
            plt.subplot2grid((3,3), (0,2))
            plt.title('Raw Data')
            plt.plot(self.raw_x, self.raw_y)
            plt.xlabel(self.RAW_X_AXIS_TITLE)
            plt.yticks([])
    
            plt.subplot2grid((3,3), (1,2))
            plt.title('Pre- Binning/Normalisation')
            plt.plot(folded_x, folded_y)
            plt.xlabel(self.RAW_X_AXIS_TITLE)
            plt.yticks([])
    
            plt.subplots_adjust(left=0.1, right=0.96, bottom=0.04, top=0.95, hspace=0.57, wspace=0.45)
            plt.show()
        
        if file_name:
            self.save_last_result(file_name=file_name, comment=comment)

        
    def _fold_data(self, x, y):
        folded_x, folded_y = np.zeros(self.datapoints), np.zeros(self.datapoints)
        for n in range(self._nloops):
            start, stop = int(n*self.datapoints), int((n+1)*self.datapoints)
            folded_x += x[start:stop]
            folded_y += y[start:stop]
        return folded_x / self._nloops, folded_y / self._nloops


    def _apply_calibration(self, data, cal_list=None):
        # Convert hall voltage (V) to field (mT)
        if cal_list is None: 
            return data
        calibrated = np.zeros(self.datapoints)
        for n in range(len(cal_list)):
                calibrated += cal_list[n]*data**(len(cal_list)-n-1)
        return calibrated


    def _rebin_data(self, x_data, y_data, rebin_x):
        # We want to average nearby data points to decrease noise and point density
        # First, get the lower and upper field limits to define histogram bin ends
        min_limit = np.min(x_data)-(np.min(x_data)%rebin_x)+rebin_x
        max_limit = np.max(x_data)-(np.max(x_data)%rebin_x)
        min_index = np.argmin(x_data)
        max_index = np.argmax(x_data)

        # Separate the up sweep and down sweep before cleaning up the signals
        down_y = y_data[np.min([min_index, max_index]):np.max([min_index, max_index])]
        up_y = np.concatenate((y_data[np.max([min_index, max_index]):], y_data[:np.min([min_index, max_index])]))
        down_x = x_data[np.min([min_index, max_index]):np.max([min_index, max_index])]
        up_x = np.concatenate((x_data[np.max([min_index, max_index]):], x_data[:np.min([min_index, max_index])]))

        # Sort the data into the correct histogram bins
        binned_up_x = np.zeros(round((max_limit-min_limit)/rebin_x))
        binned_up_y = np.zeros(round((max_limit-min_limit)/rebin_x))
        binned_upnum = np.zeros(round((max_limit-min_limit)/rebin_x))
        for n, i in enumerate(up_x):
            if (i >= min_limit) and (i <= max_limit):
                binned_up_x[round(np.ceil(i/rebin_x)-round(min_limit/rebin_x)-1)] += i
                binned_up_y[round(np.ceil(i/rebin_x)-round(min_limit/rebin_x)-1)] += up_y[n]
                binned_upnum[round(np.ceil(i/rebin_x)-round(min_limit/rebin_x)-1)] += 1

        binned_down_x = np.zeros(round((max_limit-min_limit)/rebin_x))
        binned_down_y = np.zeros(round((max_limit-min_limit)/rebin_x))
        binned_downnum = np.zeros(round((max_limit-min_limit)/rebin_x))
        for n, i in enumerate(down_x):
            if (i >= min_limit) and (i <= max_limit):
                binned_down_x[round(np.ceil(i/rebin_x)-round(min_limit/rebin_x)-1)] += i
                binned_down_y[round(np.ceil(i/rebin_x)-round(min_limit/rebin_x)-1)] += down_y[n]
                binned_downnum[round(np.ceil(i/rebin_x)-round(min_limit/rebin_x)-1)] += 1

        # Divide by the number to complete the average, not strictly necessary since we later normalise.
        binned_up_x /= binned_upnum
        binned_up_y /= binned_upnum
        binned_down_x /= binned_downnum
        binned_down_y /= binned_downnum

        # Recombine down and up sweeps into one array
        return np.concatenate((binned_up_x, binned_down_x[::-1])), np.concatenate((binned_up_y, binned_down_y[::-1]))


    def _normalise_data(self, x_data, y_data, norm_fraction):
        # Use the high and low x regions to normalise the loop
        lowerlim = norm_fraction*np.min(x_data)
        upperlim = norm_fraction*np.max(x_data)
        lower_y = []
        upper_y = []
        for n, i in enumerate(x_data):
            if i < lowerlim:
                lower_y.append(y_data[n])
            elif i > upperlim:
                upper_y.append(y_data[n])
        
        # Normalise the y signal
        y_data = y_data - (np.mean(lower_y)+np.mean(upper_y))/2
        y_data /= abs(-np.mean(lower_y)+np.mean(upper_y))/2
        return x_data, y_data

        
    def test(self):
        print(self.input_device._channel_list)
     
        


class FieldExperiment(BaseExperiment):
    CALIBRATED_X_AXIS_TITLE = r'Magnetic Field (mT)' # Strictly speaking, it should be... r'$\mu_0$H (mT)'
    RAW_X_AXIS_TITLE = 'Hall Voltage (V)'
    DEFAULT_FIELD_AMPLITUDE = 5.0
    
    def __init__(self):
        super().__init__()
        self._x_calibration = FIELD_CALIBRATION
    
    @property
    def field_calibration(self):
        print('The current x axis calibration is:')
        print(' + '.join([f'{i}*x^{len(self._x_calibration)-1-n}' for n, i in enumerate(self._x_calibration)]))
        return self._x_calibration
    
    @field_calibration.setter
    def field_calibration(self, x_calibration):
        print('The x axis calibration has been set to:')
        print(' + '.join([f'{i}*x^{len(x_calibration)-1-n}' for n, i in enumerate(x_calibration)]))
        self._x_calibration = x_calibration


    def _standard_setup(self):
        self.x_nickname = 'Hall Probe'
        self.y_nickname = 'Kerr'
        self.output_device.add_ao_channel('Hall Probe', 'ao1', 'DC', self.HALL_DRIVE_VOLTAGE)
        self.output_device.add_ao_channel('Magnet', 'ao2', 'Triangle', self.DEFAULT_FIELD_AMPLITUDE) 
        self.input_device.add_ai_channel(self.y_nickname, 'ai1')
        self.input_device.add_ai_channel(self.x_nickname, 'ai3')


    @property
    def field_amplitude(self):
        return self.output_device.get_amplitude('magnet')
        
    @field_amplitude.setter
    def field_amplitude(self, amplitude):
        if not self.output_device.set_amplitude('magnet', amplitude): 
            print('No channel named "magnet". Amplitude not set.')
         

    def run(self, nloops, rebin=True, normalise=True, plot=True, file_name=None, comment=None):
        if not self.field_amplitude > 0:
            print('Field_amplitude was not set. It should be > 0 and <= 10 V.')
            print(f'Setting field_amplitude to {self.DEFAULT_FIELD_AMPLITUDE} V and continuing.')
            self.field_amplitude = self.DEFAULT_FIELD_AMPLITUDE
        
        super().run(nloops, rebin=rebin, normalise=normalise, plot=plot, 
                    file_name=file_name, comment=comment)  
     



class CurrentExperiment(BaseExperiment):
    CALIBRATED_X_AXIS_TITLE = 'Sample Current (A)'
    RAW_X_AXIS_TITLE = 'PSU Drive Voltage (V)'
    DEFAULT_CURRENT_AMPLITUDE = 0.1
    
    DEFAULT_REBIN_SIZE = 0.001
    
    def __init__(self):
        super().__init__()
        self._x_calibration = CURRENT_CALIBRATION
        
        
    def _standard_setup(self):
        self.x_nickname = 'Sample Current'
        self.y_nickname = 'Kerr'
        self.output_device.add_ao_channel('current', 'ao2', 'Triangle', self.DEFAULT_CURRENT_AMPLITUDE) # normal kepco to sample
        self.input_device.add_ai_channel(self.y_nickname, 'ai1')
        self.input_device.add_ai_channel(self.x_nickname, 'ai5') # drive voltage to psu

    def patch_file_header(self, header=''):
        return header.replace('CALIBRATION', 'Current calibration: {}'.format(self._x_calibration))
     

    @property
    def current_amplitude(self):
            return self.output_device.get_amplitude('current')
    @current_amplitude.setter
    def current_amplitude(self, amplitude):
        if not self.output_device.set_amplitude('current', amplitude): print('No channel named "magnet". Amplitude not set.')
    






class CurrentExperimentWithField(CurrentExperiment):
    '''Fix field, sweep current'''
    
    DEFAULT_FIELD_AMPLITUDE = 0.0
    
    def __init__(self):
        super().__init__()
        self.z_calibration = FIELD_CALIBRATION
     
    def _standard_setup(self):
        self.x_nickname = 'Sample Current'
        self.y_nickname = 'Kerr'
        self.z_nickname = 'Hall Probe'
        self.input_device.add_ai_channel(self.y_nickname, 'ai1')
        self.input_device.add_ai_channel(self.z_nickname, 'ai3')
        self.input_device.add_ai_channel(self.x_nickname, 'ai5') # drive voltage to psu
        self.output_device.add_ao_channel('Hall Probe', 'ao1', 'DC', self.HALL_DRIVE_VOLTAGE)
        self.output_device.add_ao_channel('Magnet', 'ao2', 'DC', self.DEFAULT_FIELD_AMPLITUDE) # normal kepco to magnet
        self.output_device.add_ao_channel('current', 'ao0', 'Sinusoid', self.DEFAULT_CURRENT_AMPLITUDE) # second kepco to sample
        
        
    def patch_file_header(self, header=''):
        return header.replace('CALIBRATION', 'Current calibration: {}\nField calibration: {}\nField (mT): {}'.format(self._x_calibration, self.z_calibration, self.z))
    
    def _separate_data(self, data):
        for n, chan in enumerate(self.input_device.channel_list):
            if 'dummy' not in chan['nickname'].lower():
                if self.x_nickname.lower() in chan['nickname'].lower():
                    x = data[n]
                if self.y_nickname.lower() in chan['nickname'].lower():
                    y = data[n]
                if self.z_nickname.lower() in chan['nickname'].lower():
                    z = data[n]     
        return x, y, z
    
    def run(self, nloops, rebin=True, normalise=True, plot=True, file_name=None, comment=None):
    
        self.raw_x, self.raw_y, raw_z = self._run(nloops)
        
        z = self._apply_calibration(raw_z, self.z_calibration)
        self.z = str(np.mean(z)) + str(np.std(z))
        print('applied field = {}'.format(self.z))
        
        self.process_data(rebin=rebin, normalise=normalise, plot=plot, file_name=file_name, comment=comment)   
    
    
    @property
    def field_amplitude(self):
            return self.output_device.get_amplitude('magnet')
    @field_amplitude.setter
    def field_amplitude(self, amplitude):
        if not self.output_device.set_amplitude('magnet', amplitude): print('No channel named "magnet". Amplitude not set.')
      
    


class FieldExperimentWithCurrent(FieldExperiment):
    '''Fix current, sweep field'''

    DEFAULT_CURRENT_AMPLITUDE = 0.0
    
    def __init__(self):
        super().__init__()
        self.z_calibration = CURRENT_CALIBRATION
    
    
    def _standard_setup(self):
        self.x_nickname = 'Hall Probe'
        self.y_nickname = 'Kerr'
        self.z_nickname = 'Sample Current'
        self.input_device.add_ai_channel(self.y_nickname, 'ai1')
        self.input_device.add_ai_channel(self.x_nickname, 'ai3')
        self.input_device.add_ai_channel(self.z_nickname, 'ai5') # drive voltage to psu
        self.output_device.add_ao_channel('Hall Probe', 'ao1', 'DC', self.HALL_DRIVE_VOLTAGE)
        self.output_device.add_ao_channel('Magnet', 'ao2', 'Triangle', self.DEFAULT_FIELD_AMPLITUDE) # normal kepco to magnet
        self.output_device.add_ao_channel('current', 'ao0', 'DC', self.DEFAULT_CURRENT_AMPLITUDE) # second kepco to sample
        
        
    def patch_file_header(self, header=''):
        return header.replace('CALIBRATION', 'Current calibration: {}\nField calibration: {}\nCurrent (A): {}'.format(self.z_calibration, self._x_calibration, self.z))
    
    def _separate_data(self, data):
        for n, chan in enumerate(self.input_device.channel_list):
            if 'dummy' not in chan['nickname'].lower():
                if self.x_nickname.lower() in chan['nickname'].lower():
                    x = data[n]
                if self.y_nickname.lower() in chan['nickname'].lower():
                    y = data[n]
                if self.z_nickname.lower() in chan['nickname'].lower():
                    z = data[n]        
        return x, y, z
    
    def run(self, nloops, rebin=True, normalise=True, plot=True, file_name=None, comment=None):
    
        self.raw_x, self.raw_y, raw_z = self._run(nloops)
        
        z = self._apply_calibration(raw_z, self.z_calibration)
        self.z = str(np.mean(z)) + str(np.std(z))
        print('sample current = {}'.format(self.z))
        
        self.process_data(rebin=rebin, normalise=normalise, plot=plot, file_name=file_name, comment=comment)   
    
    
    @property
    def current_amplitude(self):
            return self.output_device.get_amplitude('current')
    @current_amplitude.setter
    def current_amplitude(self, amplitude):
        if not self.output_device.set_amplitude('current', amplitude): print('No channel named "magnet". Amplitude not set.')
    

def plot_result(filelist, x_label=f'${chr(956)}_0$H (mT)', y_label='Kerr Signal'):
    if not isinstance(filelist, list):
        print('Argument type must be a list, even if you only give one file name.')
    else:
        plt.figure(dpi=150)
        
        for filepath in filelist:
            filename = os.path.basename(filepath).split('.')[0]
            data = np.genfromtxt(filepath)
            plt.plot(data[:,0], data[:,1], label=filename)
            
        plt.legend(loc='best', fontsize=7)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()
        



# To remind users to update their scripts to version 2.0...
class Experiment():
    def __init__(self):
        raise Exception(r'''The SOTMOKE software has been upgraded to version 2.0 and the Experiment class has been removed!
        The new 2.0 script can be found at C:\Users\SOTMOKE\Documents\Data\example_scipt_2.0.ipynb. 
        Note, there are a few minor command changes, as detailed in the "Useful Commands" section.''')
