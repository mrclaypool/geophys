#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:59:40 2023

@author: mirandaclaypool

Note: this is adapted from the Obspy tutorial on writing an inventory
"""

import obspy
from obspy.core.inventory import Inventory, Network, Station, Channel, Site


# We'll first create all the various objects. These strongly follow the
# hierarchy of StationXML files.
inv = Inventory(
    # We'll add networks later.
    networks=[],
    # The source should be the id whoever create the file.
    source="ObsPy-Tutorial")

net = Network(
    # This is the network code according to the SEED standard.
    code="PO",
    # A list of stations. We'll add one later.
    stations=[],
    description="A test stations.",
    # Start-and end dates are optional.
    start_date=obspy.UTCDateTime(2021, 9, 1))

sta = Station(
    # This is the station code according to the SEED standard.
    code="POCB",
    latitude=19.056547,
    longitude=-98.637405,
    elevation=3599.99,
    creation_date=obspy.UTCDateTime(2021, 9, 1),
    site=Site(name="First station"))

chae = Channel(
    # This is the channel code according to the SEED standard.
    code="BHE",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=100,
    elevation=345.0,
    depth=10.0,)

chan = Channel(
    # This is the channel code according to the SEED standard.
    code="BHN",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=100,
    elevation=345.0,
    depth=10.0,)

chaz = Channel(
    # This is the channel code according to the SEED standard.
    code="BHZ",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=100,
    elevation=345.0,
    depth=10.0,)

chaf = Channel(
    # This is the channel code according to the SEED standard.
    code="HDF",
    # This is the location code according to the SEED standard.
    location_code="01",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=400,
    elevation=345.0,
    depth=10.0,)

#this is for reading the response info from the other deployment's inv
inv2=obspy.read_inventory('fdsn-station_2023-12-03T22_08_44.6050.xml')
charesp=inv2[0][0][0]
resp=charesp.response

channels=[chae,chan,chaz,chaf]
# Now tie it all together.

for i in channels:
    sta.channels.append(i)
    i.response=resp
net.stations.append(sta)
inv.networks.append(net)


# And finally write it to a StationXML file. We also force a validation against
# the StationXML schema to ensure it produces a valid StationXML file.
#
# Note that it is also possible to serialize to any of the other inventory
# output formats ObsPy supports.
inv.write("popoinv.xml", format="stationxml", validate=True)