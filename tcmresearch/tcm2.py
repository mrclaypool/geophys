import numpy as np
from obspy import read, UTCDateTime, read_inventory
from obspy.clients.fdsn import Client
from tcm import tcm
from tcm.tools import plotting
from matplotlib import rcParams, pyplot as plt
from obspy.signal.trigger import ar_pick
# %%
rcParams.update({'font.size': 10})
filename='POCBpoint5to20'

# Filter range [Hz]
freq_min = 0.5
freq_max = 20

# Use 2 Hz narrowband [True] or broadband [False] coherence maxima for calculation
search_2Hz = False

# Window length [sec]
window_length = 15.0

# Fraction of window overlap [0.0, 1.0)
window_overlap = 0.90

# Azimuths to scans over [degrees]
az_min = 0
az_max = 359.0
az_delta = 1


# %% Read in data and pre-process

inv = read_inventory('popoinv.xml')
st = read('C:/Users/clayp/Desktop/Popo_data_09152021/PopoData_20210926/POCB/*')
st.merge(method='1')
st2 = read('C:/Users/clayp/Desktop/Popo_data_09152021/PopoData_20210926/PICB/*')
st2.merge(method='1')
st.append(st2[0])

st.attach_response(inv)
print(st)
st.merge(method='1')
# st=st1.splice() use this if you
st.split()  # if there are gaps then you can use this to break it up into different streams

for i in st:
    if str(i.stats.channel)=='HDF':
        print('hi')
        continue
    else:
        print('bye')
        i.integrate(method='cumtrapz')

# Sort by component: E, F, N, Z
st.sort(keys=['component'])
# st = st.slice(UTCDateTime("2021-09-15T11:00:00"),
              # UTCDateTime("2021-09-15T12:00:00"))
st2 = st.copy()
# st.filter('highpass', freq=5)

# %% find area of interest
# tr1=st[3] #should be z
# tr2=st[2] #n
# tr3=st[0] #e
# df = tr1.stats.sampling_rate
# p_pick, s_pick = ar_pick(tr1.data, tr2.data, tr3.data, df, 1, 30.0, 1.0, 0.1, 4.0, 1.0, 2, 8, 0.1, 0.2)

# print(p_pick,s_pick)
# ti = UTCDateTime("2021-09-15T11:00:00")+s_pick

ti = UTCDateTime('2021-09-26 11:19:00')
print(ti)
# time = UTCDateTime("2021-09-15T00:53:00")
tupper = ti+120
tlower = ti-30

st.slice(tlower, tupper)
#Remove response
# for tr in st:
#     fs_resp = tr.stats.sampling_rate
#     # Pre-filt for response removal
#     pre_filt = [0.0005, 0.001, fs_resp/2-2, fs_resp/2]
#     if tr.stats.channel[1:] == 'DF':
#         tr.remove_response(inventory = inv, pre_filt=pre_filt, output='VEL', water_level=None)
#     else:
#         tr.remove_response(inventory = inv, pre_filt=pre_filt, output='DISP', water_level=None)


st.interpolate(sampling_rate=st[0].stats.sampling_rate, method='lanczos', a=15)
st.detrend(type='linear')
st = st.slice(tlower, tupper)
print(st)
# %% Run the transverse coherence minimization (TCM) algorithm
baz, sigma, time_smooth, frequency_vector, time, Cxy2, mean_coherence, freq_lim_min, freq_lim_max = tcm.run_tcm(st, freq_min, freq_max, window_length, window_overlap, az_min, az_max, az_delta, search_2Hz)  # noqa

# %% Plot the results
fig, axs = plotting.tcm_plot(st, freq_min, freq_max, baz,
                             time_smooth, frequency_vector, time,
                             Cxy2, mean_coherence, freq_lim_min, freq_lim_max,
                             search_2Hz)
# Plot uncertainties
thresh=0.90*np.average(mean_coherence)
bad=np.where(mean_coherence<thresh)
print(bad)
filt=np.ones(len(mean_coherence), dtype=bool)
filt[[bad]]=False
print(filt)

axs[4].scatter(time_smooth[filt], baz[filt] + sigma[filt], c='gray', marker='_', linestyle=':')
axs[4].scatter(time_smooth[filt], baz[filt] - sigma[filt], c='gray', marker='_', linestyle=':')
plt.savefig(str(filename)+'.pdf', format='pdf')
print(baz)
print(np.average(baz))
print(np.average(sigma))
print(mean_coherence)
print(np.average(mean_coherence))
