# -*- coding: utf-8 -*-
"""
Created on Wed May 31 20:10:49 2023

@author: Ben Nicholson
"""

import nidaqmx
import numpy as np
import serial
from time import time, sleep




class NI_pci6713:
    '''PCI Analogue output device.'''
    
    MODES = ['dc', 'triangle', 'sinusoid']
    MAX_AMPLITUDE = 10
    
    def __init__(self):
        self._task = nidaqmx.Task()
        self._system = nidaqmx.system.System.local()
        self._clock_channel = 'RTSI7'
        self._output_data_list = []
        self._channel_list = []
        self._nickname_list = []
        self._frequency = 1 # Hz
        self._export_clock = True
        
        # These may be changed if you know what you are doing,
        # although they will probably be better as @properties...
        self.sampling_rate = 800000 # Samples per second
        self.continuous_sampling = True
        
        # The National Instruments driver version should be 18.5.0, 
        # you can check the version by running the following command:
        # print('Driver version = {}.{}.{}'.format(*self.__system.driver_version))
        # If the version is not 18.5.0 then it may work, however, the card is obsolute 
        # in the latest versions so update with caution!
        
        # Check device exists and get its name
        self.device_name = None
        for device in self._system.devices:
            if device.product_type == 'PCI-6713':
                self.device_name = device.name
        if not self.device_name:
            raise Exception("Device 'PCI-6713' not found in device list.")
    
    
    @property
    def channel_list(self):
        '''Each entry is a dictionary containing the required info for that channel,
        e.g. mode (dc, triangle...), amplitude, nickname etc... '''
        return self._channel_list
    
    
    @property
    def frequency(self):
        return self._frequency
    
    @frequency.setter
    def frequency(self, freq): 
        self._frequency = freq
        for n, chan in enumerate(self._channel_list):
            if chan['mode'].lower() == 'dc': 
                self._output_data_list[n] = self.dc_waveform_data(chan['amplitude'])
            elif chan['mode'].lower() == 'triangle': 
                self._output_data_list[n] = self.triangle_waveform_data(chan['amplitude'])
            elif chan['mode'].lower() == 'sinusoid': 
                self._output_data_list[n] = self.sinusoid_waveform_data(chan['amplitude'])
            

    def get_amplitude(self, nickname):
        for n, chan in enumerate(self._channel_list):
            if chan['nickname'].lower() == nickname.lower():
                return chan['amplitude']
        return None

    def set_amplitude(self, nickname, amplitude):
        if amplitude > self.MAX_AMPLITUDE:
            print(f'''Requested amplitude ({self.MAX_AMPLITUDE} V) is greater than the max amplitude 
                  ({amplitude} V). The amplitude has been set to {self.MAX_AMPLITUDE} V.''')
        for n, chan in enumerate(self._channel_list):
            if chan['nickname'].lower() == nickname.lower():
                temp_arr = self._output_data_list[n]
                temp_arr /= np.max(temp_arr)
                temp_arr *= amplitude
                self._output_data_list[n] = list(temp_arr)
                self._channel_list[n]['amplitude'] = amplitude 
                return True
        return False
    
    
    def set_mode(self, nickname, mode):
        if mode.lower() not in self.MODES: 
            raise RuntimeError('Unrecognised channel mode, the options are {}'.format(', '.join(*self.MODES)))
        for n, channel in enumerate(self._channel_list):
            if channel['nickname'].lower() == nickname:
                if mode.lower() == 'dc': 
                    self._channel_list[n]['mode'] = 'dc'
                    self._output_data_list[n] = self.dc_waveform_data(self._channel_list[n]['amplitude'])
                elif mode.lower() == 'triangle': 
                    self._channel_list[n]['mode'] = 'triangle'
                    self._output_data_list[n] = self.triangle_waveform_data(self._channel_list[n]['amplitude'])
                elif mode.lower() == 'sinusoid': 
                    self._channel_list[n]['mode'] = 'sinusoid'
                    self._output_data_list[n] = self.sinusoid_waveform_data(self._channel_list[n]['amplitude']) 


    def dc_waveform_data(self, amplitude): 
        return list(np.full(int(self.sampling_rate/self._frequency), amplitude))

    def triangle_waveform_data(self, amplitude):        
        ramp = np.linspace(-1, 1, int(self.sampling_rate/self._frequency/2))
        return list(amplitude*np.concatenate((ramp, ramp[::-1])))
    
    def sinusoid_waveform_data(self, amplitude):
        return list(np.sin(np.linspace(0, 2*np.pi, int(self.sampling_rate/self._frequency))))
    
    
    def add_ao_channel(self, nickname, channel, mode, amplitude, max_val=10.0):
        if mode.lower() not in self.MODES: 
            raise RuntimeError('Unrecognised channel mode, the options are {}'.format(', '.join(*self.MODES)))
        
        if mode.lower() == 'dc': 
            data = self.dc_waveform_data(amplitude)
        elif mode.lower() == 'triangle': 
            data = self.triangle_waveform_data(amplitude)
        elif mode.lower() == 'sinusoid': 
            data = self.sinusoid_waveform_data(amplitude)    
        
        # To ensure channel is in the format "Dev1/ao0" rather than just "ao0":
        if self.device_name not in channel:
            channel = self.device_name+r'/'+channel
            
        self._task.ao_channels.add_ao_voltage_chan(channel, 
                                                   nickname, 
                                                   min_val=-1*max_val, 
                                                   max_val=max_val, 
                                                   units=nidaqmx.constants.VoltageUnits.VOLTS)
        self._channel_list.append({'channel' : channel,
                                  'nickname' : nickname,
                                  'mode' : mode,
                                  'amplitude' : amplitude,
                                  'max_val' : max_val})
        self._output_data_list.append(data)
        self._nickname_list.append(nickname.lower())
        print(f'''Analogue output added: nickname={nickname}, channel={channel}, mode={mode}, amplitude={amplitude}, max_val={max_val}''')
        return True
        
        
    def _timing(self):
        # Documentation refences "samples per channel", yet it seems to behave more
        # like "samples per task", i.e. number of channels * samples per channel...?
        samples_per_chan=int(len(self._output_data_list)*len(self._output_data_list[0]))
        if self.continuous_sampling:
            self._task.timing.cfg_samp_clk_timing(self.sampling_rate, 
                                                  active_edge = nidaqmx.constants.Edge.RISING, 
                                                  sample_mode = nidaqmx.constants.AcquisitionType.CONTINUOUS, 
                                                  samps_per_chan = samples_per_chan)
        else:
            raise NotImplementedError
        
        
    def status(self):
        print('This task is currently OFF.' if self.__task.is_task_done() else 'This task is currently ON.')
        print(f'There are {len(self._channel_list)} channels associated with this task:')
        for n, channel in enumerate(self._channel_list):
            print(n+1, f'''"{channel['nickname']}" on channel {channel['channel']}, 
                  mode = {channel['mode']}, amplitude = {channel['amplitude']} V, 
                  max range = {channel['max_val']} V.''')
        print(f'The timing mode is set to {"continuous" if self.continuous_sampling else "finite"} samples.')
        if self._export_clock:
            print('The internal clock is being output on channel {self._clock_channel}')
        else:
            print('The internal clock is not being output.')
            
            
    def start(self):
        print('Starting output task...')
        if self._export_clock:
            self._task.export_signals.export_signal(nidaqmx.constants.Signal.TWENTY_MHZ_TIMEBASE_CLOCK, 
                                                    self._clock_channel)
        self._timing()
        # nidaqmx code does not like the output data format to be a list of lists if there is only one output channel.
        # If there is more than one output, a list of lists is the correct format.
        if len(self._output_data_list) == 1:
            self._task.write(self._output_data_list[0], auto_start=True)
        else:
            self._task.write(self._output_data_list, auto_start=True)
            
            
    def stop(self):
        self._task.stop()
        
        # When stop task is called, the output will remain at the last written point.
        # This may leave the magnet at a very high current if it happens to stop at the peak.
        # Hence, write 0 V to each channel...
        zero_output = []
        for n in range(len(self._output_data_list)):
            zero_output.append(list(np.zeros(10000)))
        self._task.timing.cfg_samp_clk_timing(self.sampling_rate, 
                                              active_edge = nidaqmx.constants.Edge.RISING, 
                                              sample_mode = nidaqmx.constants.AcquisitionType.FINITE, 
                                              samps_per_chan = 10000*len(self._output_data_list))
        if len(self._output_data_list) == 1:
            self._task.write(zero_output[0], auto_start=True)
        else:
            self._task.write(zero_output, auto_start=True)
        
        # Now stop the zero output task...
        self._task.wait_until_done()
        self._task.stop()
        print('Output task stopped.')
        
        
    def close(self):
        self._task.close()
        
        
    def reset(self):
        nidaqmx.system.device.Device(self.device_name).reset_device()








