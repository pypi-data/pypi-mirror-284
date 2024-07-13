# Durham Spintronics Group
A collection of instrument control and analysis tools for the Spintronics group at Durham University.

## Installation
Currently, this package is only installable using ```pip```. You can still install this pacakge within the anaconda environment, however, you must use ```pip install```, not ```conda install```.
```
pip install durhamspintronics
```
Once installed, there are several differnt sub-modules.

### Instruments
```durhamspintronics.instruments``` 
A variety of class objects, each of which provides a user friendly wrapper for various instruments. The instruments are sorted by manufacturer. Currently included devices:
* ```kepco.BOP``` Kepco BOP power supply (commonly the magnet power supply).
* ```newport.ESP300``` Newport motion controller, model ESP300.
* ```ni.NI_pci6713``` National Instruments analogue output device.
* ```ni.NI_pci6034E``` National Instruments analogue input device.
* ```rohdeandschwarz.ZNLE18_VNA``` Rohde & Schwarz 18 GHz Vector Network Analyser.

### Experiments
```durhamspintronics.experiments``` 
Class objects for the various experiements, such as the sotmoke. These classes combine the aforementioned instrument classes to create one object to control your experiment.
* ```fmr_vna``` Example script for running a frequency sweep measurement on the FMR setup in Ph50.
* ```sotmoke``` Various experiment classes for running hysteresis loops which are field driven, current driven, or a combination of both.

### Data Loaders
```durhamspintronics.dataloader``` 
Class objects for loading the result files from various experiments.
* ```xray.Load_brml``` For use with Bruker D8 .brml files.
* ```deposition.Load_MantisLog``` For use with Mantis Deposition sputtering log files.

### Anaylsis
```durhamspintronics.analysis``` 
Anaylsis methods, sorted by measurement type.
* ```microscope.add_scale_bar()``` Adds a calibrated scale bar to the images taken using the microscope in Ph58.
* ```microscope.reduce_saturation()``` Reduces the image saturation for easier viewing on some projectors/screens.
* ```moke.langevin_singlesweep()``` Modified langevin function for modelling half-hysteresis loops.
* ```moke.langevin_dualshape_singlesweep()``` Extends ```langevin_singlesweep()``` to include two shape parameters for half-hysteresis loops which are antisymmetric immediately above/below the coercive field.
* ```moke.langevin_dualshape()``` Converts ```langevin_dualshape_singlesweep()``` into complete hysteresis loops.
* ```moke.fit_langevin_dualshape()``` Performs a basic ```lmfit``` for a given hysteresis loop.
  
### General
```durhamspintronics.general``` 
An unsorted, yet useful, set of functions.
* ```get_symbols()``` Prints a list of common symbols along which the respective chr() values.
* ```format_uncertainty(value, error)``` Returns a nicely formatted string in the form of "value ± error".
* ```GenerateSampleDiagram``` A tool for quickly generating sample diagrams for presentations and reports.
