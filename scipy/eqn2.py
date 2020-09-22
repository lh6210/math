import scipy.integrate as scp_intl
from sympy import Pow, Symbol, integrate, N 
from math import pow





def f(x):
    return (3* pow(x, 5) - 10*pow(x, 4) + 21* pow(x, 3))/ (x* (pow(x, 2) + 1) * pow((pow(x, 2) + 4), 2))

result1 = scp_intl.quad(f, 2, 3)
print("result1 is {}".format(result1))


x = Symbol('x')

expr = (3* Pow(x, 5) - 10*Pow(x, 4) + 21* Pow(x, 3))/ (x* (Pow(x, 2) + 1) * Pow((Pow(x, 2) + 4), 2))
result2 =  N(integrate( expr, (x, 2, 3)))

print('resutl2 is {}'.format(result2))
