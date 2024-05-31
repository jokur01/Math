from sympy import *
import numpy as np
x = Symbol('x')
y = x**3
y1prime = y.diff(x)
y2prime = y1prime.diff(x)



f = lambdify(x, y2prime, 'numpy')
print(f(2))

