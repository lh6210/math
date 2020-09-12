


###################################################################
# In this file, explore exp function and its Taylor series
###################################################################

from math import pow, sin, pi, factorial, exp
import matplotlib.ticker as tck
from math import factorial as fact
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
#ax.set_title(r'$Taylor_{9}(sin, x \in V_{\epsilon}(0))$ vs $sin(\theta)$')

# method 1 to set ticks
#start, end = -3*pi, 3*pi
#ax.set_xlim(start, end)
#ax.xaxis.set_major_locator(tck.MultipleLocator(np.pi / 2))

# method 2 to set ticks
#ax.set_xticks(np.arange(-3*np.pi, 3*np.pi, np.pi/2))
#ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
ax.set_xlim(-3, 6)
ax.set_ylim(-10, 100)

#def format_func(value, tick_number):
#    # find number of multiples of pi/2
#    N = int(np.round(2 * value / np.pi))
#    if N == 0:
#        return "0"
#    elif N == 1:
#        return r"$\pi/2$"
#    elif N == 2:
#        return r"$\pi$"
#    elif N % 2 > 0:
#        return r"${0}\pi/2$".format(N)
#    else:
#        return r"${0}\pi$".format(N // 2)
#
#ax.xaxis.set_major_formatter(tck.FuncFormatter(format_func))

def taylor_exp(x, n):
    if n == 0:
        return 1
    else:
        return taylor_exp(x, n - 1) + pow(x, n) / factorial(n)


mx = np.linspace(-3, 6, 200)
y0x = [exp(x) for x in mx]
y1x = [taylor_exp(x, 3) for x in mx]
y2x = [taylor_exp(x, 7) for x in mx]

# x-axis
ax.arrow(-3, 0, 9, 0, length_includes_head=True, head_width=1.3, head_length= 0.3, color='xkcd:almost black'  )
ax.arrow(0, -10, 0, 110, length_includes_head=True, head_width= 0.1, head_length = 3, color='xkcd:almost black')
ax.plot(mx, y0x, color='xkcd:bluish purple')
ax.plot(mx, y1x, color='xkcd:teal')
ax.plot(mx, y2x, color='xkcd:dark pink')

plt.show()
#plt.draw()
#loc = ax.get_xticks()
#lab = ax.get_xmajorticklabels()
