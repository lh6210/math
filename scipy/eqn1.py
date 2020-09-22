
from scipy.optimize import fsolve
from math import exp


#def f(x):
#    return [exp(x[0]) + x[0] - 2, exp(x[1]) + x[1] - 1/x[1]]
#
#root = fsolve(f, [1, 1])

def g(x):
    return exp(x) + x - 2

root = fsolve(g, 1)

