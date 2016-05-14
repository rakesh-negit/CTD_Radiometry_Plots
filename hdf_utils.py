# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:35:54 2016

@author: tcdod
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['svg.fonttype'] = 'none'

from pyhdf.HDF import *
from pyhdf.V   import *
from pyhdf.VS  import *
from pyhdf.SD  import *

def read_radiances_etc(inputfile):
    wavelengths = []
    depth = []
    downwelling_downcast = []
    downwelling_upcast = []
    upwelling_downcast = []
    upwelling_upcast = []

    # open the hdf file read-only
    # Initialize the SD, V and VS interfaces on the file.
    hdf = HDF(inputfile)
    vs = hdf.vstart()
    v  = hdf.vgstart()

    # Attach and read the contents of the Profiler vgroup

    vg = v.attach(v.find('Profiler'))

    for tag, ref in vg.tagrefs():
        assert(tag == HC.DFTAG_VH)
        vd = vs.attach(ref)
        nrecs, intmode, fields, size, name = vd.inquire()

        if name == "ED_hyperspectral_downcast":
            x = vd.read(nrecs)
            downwelling_downcast = np.asarray([i[3:] for i in x])
            wavelengths = np.asarray([float(x) for x in fields[3:]])
            depth = np.asarray([i[2] for i in x])
        elif name == "ED_hyperspectral_upcast":
            downwelling_upcast = np.asarray([i[3:] for i in vd.read(nrecs)])
        elif name == "LU_hyperspectral_downcast":
            upwelling_downcast = np.asarray([i[3:] for i in vd.read(nrecs)])
        elif name == "LU_hyperspectral_upcast":
            upwelling_upcast = np.asarray([i[3:] for i in vd.read(nrecs)])

        vd.detach()

    # Close vgroup
    vg.detach()

    #clean up
    v.end()
    vs.end()
    hdf.close()

    return wavelengths, depth, downwelling_downcast, downwelling_upcast, \
            upwelling_downcast, upwelling_upcast

def scan_all_vgroups(v,vs,sd):
    ref = -1
    while 1:
        try:
            ref = v.getid(ref)
        except HDF4Error as msg:    # no more vgroup
            break
        describevg(ref,v,vs,sd)

def describevg(refnum,v,vs,sds):

    # Describe the vgroup with the given refnum.

    # Open vgroup in read mode.
    vg = v.attach(refnum)
    print("----------------")
    print("name:", vg._name, "class:",vg._class, "tag,ref:", end=' ')
    print(vg._tag, vg._refnum)

    # Show the number of members of each main object type.
    print("members: ", vg._nmembers, end=' ')
    print("datasets:", vg.nrefs(HC.DFTAG_NDG), end=' ')
    print("vdatas:  ", vg.nrefs(HC.DFTAG_VH), end=' ')
    print("vgroups: ", vg.nrefs(HC.DFTAG_VG))

    # Read the contents of the vgroup.
    members = vg.tagrefs()

    # Display info about each member.
    index = -1
    for tag, ref in members:
        index += 1
        print("member index", index)
        # Vdata tag
        if tag == HC.DFTAG_VH:
            vd = vs.attach(ref)
            nrecs, intmode, fields, size, name = vd.inquire()
            print("  vdata:",name, "tag,ref:",tag, ref)
            print("    fields:",fields)
            print("    nrecs:",nrecs)
            vd.detach()

        # SDS tag
        elif tag == HC.DFTAG_NDG:
            sds = sd.select(sd.reftoindex(ref))
            name, rank, dims, type, nattrs = sds.info()
            print("  dataset:",name, "tag,ref:", tag, ref)
            print("    dims:",dims)
            print("    type:",type)
            sds.endaccess()

        # VS tag
        elif tag == HC.DFTAG_VG:
            vg0 = v.attach(ref)
            print("  vgroup:", vg0._name, "tag,ref:", tag, ref)
            vg0.detach()

        # Unhandled tag
        else:
            print("unhandled tag,ref",tag,ref)

    # Close vgroup
    vg.detach()
	