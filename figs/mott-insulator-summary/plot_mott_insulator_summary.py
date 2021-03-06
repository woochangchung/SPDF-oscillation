import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import csv

fname = 'atomnumber-doublon-statistics-plateau-fractions.csv'
fname_exp = '2020-11-23-neg-u-doublon-statistics-vs-dimple.npz'
    
rawdat_exp = np.load(fname_exp)
dimple_v, spdfs, spdferr, dbls, dblerr, scanvar, dblmode, ncounts_raw = [rawdat_exp[x] for x in rawdat_exp]
NcountToNumberConversion = 145.34 * 1.4 * (2.5 / 2)**2  

atomNumbers = np.zeros_like(dimple_v[0])
for i, xv in enumerate(dimple_v[0]):
    atomNumbers[i] = NcountToNumberConversion * ncounts_raw[np.logical_and(scanvar == xv, dblmode == 1)].mean()

rawdat = []
with open(fname) as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        rawdat.append( [float(r) for r in row] )
        
atomnumber = np.array([r[0] for r in rawdat]) / 1e3
dblstats = np.vstack( [r[1:3] for r in rawdat] )
plateaufracs = np.vstack( [r[3:] for r in rawdat] )

fig, ax = plt.subplots(2, 1, figsize = (3.2, 3), sharex = True)

ax[0].plot(atomnumber, dblstats[:, 0], label = 'Doublon fraction')
#ax[0].plot(atomnumber, dblstats[:, 1], label = 'SPDF')
#ax[0].legend()
ax[0].errorbar(atomNumbers/1e3, dbls[0], dblerr[0], marker = 'o', ls = 'none')

for i in range( plateaufracs.shape[1] ):
    ax[1].plot(atomnumber, plateaufracs[:, i])

ax[1].set_xlabel("Atom number ($10^3$)", fontsize = 10)
ax[1].set_ylabel("Plateau fraction", fontsize = 10)
ax[1].tick_params(labelsize = 8)

ax[0].tick_params(labelsize = 8)
ax[0].set_ylabel("Doublon fraction", fontsize = 10)

xy_1 = (48.1, 0)
xy_2 = (48.1, 0.544)
con = ConnectionPatch(xyA=xy_1, xyB=xy_2, coordsA="data", coordsB="data",  \
                      axesA=ax[1], axesB=ax[0], color="gray", alpha = 0.5, lw = 2, ls = "--")
ax[1].add_artist(con)
ax[1].plot(xy_1[0], xy_1[1], ls = 'none', marker = 'o', ms = 5, color = 'gray', alpha = 0.7)
ax[0].plot(xy_2[0], xy_2[1], ls = 'none', marker = 'o', ms = 5, color = 'gray', alpha = 0.7)
ax[0].hlines(0.544, xmin = -10, xmax = xy_2[0], lw = 2, color = "gray", alpha = 0.5, ls = "--")
ax[0].set_xlim((-5.72, 125.98))


plt.tight_layout()
#plt.savefig("mott-insulator-summary.pdf")