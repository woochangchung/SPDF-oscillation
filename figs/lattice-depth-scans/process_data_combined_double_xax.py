import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from matplotlib import rc
from matplotlib.offsetbox import AnchoredText
import matplotlib.ticker as ticker

#rc('font', **{'family': 'sans serif', 'fontname': 'Consolas'})
rc('font',**{'family': 'sans-serif', 'sans-serif': ['Arial']})
rc('text', usetex=False)

fig, ax = plt.subplots(2, 1, figsize = (3.4, 4), sharex = False)

### Data extraction and plotting
## Positive u plot
expdat1 = np.load('20201210-pos-u-hold-70-ms-scan-lattice.npz', allow_pickle = True)
simdat = np.load('spdf-11-10-pair-vary-hold-lattice-8-to-20Er.npz', allow_pickle = True)

V0se1, spdfse1, spdferr1, _, _ = [expdat1[x] for x in expdat1]
V0ss, timess, spdfss = [simdat[x] for x in simdat]

keepPoints = (V0ss >= 8)
V0ss = V0ss[keepPoints]
timess = timess[keepPoints]
spdfss = spdfss[keepPoints]

rmPoints = np.logical_not(V0se1[0] < 8.5)
V0se1 = V0se1[0][rmPoints]
spdfse1 = spdfse1[0][rmPoints]
spdferr1 = spdferr1[0][rmPoints]

ax[0].errorbar(V0se1, spdfse1, spdferr1, marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'k')

holdtime = 70.
sel_spdf = np.zeros_like(V0ss)
for i, V0 in enumerate(V0ss):
    ind = np.argmin(np.abs( timess[i] - holdtime ))
    sel_spdf[i] = spdfss[i][ind]

ax[0].plot(V0ss, sel_spdf, color = 'k', label = 'Simulation', lw = 0.8)

## Negative u plot
expdat1 = np.load('20201130-neg-u-hold-25-ms-scan-lattice.npz', allow_pickle = True)
#expdat1 = np.load('20201210-neg-u-hold-25-ms-scan-lattice.npz')
simdat = np.load('spdf-11-1m1-pair-vary-hold-lattice-8-to-20Er.npz', allow_pickle = True)

V0se1, spdfse1, spdferr1, _, _ = [expdat1[x] for x in expdat1]
V0ss, timess, spdfss = [simdat[x] for x in simdat]

ax[1].errorbar(V0se1[0], spdfse1[0], spdferr1[0], marker = 'o', ls = 'none', ms = 3, elinewidth = 0.5, color = 'k')

holdtime = 25.
sel_spdf = np.zeros_like(V0ss)
for i, V0 in enumerate(V0ss):
    ind = np.argmin(np.abs( timess[i] - holdtime ))
    sel_spdf[i] = spdfss[i][ind]

ax[1].plot(V0ss, sel_spdf, color = 'k', label = 'Simulation', lw = 0.8)


### Plot formatting
ax[0].set_xlim([7.5, 20.5])
#ax[0].set_xlabel("Lattice depth ($E_R$)")
ax[0].set_ylabel("SPDF", fontsize = 10)
ax[0].tick_params(labelsize = 8)
ax[0].set_ylim([0.43, 0.74])
ax[0].set_xticks([8, 12, 16, 20])
ax[0].xaxis.set_minor_locator(ticker.AutoLocator())

# at = AnchoredText("$|ab\\rangle = |1,-1\\rangle|1,0\\rangle$",
#                   prop=dict(size=8), frameon=True,
#                   loc='upper left',
#                   )
# at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
# at.patch.set_facecolor([1., 1., 1., 0.6])
# at.patch.set_linewidth(0.5)
# ax[0].add_artist(at)


ax[1].set_xlim([7.5, 20.5])
ax[1].set_xlabel("Lattice depth ($E_R$)")
ax[1].set_ylabel("SPDF", fontsize = 10)
ax[1].tick_params(labelsize = 8)
ax[1].set_ylim([0.21, 0.55])
ax[1].set_xticks([8, 12, 16, 20])
ax[1].xaxis.set_minor_locator(ticker.AutoLocator())

# at = AnchoredText("$|ab\\rangle = |1,-1\\rangle|1,1\\rangle$",
#                   prop=dict(size=8), frameon=True,
#                   loc='upper left',
#                   )
# at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
# at.patch.set_facecolor([1., 1., 1., 0.6])
# at.patch.set_linewidth(0.5)
# ax[1].add_artist(at)

## Adjust axes positions
apos0 = ax[0].get_position()
newpos = [apos0.x0, apos0.y0 + 0.05, apos0.width, apos0.height]
#ax[0].set_position(newpos)

### Add D/J axes
def tick_formatter(val):
    if np.abs(val) < 1.:
        return "%.1f" % val
    else:
        return "%.0f" % val

lat_params = np.load('generic-lattice-parameters.npz')
[V0, ts, Us] = [lat_params[x] for x in lat_params]

# Positive D-pair
UAA = Us * (100.4 + 100.867) / 2. / 100.
UAB = Us * 100.4 / 100.
Js = 4*ts**2 / UAB
Ds = UAA - UAB

interpfun = interp1d(Ds/Js, V0)

ax2 = ax[0].twiny()
ax2.tick_params(labelsize = 8)
ax2.set_xlim([7.5, 20.5])

newticks = np.array([0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0])
#newticks = np.array([0.1, 0.5, 1.0, 5.0, 10.])
newtickpositions = interpfun(newticks)
ax2.set_xticks(newtickpositions)
ax2.set_xticklabels([tick_formatter(tick) for tick in newticks])
ax2.set_xlabel("$D/J$", fontsize = 10)

# Negative D-pair
UAA = Us * 100.4 / 100.
UAB = Us * 101.333 / 100.
Js = 4*ts**2 / UAB
Ds = UAA - UAB

interpfun = interp1d(Ds/Js, V0)

ax3 = ax[1].twiny()
ax3.tick_params(labelsize = 8)
ax3.set_xlim([7.5, 20.5])

axstroke = 0.5
for axis in ['top','bottom','left','right']:
    ax[0].spines[axis].set_linewidth(axstroke)
    ax[1].spines[axis].set_linewidth(axstroke)
    ax2.spines[axis].set_linewidth(axstroke)
    ax3.spines[axis].set_linewidth(axstroke)

newticks = np.array([-0.5, -1, -2, -5, -10, -20, -50, -100])
#newticks = np.array([-0.5, -1, -5, -10, -50, -100])
#newticks = np.array([-1, -2, -10, -20, -100])
newtickpositions = interpfun(newticks)
ax3.set_xticks(newtickpositions)
ax3.set_xticklabels([tick_formatter(tick) for tick in newticks])
#ax3.set_xticklabels(["$-10^1$", "$-10^2$", "$-10^3$"])
#ax3.set_xlabel("$D/J$", fontsize = 10)

plt.tight_layout()
fname = "scan-lattice-depth-combined-double-axis"
plt.savefig(fname + ".pdf")
#plt.savefig(fname + ".png")