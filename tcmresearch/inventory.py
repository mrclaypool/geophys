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
    description="Po Network",
    # Start-and end dates are optional.
    start_date=obspy.UTCDateTime(2021, 9, 1))
#%% stations
stacb = Station(
    # This is the station code according to the SEED standard.
    code="POCB",
    latitude=19.056547,
    longitude=-98.637405,
    elevation=4028,
    creation_date=obspy.UTCDateTime(2021, 9, 1),
    site=Site(name="Cruz Blanca"))
staae=Station(
    # This is the station code according to the SEED standard.
    code="POAE",
    latitude=18.88,#done
    longitude=-98.43,
    elevation=1802,
    creation_date=obspy.UTCDateTime(2021, 9, 1),
    site=Site(name="Atlixco"))
stabv=Station(
        # This is the station code according to the SEED standard.
    code="POBV",
    latitude=19.12,
    longitude=-98.58,
    elevation=3310,
    creation_date=obspy.UTCDateTime(2021, 9, 1),
    site=Site(name="Buenavista"))
stasp=Station(
    # This is the station code according to the SEED standard.
    code="POSP",
    latitude=19.08,
    longitude=-98.71,
    elevation=2768,
    creation_date=obspy.UTCDateTime(2021, 9, 1),
    site=Site(name="San Pedro Nexapa"))
stato=Station(
    # This is the station code according to the SEED standard.
    code="POTO",
    latitude=18.89,
    longitude=-98.57,
    elevation=2062,
    creation_date=obspy.UTCDateTime(2021, 9, 1),
    site=Site(name="Tochimilco"))
#%% cb channels
chaecb = Channel(
    # This is the channel code according to the SEED standard.
    code="BHE",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=100,
    elevation=4028,
    depth=10.0,)

chancb = Channel(
    # This is the channel code according to the SEED standard.
    code="BHN",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=100,
    elevation=4028,
    depth=10.0,)

chazcb = Channel(
    # This is the channel code according to the SEED standard.
    code="BHZ",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=100,
    elevation=4028,
    depth=10.0,)

chafcb = Channel(
    # This is the channel code according to the SEED standard.
    code="HDF",
    # This is the location code according to the SEED standard.
    location_code="01",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.056547,
    longitude=-98.637405,
    sample_rate=400,
    elevation=4028,
    depth=10.0,)
#%% bv channels
#done
chaebv = Channel(
    # This is the channel code according to the SEED standard.
    code="BHE",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.12,
    longitude=-98.58,
    sample_rate=100,
    elevation=3310,
    depth=10.0,)

chanbv = Channel(
    # This is the channel code according to the SEED standard.
    code="BHN",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.12,
    longitude=-98.58,
    sample_rate=100,
    elevation=3310,
    depth=10.0,)

chazbv = Channel(
    # This is the channel code according to the SEED standard.
    code="BHZ",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.12,
    longitude=-98.58,
    sample_rate=100,
    elevation=3310,
    depth=10.0,)

chafbv = Channel(
    # This is the channel code according to the SEED standard.
    code="HDF",
    # This is the location code according to the SEED standard.
    location_code="01",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.12,
    longitude=-98.58,
    sample_rate=400,
    elevation=3310,
    depth=10.0,)
#%% ae channels
chaeae = Channel(
    code="BHE",
    location_code="",
    latitude=18.88,
    longitude=-98.43,
    sample_rate=100.0,
    elevation=1802,
    depth=10.0,
    )
chanae = Channel(
    code="BHN",
    location_code="",
    latitude=18.88,
    longitude=-98.43,
    sample_rate=100.0,
    elevation=1802,
    depth=10.0,
    )

chazae = Channel(
    code="BHZ",
    location_code="",
    latitude=18.88,
    longitude=-98.43,
    sample_rate=100.0,
    elevation=1802,
    depth=10.0,
    )

chafae = Channel(
    # This is the channel code according to the SEED standard.
    code="HDF",
    # This is the location code according to the SEED standard.
    location_code="01",
    # Note that these coordinates can differ from the station coordinates.
    latitude=18.88,
    longitude=-98.43,
    sample_rate=200.0,
    elevation=1802,
    depth=10.0,)
#%% sp channels

chaesp = Channel(
    code="BHE",
    location_code="",
    latitude=19.080778,
    longitude=-98.71773,
    sample_rate=100.0,
    elevation=2768,
    depth=10.0,
    )

chansp = Channel(
    code="BHN",
    location_code="",
    latitude=19.080778,
    longitude=-98.71773,
    sample_rate=100.0,
    elevation=2768,
    depth=10.0,
    )

