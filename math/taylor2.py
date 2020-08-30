

from math import factorial as fact
from math import sin, pi
import matplotlib.pyplot as plt
import numpy as np




# canvas set-up
fig, ax = plt.subplots()

# x, y limit
ax.set_xlim(-4 * pi, 4 * pi)
ax.set_ylim(-5, 5)

# draw x-axis
ax.arrow(-4*pi, 0, 8*pi, 0, length_includes_head=True, head_width=0.2, head_length= 0.7, color='xkcd:almost black'  )
ax.annotate('X-axis', (3.3*pi, 0.3), color='xkcd:almost black')

# draw y-axis
ax.arrow(0, -5, 0, 10, length_includes_head=True, head_width=0.3, head_length= 0.5, color='xkcd:almost black'  )
ax.annotate('Y-axis', (0.2, 4.6), color='xkcd:almost black')

# taylor series with degree 9
def taylor_sin(x):
    return x - pow(x, 3)/ fact(3) + pow(x, 5)/fact(5) - pow(x, 7)/fact(7) + pow(x, 9) / fact(9)

# taylor series with degree 2*n + 1
def taylorN_sin(x, n):
    if n == 0:
        return x
    return pow(-1, n)*pow(x, 2*n+1)/fact(2*n+1) + taylorN_sin(x, n-1)

# x and y values
xv = np.linspace(-4*pi, 4* pi, 100)
sin_yv= [sin(x) for x in xv]
taylor9_yv= [taylor_sin(x) for x in xv]
taylor15_yv= [taylorN_sin(x, 7) for x in xv]


ax.grid(b=True, which= 'major', axis='x')

# function graph
ax.plot(xv, sin_yv)
ax.plot(xv, taylor9_yv)
ax.plot(xv, taylor15_yv)

plt.show()