class NI_pci6034E:
    '''PCI Analogue input device.'''
    
    def __init__(self):
        self._task = nidaqmx.Task()
        self._system = nidaqmx.system.System.local()
        self._clock_channel = 'RTSI7'
        self._channel_list = []
        self._import_clock = True
        
        # These may be changed if you know what you are doing,
        # although they will probably be better as @properties...
        self.sampling_rate = 100000
        self.continuous_sampling = False
        
        # The National Instruments driver version should be 18.5.0, 
        # you can check the version by running the following command:
        # print('Driver version = {}.{}.{}'.format(*self.__system.driver_version))
        # If the version is not 18.5.0 then it may work, however, the card is obsolute 
        # in the latest versions so update with caution!
        
        # Check device exists and get its name
        self.device_name = None
        for device in self._system.devices:
            if device.product_type == 'PCI-6034E':
                self.device_name = device.name
        if not self.device_name:
            raise Exception("Device 'PCI-6034E' not found in device list.")
            
            
    @property
    def channel_list(self): 
        '''Each entry is a dictionary containing the required info for that channel,
        e.g. nickname, max value etc... '''
        return self._channel_list       
    
    
    @property
    def frequency(self):
        return None
    
    @frequency.setter
    def frequency(self, freq):
        pass
    
    
    def add_ai_channel(self, nickname, channel, max_val=10.0, dummy_channel=True):
        if self.device_name not in channel:
            channel = self.device_name+r'/'+channel
        if dummy_channel:
            self._task.ai_channels.add_ai_voltage_chan(channel, 
                                                       nickname+'_dummy', 
                                                       min_val=-1*max_val, 
                                                       max_val=max_val, 
                                                       units=nidaqmx.constants.VoltageUnits.VOLTS)
            self._channel_list.append({'channel' : channel,
                                      'nickname' : nickname+'_dummy',
                                      'max_val' : max_val})
            print('Analogue input added: nickname={}, channel={}, max_val={}'.format(nickname+'_dummy', channel, max_val))
        self._task.ai_channels.add_ai_voltage_chan(channel, 
                                                   nickname, 
                                                   min_val=-1*max_val, 
                                                   max_val=max_val, 
                                                   units=nidaqmx.constants.VoltageUnits.VOLTS)
        self._channel_list.append({'channel' : channel,
                                  'nickname' : nickname,
                                  'max_val' : max_val})
        print('Analogue input added: nickname={}, channel={}, max_val={}'.format(nickname, channel, max_val))

        
    def _timing(self, npoints):
        if self.continuous_sampling:
            raise NotImplementedError
        else:
            self._task.timing.cfg_samp_clk_timing(self.sampling_rate, 
                                                  active_edge=nidaqmx.constants.Edge.RISING, 
                                                  sample_mode=nidaqmx.constants.AcquisitionType.FINITE, 
                                                  samps_per_chan=int(npoints))
        
    def status(self):
        print('This task is currently OFF.' if self._task.is_task_done() else 'This task is currently ON.')
        print('There are {} channels associated with this task:'.format(len(self._channel_list)))
        for n, channel in enumerate(self._channel_list):
            print(n+1, "'{}' on channel {}, maximum input = {} V.".format(channel['nickname'], channel['channel'], channel['max_val']))
        print('The timing mode is set to {} samples.'.format('continuous' if self.continuous_sampling else 'finite'))
        print('The base clock is {}.'.format('external' if self.import_clock else 'internal ({})'.format(self._clock_channel)))
            
        
    def start(self, npoints=None):
        print('Starting input task...')
        if self._import_clock:
            self._task.timing.master_timebase_src=self._clock_channel
            self._task.timing.master_timebase_rate = 20000000
        
    def read(self, npoints, timeout=120):
        self._timing(npoints)
        data = self._task.read(npoints)
        self._task.wait_until_done(timeout=timeout)
        print('Input task finished.')
        return data
        
    def stop(self):
        print('Input task stopped.')
        self._task.stop()
        
    def close(self):
        self._task.close()
        
    def reset(self):
        nidaqmx.system.device.Device(self.device_name).reset_device()
