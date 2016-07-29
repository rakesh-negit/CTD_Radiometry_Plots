# -*- coding: utf-8 -*-
"""
Created on Fri May 13 15:46:48 2016

@author: tcdod
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams['svg.fonttype'] = 'none'

from hdf_utils import *

# convert uW/cm^2 to umol/(m^2*s)
def convert(y, wavelengths):
    hc = 6.626e-34 * 3e8;
    Na = 6.02e23;

    # factor of 1e6 to convert uW to W
    # factor of 100^2 to go from 1/cm^2 to 1/m^2
    return  y * wavelengths / (1e5 * hc * Na)

inputfile=r'test_data\01May2016\001AB_L2s.hdf'

wavelengths, depth, downwelling_downcast, downwelling_upcast, \
    upwelling_downcast, upwelling_upcast = read_radiances_etc(inputfile)

# convert units
# plot upwelling and downwelling at/near depth=0
# merge upcast and downcast somewhere
# plot the attenuation as a function of depth with contourf (divide each row
#   by the max of that row)

plt.figure()
plt.contourf(wavelengths,depth,downwelling_downcast)

plt.figure()
plt.contourf(wavelengths,depth,downwelling_upcast)
