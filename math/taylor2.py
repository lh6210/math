

from math import factorial as fact
from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck


# canvas set-up
######################################################################
fig, ax = plt.subplots(figsize=(10, 4.8))

# x, y limit
ax.set_xlim(-4 * pi, 4 * pi)
ax.set_ylim(-5, 5)

# draw x-axis
ax.arrow(-4*pi, 0, 8*pi, 0, length_includes_head=True, head_width=0.2, head_length= 0.7, color='xkcd:almost black'  )
ax.annotate('X-axis', (3.3*pi, 0.3), color='xkcd:almost black')

# draw y-axis
ax.arrow(0, -5, 0, 10, length_includes_head=True, head_width=0.3, head_length= 0.5, color='xkcd:almost black'  )
ax.annotate('Y-axis', (0.2, 4.6), color='xkcd:almost black')
######################################################################


#Taylor series functions
######################################################################
# taylor series of degree 9
def taylor_sin(x):
    return x - pow(x, 3)/ fact(3) + pow(x, 5)/fact(5) - pow(x, 7)/fact(7) + pow(x, 9) / fact(9)

# taylor series of degree 2*n + 1
def taylorN_sin(x, n):
    if n == 0:
        return x
    return pow(-1, n)*pow(x, 2*n+1)/fact(2*n+1) + taylorN_sin(x, n-1)
######################################################################


# graph functions
######################################################################
# x and y values
xv = np.linspace(-4*pi, 4* pi, 100)
sin_yv= [sin(x) for x in xv]
taylor9_yv= [taylor_sin(x) for x in xv]
taylor15_yv= [taylorN_sin(x, 7) for x in xv]

ax.grid(b=True, which= 'major', axis='x')

# function graph
ax.plot(xv, sin_yv, color='xkcd:bright blue')
ax.annotate('sin(x)', (7.5, 1.2), color='xkcd:bright blue')
ax.plot(xv, taylor9_yv, color='xkcd:grass green')
ax.annotate(r'$Taylor_{9}$(sin, x)', (6.2, 4), color='xkcd:grass green')
ax.plot(xv, taylor15_yv, color='xkcd:brick red')
ax.annotate(r'$Taylor_{15}$(sin, x)', (2.3, -4), color='xkcd:brick red')
######################################################################


# x ticks and labels
######################################################################
# x-axis ticks
ax.xaxis.set_major_locator(tck.MultipleLocator(pi/2))

# x-axis ticklabels

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

ax.xaxis.set_major_formatter(tck.FuncFormatter(format_func))
ax.xaxis.set_tick_params(rotation=-30)
######################################################################


plt.show()
