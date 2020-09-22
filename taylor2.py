

######################################################################
#This document is the comparison of two taylor polynomials of sin(x) located at different points
#You could see the limitation of taylor polynomials, the x has to be close to point a
#
#Think of how to define the taylor polynomial for sin(x)
#for any x, since sin(x) is sinusoidal, find the coterminal angle of x between 0 and 2pi
#and then set a = pi would be a good try
#
#
######################################################################


from math import factorial as fact
from math import sin, pi
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as tck


# figure and two axes set-up
######################################################################
fig, axes = plt.subplots(2, 1, figsize=(10, 8))

plt.subplots_adjust(hspace=0.5)

# x, y limit
for i in range(2):
    axes[i].set_xlim(-3 * pi, 6 * pi)
    axes[i].set_ylim(-5, 5)
# draw x-axis
    axes[i].arrow(-3*pi, 0, 9*pi, 0, length_includes_head=True, head_width=0.2, head_length= 0.7, color='xkcd:almost black'  )
    axes[i].annotate('X-axis', (5.5*pi, 0.3), color='xkcd:almost black')
# draw y-axis
    axes[i].arrow(0, -5, 0, 10, length_includes_head=True, head_width=0.3, head_length= 0.5, color='xkcd:almost black'  )
    axes[i].annotate('Y-axis', (0.2, 4.3), color='xkcd:almost black')
######################################################################


# two axes x ticks and labels set-up
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

for i in range(2):
# x-axis ticks
    axes[i].xaxis.set_major_locator(tck.MultipleLocator(pi/2))
# x-axis ticklabels
    axes[i].xaxis.set_major_formatter(tck.FuncFormatter(format_func))
    axes[i].xaxis.set_tick_params(rotation=-30)
######################################################################


#Taylor series functions around x=0
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


# graph functions on axes[0]
######################################################################
# x and y values
xv = np.linspace(-3*pi, 6* pi, 100)
sin_yv= [sin(x) for x in xv]
taylor9_yv= [taylor_sin(x) for x in xv]
taylor15_yv= [taylorN_sin(x, 7) for x in xv]

axes[0].grid(b=True, which= 'major', axis='x')

# function graph
axes[0].plot(xv, sin_yv, color='xkcd:bright blue')
axes[0].annotate('sin(x)', (7.5, 1.2), color='xkcd:bright blue')
axes[0].plot(xv, taylor9_yv, color='xkcd:grass green')
axes[0].annotate(r'$Taylor_{9}(sin, x{\in}V_{\epsilon}(0))$', (6.2, 4), color='xkcd:grass green')
axes[0].plot(xv, taylor15_yv, color='xkcd:brick red')
axes[0].annotate(r'$Taylor_{15}(sin, x{\in}V_{\epsilon}(0))$', (8.2, -4), color='xkcd:brick red')
######################################################################


#Taylor series functions around x = 3pi
######################################################################
## taylor series of degree 9
#def taylor_sin(x):
#    return x - pow(x, 3)/ fact(3) + pow(x, 5)/fact(5) - pow(x, 7)/fact(7) + pow(x, 9) / fact(9)

# taylor series of degree 2*n + 1
def taylorN_sin_around3Pi(x, n):
    if n == 0:
        return -(x - 3 * pi)
    return pow(-1, n+1)*pow(x - 3*pi, 2*n+1)/fact(2*n+1) + taylorN_sin_around3Pi(x, n-1)
######################################################################


# graph functions on axes[1]
######################################################################
# x and y values
#xv1 = np.linspace(-pi, 7* pi, 100)
sin_yv1= [sin(x) for x in xv]
taylor9_yv1= [taylorN_sin_around3Pi(x, 4) for x in xv]
taylor15_yv1= [taylorN_sin_around3Pi(x, 7) for x in xv]

axes[1].grid(b=True, which= 'major', axis='x')

# function graph
axes[1].plot(xv, sin_yv1, color='xkcd:bright blue')
axes[1].annotate('sin(x)', (7.5, 1.2), color='xkcd:bright blue')
axes[1].plot(xv, taylor9_yv1, color='xkcd:grass green')
axes[1].annotate(r'$Taylor_{9}(sin, x{\in}V_{\epsilon}({3\pi}))$', (4.2, 4), color='xkcd:grass green')
axes[1].plot(xv, taylor15_yv1, color='xkcd:brick red')
axes[1].annotate(r'$Taylor_{15}(sin, x{\in}V_{\epsilon}(3{\pi}))$', (1.7, -4), color='xkcd:brick red')
######################################################################

axes[0].set_title(r'$n^{th}$ degree Taylor polynomials of Sin(x) at x = 0')
axes[1].set_title(r'$n^{th}$ degree Taylor polynomials of Sin(x) at x = $3\pi$')


plt.show()
