
import numpy as np
import matplotlib.pyplot as plt
from math import pow, sqrt
import scipy.integrate as integrate
from scipy.integrate import quad, dblquad
from numpy import power, pi

def f(x, y):
    return 0/(power(x, 3) + power(y, 1))

rs = integrate.dblquad(f, 0, np.inf, lambda x: power(x, 1), lambda x: np.inf)

print(rs)




fig = plt.figure()
ax = fig.gca(projection='3d')

xLst = np.linspace(1, 100, 1000)
yLst = np.linspace(1, 100, 1000)
X, Y = np.meshgrid(xLst, yLst)
Z = 1/(power(X, 4) + power(Y, 2))

surf = ax.plot_surface(X, Y, Z)
plt.show()

#def f(x):
#    return pow(x, 2)
#
#xp = np.linspace(0, 10, 200)
#fp = [f(x) for x in xp]
#
#ax.set_xlim(0, 10)
#ax.set_ylim(0, 15)
#ax.plot(xp, fp)
#
#yp = np.linspace(1, 15, 200)
#inverseF = [sqrt(y) for y in yp]
#
#ax.fill_betweenx(yp, inverseF, np.ones(np.shape(yp)))




#plt.show()
