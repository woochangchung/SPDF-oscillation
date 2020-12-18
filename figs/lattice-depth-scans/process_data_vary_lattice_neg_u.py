import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import rc

expdat1 = np.load('20201130-neg-u-hold-25-ms-scan-lattice.npz')
#expdat1 = np.load('20201210-neg-u-hold-25-ms-scan-lattice.npz')
simdat = np.load('spdf-11-1m1-pair-vary-hold-lattice-8-to-20Er.npz')

V0se1, spdfse1, spdferr1, _, _ = [expdat1[x] for x in expdat1]
V0ss, timess, spdfss = [simdat[x] for x in simdat]

fig, ax = plt.subplots(figsize = (3.4, 2.2))
ax.errorbar(V0se1[0], spdfse1[0], spdferr1[0], marker = 'o', ls = 'none', ms = 4)

holdtime = 25.
sel_spdf = np.zeros_like(V0ss)
for i, V0 in enumerate(V0ss):
    ind = np.argmin(np.abs( timess[i] - holdtime ))
    sel_spdf[i] = spdfss[i][ind]

ax.plot(V0ss, sel_spdf, color = 'C0', label = 'Simulation')
#ax.legend(fontsize = 8)

ax.set_xlabel("Lattice depth ($E_r$)", fontsize = 10)
ax.set_ylabel("SPDF", fontsize = 10)
#ax.set_title("35/35/x, hold for 25 ms $(u < 0)$", fontsize = 10)
ax.tick_params(labelsize = 8)


plt.tight_layout()
fname = "negative-u-scan-lattice-depth"
plt.savefig(fname + ".pdf")
plt.savefig(fname + ".png")