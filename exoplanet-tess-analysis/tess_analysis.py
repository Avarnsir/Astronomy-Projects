import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import BoxLeastSquares


#search for TESS data 

target = "TOI 700"
search_result = search_tesscut(target)
tpf = search_result.download(cutout_size=(50, 50))
lc = tpf.to_lightcurve().flatten()

#Clean the data
lc_clean = lc.remove_outliners()
lc_norm = lc_clean.normalize()


#Plotting
lc.plot()
lc_norm.scatter()
plt.show()