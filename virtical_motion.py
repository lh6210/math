

from math import sqrt, pow

def find_time(y, v):
    """ y = vt - 1/2*gt**2; g = 9.81
    
    """
    g = 9.81

    t1 = (v - sqrt(pow(v, 2) - 2 * y * g )) / g
    t2 = (v + sqrt(pow(v, 2) - 2 * y * g )) / g
    print('at time t=%g s and t=%g s, the height is %g m.' % (t1, t2, y))

