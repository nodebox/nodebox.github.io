def evaluate(expr, x, y, z):
    ns = {"x": x, "y": y, "z": z}
    exec "from math import *" in ns
    return eval(expr, ns)