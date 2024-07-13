# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:09:11 2024

@author: Ben Nicholson
"""

import setuptools
from os.path import join

version = None
for line in open(join("durhamspintronics", "__init__.py")):
    if "__version__" in line:
        version = line.split('"')[1]

setuptools.setup(
    name="durhamspintronics",
    version=version,
    author="Ben Nicholson",
    author_email="ben.nicholson@durham.ac.uk",
    description="A collection of instrument control and analysis tools for the Spintronics group at Durham University.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ben-Nicholson/durhamspintronics",
    packages=setuptools.find_packages(),
    python_requires = '>=3',
    install_requires = [
            'matplotlib',
            'scipy',
            'numpy',
            'nidaqmx',
            'pyserial',
            'opencv-python',
            'pillow',
    ],
)
