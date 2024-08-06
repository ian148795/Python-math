import numpy as np
from sympy import *
from scipy import linalg
a=np.array([[-1,2,0],
            [-3,0,19],
            [5,-1,-3]])
b=np.array([1,2,3])
print("matriz")
print(a)
print(b)
x=linalg.solve(a,b)
print("x:", x)
inversa=linalg.inv(a)
print("inversa:")
print(inversa)

