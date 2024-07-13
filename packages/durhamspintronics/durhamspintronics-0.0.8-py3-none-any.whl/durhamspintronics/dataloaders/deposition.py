# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 10:56:39 2023

@author: Ben Nicholson
"""

from numpy import genfromtxt, zeros

class Load_MantisLog():
    def __init__(self, filename):
        """
        For use with mantis Deposition Log files.
        
        Required arguments:
         filename : File name to load.

        Attributes:
          headers : List of data headers. 
             data : Dictionary containing each data array sorted by the header key.
        """
        
        self.filename = filename
        self._get_header_length()
        self.load_data()
        
    def _get_header_length(self, max_search=20):
        skip_header = 0
        with open(self.filename, mode='r') as f:
            for n in range(max_search):
                line = f.readline()
                skip_header += 1
                if 'Time Stamp' in line:
                    headers = line.strip().split('	')
                    break
            f.close()
        self.skip_header = skip_header
        self.headers = headers
        return self.skip_header
            
    def load_data(self):
        self.raw_data_array = genfromtxt(self.filename, skip_header=self.skip_header, delimiter='\t', encoding='utf-8', dtype='str')
        self.data = {}
        for n, header in enumerate(self.headers):
            # Converts time stamp to seconds, with 0 being the first logged line:
            if header == 'Time Stamp': 
                start_time = float(self.raw_data_array[0,n].split(':')[0])*3600 + float(self.raw_data_array[0,n].split(':')[1])*60 + float(self.raw_data_array[0,n].split(':')[2])
                time_array = zeros(len(self.raw_data_array[:,n]))
                for i in range(1, len(self.raw_data_array[:,n])):
                    time_array[i] = float(self.raw_data_array[i,n].split(':')[0])*3600 + float(self.raw_data_array[i,n].split(':')[1])*60 + float(self.raw_data_array[i,n].split(':')[2])-start_time
                self.data[str(header).strip()] = time_array
            else:
                self.data[str(header).strip()] = self.raw_data_array[:,n]
        return 1
    
    def print_headers(self):
        print('The Available headers are:')
        for n, header in enumerate(self.headers):
            print(f'{n}, "{header}"')
