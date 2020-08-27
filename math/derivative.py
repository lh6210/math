

def derivative(fn):
    dx = 1e-10
    def g(x):
        return (fn(x + dx) - fn(x)) / dx
    return g


def summation()
