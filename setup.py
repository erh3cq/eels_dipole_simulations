# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:00:03 2017

@author: Eric Hoglund
"""

from setuptools import setup, find_packages
from os import path
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='eels dipole simulations',
      version='0.1',
      description='Dipole simulations for low-loss electron energy-loss spectroscopy.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/erh3cq/eels_dipole_simulations',
      author='Eric Hoglund',
      author_email='erh3cq@virginia.edu',
      classifiers=['Development Status :: 3 - Alpha'],
      keywords='hyperspy extension EELS',
      license='',
      packages=['eels_dipole_simulations'],
      package_data={'hspy_ext': ['hyperspy_extension.yaml']},
      entry_points={'hyperspy.extensions': 'eels_dipole_simulations = eels_dipole_simulations'},
      zip_safe=False)