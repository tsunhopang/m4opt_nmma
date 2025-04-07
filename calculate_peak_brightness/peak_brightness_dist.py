import sys
import numpy as np
import glob
import matplotlib
matplotlib.use("agg")
matplotlib.rcParams.update(
    {'font.size': 16,
     'text.usetex': True,
     'font.family': 'Times New Roman'}
)
import matplotlib.pyplot as plt

def count_given_limit(x, lim):
    return len(np.where(x < lim)[0])

label = str(sys.argv[1])
nbins = int(sys.argv[2])
lc_files = glob.glob(f'./outdir_{label}/lc_*.dat')

peak_brightness_FUV = []
peak_brightness_NUV = []
for lc_file in lc_files:
    t, mag_FUV, mag_NUV = np.loadtxt(lc_file, usecols=[0, 1, 2], unpack=True)
    peak_brightness_FUV.append(np.amin(mag_FUV))
    peak_brightness_NUV.append(np.amin(mag_NUV))
peak_brightness_FUV = np.array(peak_brightness_FUV)
peak_brightness_NUV = np.array(peak_brightness_NUV)

plt.figure(1)
plt.xlabel('Peak brightness magnitude ' + r'$m_{\rm{AB}}$')
plt.ylabel('Count')
bins = np.linspace(
    min(np.amin(peak_brightness_FUV), np.amin(peak_brightness_NUV)),
    max(np.amax(peak_brightness_FUV), np.amax(peak_brightness_NUV)),
    nbins
)
plt.hist(peak_brightness_FUV, bins=bins, histtype='step', color='C0', label='FUV')
plt.hist(peak_brightness_NUV, bins=bins, histtype='step', color='C1', label='NUV')
#plt.axvline(26, label=r'$m_{\rm AB} = 26$', color='k', linestyle='--')
#plt.axvline(24, label=r'$m_{\rm AB} = 24$', color='k', linestyle='-.')
plt.legend()
plt.savefig(f'peak_brightness_hist_{label}.pdf', bbox_inches='tight')

#print(f"In filter NUV, out of {len(peak_brightness_NUV)} events, {count_given_limit(peak_brightness_NUV, 24)} is brighter than mag of 24 and {count_given_limit(peak_brightness_NUV, 26)} is brighter than mag of 26")
#print(f"In filter FUV, out of {len(peak_brightness_FUV)} events, {count_given_limit(peak_brightness_FUV, 24)} is brighter than mag of 24 and {count_given_limit(peak_brightness_FUV, 26)} is brighter than mag of 26")
