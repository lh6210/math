

from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(4)
y = x**2

fig, ax = plt.subplots()
plt.plot(x,y,'--o')

st = '2'
st1 = '3'
#ax.set_title(r"$\frac{{0}}{{1}}$".format(st, st1))
ax.set_title(r"$\frac{{1\pi}}{{0}}$".format(st, st1))



plt.show()
