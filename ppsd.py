#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:52:52 2023

@author: randaclaypool
"""

from obspy import read, UTCDateTime, read_inventory
from obspy.io.xseed import Parser
from obspy.signal import PPSD

st=read('01/*') #the files used for this ppsd were in a folder labelled 01 for the 1st of sept 2021
st.merge(method=1)
tr=st[3]

inv = read_inventory("popoinv.xml")
ppsd = PPSD(tr.stats, metadata=inv)
ppsd.add(st)
ppsd.plot(xaxis_frequency=True)
 