chazsp = Channel(
    code="BHZ",
    location_code="",
    latitude=19.080778,
    longitude=-98.71773,
    sample_rate=100.0,
    elevation=2768,
    depth=10.0,
    )

chafsp = Channel(
    # This is the channel code according to the SEED standard.
    code="HDF",
    # This is the location code according to the SEED standard.
    location_code="01",
    # Note that these coordinates can differ from the station coordinates.
    latitude=19.080778,
    longitude=-98.71773,
    sample_rate=400,
    elevation=2768,
    depth=10.0,)
#%% to channels
chaeto = Channel(
    # This is the channel code according to the SEED standard.
    code="BHE",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=18.89,
    longitude=-98.57,
    sample_rate=100,
    elevation=2062,
    depth=10.0,)

chanto = Channel(
    # This is the channel code according to the SEED standard.
    code="BHN",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=18.89,
    longitude=-98.57,
    sample_rate=100,
    elevation=2062,
    depth=10.0,)

chazto = Channel(
    # This is the channel code according to the SEED standard.
    code="BHZ",
    # This is the location code according to the SEED standard.
    location_code="",
    # Note that these coordinates can differ from the station coordinates.
    latitude=18.89,
    longitude=-98.57,
    sample_rate=100,
    elevation=2062,
    depth=10.0,)

chafto = Channel(
    # This is the channel code according to the SEED standard.
    code="HDF",
    # This is the location code according to the SEED standard.
    location_code="01",
    # Note that these coordinates can differ from the station coordinates.
    latitude=18.89,
    longitude=-98.57,
    sample_rate=200,
    elevation=2062,
    depth=10.0,)

#%% creating inventory
#this is for reading the response info from the other deployment's inv
# inv2=obspy.read_inventory('fdsn-station_2023-12-03T22_08_44.6050.xml')
# charesp=inv2[0][0][0]
# resp=charesp.response

inv_chap=obspy.read_inventory('C:/Users/clayp/Desktop/Popo_data_09152021/chapparaluhp.xml')
charesp_chap=inv_chap[0][0][0]
respch=charesp_chap.response

inv_chap2=obspy.read_inventory('C:/Users/clayp/Desktop/Popo_data_09152021/chapparal60uhp.xml')
charesp_chap60=inv_chap[0][0][0]
respch60=charesp_chap60.response

inv_hyp=obspy.read_inventory('C:/Users/clayp/Desktop/Popo_data_09152021/hyperion.xml')
charesp_hyp=inv_hyp[0][0][0]
resphyp=charesp_hyp.response

inv_trill=obspy.read_inventory('C:/Users/clayp/Desktop/Popo_data_09152021/trillium.xml')
charesp_trill=inv_trill[0][0][0]
resptrill=charesp_trill.response

channelscb=[chaecb,chancb,chazcb,chafcb] #cruz blanca channels
channelsae=[chaeae,chanae,chazae,chafae] #atlixco
channelsbv=[chaebv,chanbv,chazbv,chafbv] #buenavista
channelssp=[chaesp,chansp,chazsp,chafsp] #san perdro nexapa
channelsto=[chaeto,chanto,chazto,chafto] #tochimilco
# Now tie it all together.
stations=[stacb,stabv,staae,stasp,stato]
#CB, BV, AE, chapparal
#TC, SP, hyperion
#cb
for i in channelscb:
    if str(i.code)=='HDF':
        stacb.channels.append(i)
        i.response=respch60
    else:
        stacb.channels.append(i)
        i.response=resptrill
#ae
for i in channelsae:
    if str(i.code)=='HDF':
        staae.channels.append(i)
        i.response=respch60
    else:
        staae.channels.append(i)
        i.response=resptrill
#bv
for i in channelsbv:
    stabv.channels.append(i)
    i.response=respch
#to
for i in channelsto:
    if str(i.code)=='HDF':
        stato.channels.append(i)
        i.response=resphyp
        print('HDF')
    else:
        stato.channels.append(i)
        i.response=resptrill
        print(i)
#sp
for i in channelssp:
    if str(i.code)=='HDF':
        stasp.channels.append(i)
        i.response=resphyp
    else:
        stasp.channels.append(i)
        i.response=resptrill

for i in stations:
    net.stations.append(i)
    
inv.networks.append(net)


# And finally write it to a StationXML file. We also force a validation against
# the StationXML schema to ensure it produces a valid StationXML file.
#
# Note that it is also possible to serialize to any of the other inventory
# output formats ObsPy supports.
inv.write("popoinv.xml", format="stationxml", validate=True)
