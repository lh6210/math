

######################################################################
# This file simulates how the computer calculates sin(x)
# Aug 31, 2020
######################################################################


import matplotlib.pyplot as plt
import numpy as np
from math import pi 
import matplotlib.ticker as tck
from math import factorial as fact


# figure and axes set-up
######################################################################
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

# x, y limit
ax.set_xlim(-3 * pi, 6 * pi)
ax.set_ylim(-2, 2)
# draw x-axis
ax.arrow(-3*pi, 0, 9*pi, 0, length_includes_head=True, head_width=0.1, head_length= 0.5, color='xkcd:almost black'  )
ax.annotate('X-axis', (5.5*pi, 0.2), color='xkcd:almost black')
# draw y-axis
ax.arrow(0, -2, 0, 4, length_includes_head=True, head_width=0.3, head_length= 0.15, color='xkcd:almost black'  )
ax.annotate('Y-axis', (0.3, 1.8), color='xkcd:almost black')
######################################################################


# x ticks and labels set-up
######################################################################
def format_func(x, loc):
    x = round(x*2/pi)  # round to an integer
    if x == 0:
        return 0
    if x == 1:
        return r'$\pi/2$'
    if x == -1:
        return r'$-\pi/2$'
    if x == 2:
        return r'$\pi$'
    if x == -2:
        return r'$-\pi$'
    elif x % 2 == 0:
        return r'${0}\pi$'.format(int(x // 2))
    else:
        x = str(int(x))
        return r"${0}\pi/2$".format(x)

# x-axis ticks
ax.xaxis.set_major_locator(tck.MultipleLocator(pi/2))
# x-axis ticklabels
ax.xaxis.set_major_formatter(tck.FuncFormatter(format_func))
ax.xaxis.set_tick_params(rotation=-30)
######################################################################


#Taylor series functions around x = pi
######################################################################
# taylor series of degree 2*n + 1
def taylorN_sin_aroundPi(x, n):
    if n == 0:
        return -(x - pi)
    return pow(-1, n+1)*pow(x - pi, 2*n+1)/fact(2*n+1) + taylorN_sin_aroundPi(x, n-1)
######################################################################


# graph functions on ax
######################################################################
# x and y values
xv = np.linspace(-3*pi, 6* pi, 200)
sin_yv1= [np.sin(x) for x in xv]
taylor9_yv1= [taylorN_sin_aroundPi(x, 4) for x in xv]
taylor15_yv1= [taylorN_sin_aroundPi(x, 7) for x in xv]

ax.grid(b=True, which= 'major', axis='x')

# function graph
ax.plot(xv, sin_yv1, color='xkcd:bright blue')
ax.annotate('sin(x)', (13.8, 1.2), color='xkcd:bright blue')
ax.plot(xv, taylor9_yv1, color='xkcd:grass green')
ax.annotate(r'$Taylor_{9}(sin, x{\in}V_{\epsilon}({\pi}))$', (9.2, -1.5), color='xkcd:grass green')
ax.plot(xv, taylor15_yv1, color='xkcd:brick red')
ax.annotate(r'$Taylor_{15}(sin, x{\in}V_{\epsilon}({\pi}))$', (7, 1.5), color='xkcd:brick red')
######################################################################


plt.show()
