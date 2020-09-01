

from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

xv = np.arange(4)
yv = np.exp(xv)

fig, ax = plt.subplots()
plt.plot(xv,yv,'--o')

#st = '2'
#st1 = '3'
##ax.set_title(r"$\frac{{0}}{{1}}$".format(st, st1))
#ax.set_title(r"$\frac{{1\pi}}{{0}}$".format(st, st1))



plt.show()
