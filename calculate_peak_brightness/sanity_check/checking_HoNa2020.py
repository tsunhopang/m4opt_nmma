import numpy as np
import matplotlib
matplotlib.use('agg')
matplotlib.rcParams.update(
    {'font.size': 16,
     'text.usetex': True,
     'font.family': 'Times New Roman'}
)
import matplotlib.pyplot as plt
from nmma.em.utils import lightcurve_HoNa

# setting parameters the same as Fig. 8 in https://iopscience.iop.org/article/10.3847/1538-4357/ab6a98/pdf
mass = 0.05
vej = [0.1, 0.2, 0.4]
opa = [3, 0.5]
n = 4.5
t = np.logspace(-1, 2, num=50)

L, T, _ = lightcurve_HoNa(t, mass, vej, opa, n)

plt.figure(1)
plt.xlabel('Time (day)')
plt.ylabel(r'$L_{\rm bol} \ [{\rm erg} / {\rm s}]$')
plt.loglog(t, L)
plt.xlim(1e-1, 1e2)
plt.ylim([2e38, 1e43])
plt.savefig('Lbol_check.pdf', bbox_inches='tight')

plt.figure(2)
plt.xlabel('Time (day)')
plt.ylabel(r'$T \ [{\rm K}]$')
plt.loglog(t, T)
plt.xlim(1e-1, 1e2)
plt.ylim([1e3, 2e4])
plt.savefig('T_check.pdf', bbox_inches='tight')
