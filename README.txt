plot_radiance.py is the primary file here. It will make a nice printable page of plots of 
CTD (conductivity, temperature, depth, O2 %age) from the ship's big CTD rig, and radiometry
from the smaller hand-deployed Satlantic instrument.

The raw data recorded by the Satlantic instruments is run through a file called ProSoft to
create 4 levels of HDF4 files. 


Depends on:
numpy
scipy
matplotlib
pyhdf