from sympy import Pow, Symbol, integrate, N, oo
import scipy.integrate as sci_int
from math import pow
from numpy import inf 

def f(y, x):
    return 1 / (pow(x, 4) + pow(y, 2)) 

rs = sci_int.dblquad(f, 1, inf, lambda x: pow(x, 2), lambda x: inf)

print("scipy result: {}".format(rs))



x = Symbol('x ')
y = Symbol('y')

expr = 1/ (Pow(x, 4) + Pow(y, 2))

int1 = integrate(expr, (y, Pow(x, 2), oo))

int2 = integrate(int1, (x, 1, oo))

result = N(int2)

int3 = integrate(int1, x)


#print("step 1: {}".format(int1))

print("sympy result: {}".format(result))



print("sympy result: {}".format(int3))
