import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import rc

rc('font', **{'family': 'sans-serif', 'sans-serif': ['Arial']})
rc('text', usetex=False)

expdat1 = np.load('20201201-neg-u-12Er-vary_holdtime.npz', allow_pickle = True)
expdat2 = np.load('20201201-neg-u-9Er-vary_holdtime.npz', allow_pickle = True)
simdat = np.load('spdf-11-1m1-pair-vary-hold-lattice-8-to-20Er.npz', allow_pickle = True)

V0se1, spdfse1, spdferr1, _, _ = [expdat1[x] for x in expdat1]
V0se2, spdfse2, spdferr2, _, _ = [expdat2[x] for x in expdat2]
V0ss, timess, spdfss = [simdat[x] for x in simdat]

fig, ax = plt.subplots(figsize = (3.4, 2.5))
ax.errorbar(V0se1[0], spdfse1[0], spdferr1[0], marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'k')
ax.errorbar(V0se2[0], spdfse2[0], spdferr2[0], marker = 's', ls = 'none', ms = 3, elinewidth = 0.5, color = 'C0')

lattice = 12.
ind = np.argmin(np.abs( V0ss - lattice ))
dat1 = spdfss[ind]
dat2 = np.exp(-timess[0] / 100) * (np.array(dat1) - 1/3) + 1/3
ax.plot(timess[0], dat2, color = 'k', label = '$12 E_r$', lw = 1)
ax.plot(timess[0], dat1, color = 'k', lw = 0.5, ls = (0, (10, 10)))

lattice = 9.
ind = np.argmin(np.abs( V0ss - lattice ))
dat1 = spdfss[ind]
dat2 = np.exp(-timess[0] / 100) * (np.array(dat1) - 1/3) + 1/3

ax.plot(timess[0], dat2, color = 'C0', label = '$9 E_r$', lw = 1)
ax.plot(timess[0], dat1, color = 'C0', ls = (0, (10, 10)), lw = 0.5)

ax.set_xlim([-10, 210])
ax.set_ylim([0.16, 0.54])
ax.set_yticks( np.arange(0.2, 0.6, 0.1) )
ax.legend(fontsize = 8, loc = 'upper right')

ax.set_xlabel("Time (ms)", fontsize = 10)
ax.set_ylabel("SPDF", fontsize = 10)
#ax.set_title("$u < 0$", fontsize = 10)
ax.tick_params(labelsize = 8)
axstroke = 0.5
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(axstroke)

# at = AnchoredText("$D/J < 0$",
#                   prop=dict(size=8), frameon=True,
#                   loc='upper right',
#                   )
# at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
# at.patch.set_facecolor([1., 1., 1., 0.6])
# at.patch.set_linewidth(0.5)
# ax.add_artist(at)

plt.tight_layout()

# Set position such that the axes align vertically with those in the u > 0 figure
#pos = ax.get_position()
#ax.set_position([0.1867, pos.y0, 0.7692, pos.height])

fname = "negative-u-scan-hold-time"
plt.savefig(fname + ".pdf")
#plt.savefig(fname + ".png")