

###################################################################
# In this file, xticks' locations and format are implemented.
###################################################################

from math import pow, sin, pi
import matplotlib.ticker as tck
from math import factorial as fact
import matplotlib.pyplot as plt 
import numpy as np 


fig, ax = plt.subplots()
ax.set_title(r'$Taylor_{9}(sin, x \in V_{\epsilon}(0))$ vs $sin(\theta)$')

# method 1 to set ticks
start, end = -3*pi, 3*pi
ax.set_xlim(start, end)
ax.xaxis.set_major_locator(tck.MultipleLocator(np.pi / 2))

# method 2 to set ticks
#ax.set_xticks(np.arange(-3*np.pi, 3*np.pi, np.pi/2))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))

ax.set_ylim(-5, 5)

def format_func(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)

ax.xaxis.set_major_formatter(tck.FuncFormatter(format_func))




def taylor_sin(x):
    return x - pow(x, 3)/ fact(3) + pow(x, 5)/fact(5) - pow(x, 7)/fact(7) + pow(x, 9) / fact(9)

mx = np.linspace(-2*pi, 2* pi, 200)
y1x = [taylor_sin(x) for x in mx]
y2x = [sin(x) for x in mx]

# x-axis
ax.plot([-3*pi, 0, 3*pi], [0, 0, 0])
ax.plot(mx, y1x)
ax.plot(mx, y2x)

plt.show()
#plt.draw()
#loc = ax.get_xticks()
#lab = ax.get_xmajorticklabels()


