#!/usr/bin/env python
#coding:utf-8
import os
from cpsvisualizer import *
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.md')).read()
except:
    README = 'https://github.com/GeoPyTool/CPS-Visualizer/blob/main/README.md'



setup(name='cpsvisualizer',
      version= 1.20240715141111,
      description='Calculation and visualization of CPS (counts per second) for ICPMS scan data.',
      longdescription=README,
      author='Frederic',
      author_email='wedonotuse@outlook.com',
      url='https://github.com/GeoPyTool/CPS-Visualizer',
      packages=['cpsvisualizer'],
      package_data={
          'cpsvisualizer': ['*.py','*.txt','*.png','*.qm','*.ttf','*.ini','*.md'],},
      include_package_data=True,
      install_requires=[
                        'cython',
                        'numpy==1.26.4',
                        'pandas',
                        'scipy',
                        'xlrd',
                        'openpyxl',
                        'matplotlib',
                        "PySide6",
                        "scikit-learn",
                        "scikit-image",
                         ],
     )