import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import rc

#rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
rc('font', **{'family': 'serif'})
rc('text', usetex=True)

expdat1 = np.load('20201201-neg-u-12Er-vary_holdtime.npz')
expdat2 = np.load('20201201-neg-u-9Er-vary_holdtime.npz')
simdat = np.load('spdf-11-1m1-pair-vary-hold-lattice-8-to-20Er.npz')

V0se1, spdfse1, spdferr1, _, _ = [expdat1[x] for x in expdat1]
V0se2, spdfse2, spdferr2, _, _ = [expdat2[x] for x in expdat2]
V0ss, timess, spdfss = [simdat[x] for x in simdat]

fig, ax = plt.subplots(figsize = (3.4, 3))
ax.errorbar(V0se1[0], spdfse1[0], spdferr1[0], marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'k')
ax.errorbar(V0se2[0], spdfse2[0], spdferr2[0], marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'gray')

lattice = 12.
ind = np.argmin(np.abs( V0ss - lattice ))
dat1 = spdfss[ind]
dat2 = np.exp(-timess[0] / 100) * (np.array(dat1) - 1/3) + 1/3
ax.plot(timess[0], dat2, color = 'k', label = '$12 E_r$', lw = 1)
ax.plot(timess[0], dat1, color = 'k', lw = 1, ls = ':')

lattice = 9.
ind = np.argmin(np.abs( V0ss - lattice ))
dat1 = spdfss[ind]
dat2 = np.exp(-timess[0] / 100) * (np.array(dat1) - 1/3) + 1/3

ax.plot(timess[0], dat2, color = 'gray', label = '$9 E_r$', lw = 1)
ax.plot(timess[0], dat1, color = 'gray', ls = ':', lw = 1)

ax.set_xlim([-2, 202])

## INSET PLOT
ax.set_ylim([0.12, 0.7])
ax.legend(fontsize = 8, loc = 'lower right')
axins = ax.inset_axes([0.5, 0.5, 0.47, 0.47])
axins.set_xticklabels('')
axins.set_yticklabels('')

axins.errorbar(V0se1[0], spdfse1[0], spdferr1[0], marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'k')
axins.errorbar(V0se2[0], spdfse2[0], spdferr2[0], marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'gray')

lattice = 12.
ind = np.argmin(np.abs( V0ss - lattice ))
dat1 = spdfss[ind]
dat2 = np.exp(-timess[0] / 100) * (np.array(dat1) - 1/3) + 1/3
axins.plot(timess[0], dat2, color = 'k', label = '$12 E_r$', lw = 1)
axins.plot(timess[0], dat1, color = 'k', ls = ':', lw = 1)

lattice = 9.
ind = np.argmin(np.abs( V0ss - lattice ))
dat1 = spdfss[ind]
dat2 = np.exp(-timess[0] / 100) * (np.array(dat1) - 1/3) + 1/3

axins.plot(timess[0], dat2, color = 'gray', label = '$9 E_r$', lw = 1)
axins.plot(timess[0], dat1, color = 'gray', ls = ':', lw = 1)
axins.set_facecolor([0.98, 0.98, 0.98])

axins.set_xlim([0, 45])
axins.set_ylim([0.22, 0.54])
ax.indicate_inset_zoom(axins)

## END INSET PLOT

ax.set_xlabel("Time (ms)", fontsize = 10)
ax.set_ylabel("SPDF", fontsize = 10)
ax.set_title("$u < 0$", fontsize = 10)
ax.tick_params(labelsize = 8)

ax.set_facecolor([0.98, 0.98, 0.98])

plt.tight_layout()

# Set position such that the axes align vertically with those in the u > 0 figure
pos = ax.get_position()
ax.set_position([0.2024, pos.y0, 0.7535, pos.height])

fname = "negative-u-scan-hold-time"
plt.savefig(fname + ".pdf")
#plt.savefig(fname + ".png")