# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:25:07 2023

@author: Ben Nicholson
"""

import zipfile
import os
import glob
import xml.etree.ElementTree as ET
import numpy as np




class Load_brml():
    def __init__(self, filename, savetxt=False):
        """
        For use with Bruker D8 .brml files.
        
        Required arguments:
        filename : File name to load.

        Attributes:
           counts : 1D array. X-Ray total counts at each position.
         twotheta : 1D array. Angle (degrees) for TwoTheta.
        """
        
        self.filename = filename

        # Temporary path to extract the files to
        extract_path = os.path.join(os.path.dirname(self.filename),"tempunzip")

        # Extract all RawData*.xml files from the brml file into the tempunzip directory
        with zipfile.ZipFile(self.filename,"r") as brml:
            for info in brml.infolist():
                if ("RawData" in info.filename):
                    brml.extract(info.filename, extract_path)

        # Get the path for the RawData xml files
        data_path = os.path.join(extract_path, "Experiment0","RawData*.xml")
        # In theory, there may be multiple experiments within one brml file. Each experiment will prpduce a seperate RawData*.xml file.
        # This code assumes the final file is the XRR scan (i.e. files 1 to (n-1) are alignment results, file n is the final XRR result).
        file = sorted(glob.glob(data_path), key=self._file_nb)[-1]

        # Parsing XML file
        tree = ET.parse(file)
        root = tree.getroot()

        # Find scanning motors
        scanning_motors = {}
        for chain in (root.findall("./DataRoutes/DataRoute/ScanInformation/ScanAxes/ScanAxisInfo") or root.findall("./ScanInformation/ScanAxes/ScanAxisInfo")):
            scanning_motors[chain.get("AxisName")] = np.arange(float(chain.find("Start").text), 
                                                               float(chain.find("Stop").text)+float(chain.find("Increment").text), 
                                                               float(chain.find("Increment").text))

        # Find static motors
        static_motors = {}
        for chain in root.findall("./FixedInformation/Drives/InfoData"):
            static_motors[chain.get("LogicName")] = chain.find("Position").attrib["Value"]

        # Find X-ray counts
        intensity = []
        for chain in root.findall("./DataRoutes/DataRoute/Datum"):
            intensity.append(int(chain.text.split(',')[-1]))

        if savetxt == True:
            np.savetxt(os.path.join(os.path.dirname(self.filename), os.path.splitext(os.path.basename(self.filename))[0] + r'.txt'), 
                       np.column_stack((scanning_motors["TwoTheta"], intensity)))
        
        #print(os.path.splitext(os.path.basename(file_name))[0])
        
        # Remove extracted files
        os.system('RMDIR "'+ extract_path +'" /s /q')
        
        # Set useful variables, needs expanding to include rocking curves etc
        self.counts = intensity
        self.twotheta = scanning_motors["TwoTheta"]


    def _file_nb(self, path):
        number = int(path.split("RawData")[-1].split(".xml")[0])
        return number
