from math import pow, sin, pi
from math import factorial as fact
import matplotlib.pyplot as plt 
import numpy as np 


fig, ax = plt.subplots()
ax.set_title(r'$Taylor_{9}(sin, x \in V_{\epsilon}(0))$ vs $sin(\theta)$')


start, end = -2.5*pi, 2.5*pi
stepsize = pi / 4
ax.set_xlim(start, end)
#ax.xticks(np.arange(-2.5*pi, 2.5*pi, pi/4))
#ax.xaxis.set_ticks(np.arange(start, end, stepsize))
ax.xaxis.set_major_locator(plt.MultipleLocator(pi / 4))
ax.yaxis.set_major_locator(plt.NullLocator())
ax.set_ylim(-5, 5)

def taylor_sin(x):
    return x - pow(x, 3)/ fact(3) + pow(x, 5)/fact(5) - pow(x, 7)/fact(7) + pow(x, 9) / fact(9)

mx = np.linspace(-2*pi, 2* pi, 200)
y1x = [taylor_sin(x) for x in mx]
#y1x = taylor_sin(mx)
y2x = [sin(x) for x in mx]

ax.plot([-3*pi, 0, 3*pi], [0, 0, 0])
ax.plot(mx, y1x)
ax.plot(mx, y2x)

plt.show()

