# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:46:48 2016

@author: tcdod
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pyhdf import SD

matplotlib.rcParams['svg.fonttype'] = 'none'

hdf = SD.SD(r'C:\Users\tcdod\OneDrive\Documents\GitHub\CTD_Radiometry_Plots\test_data\01May2016\001AB_L2s.hdf')
