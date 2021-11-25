import math
import numpy as np
from scipy import integrate

def f(x):
    return (math.log10(x**2+1))/x
    
b = 1.6
a = 0.8
n = 8
    
def simpson_method(a, b, n):
    x = np.linspace(a, b, n+1)
    y = []
    for i in range(len(x)):
        y.append(f(x[i]))
    h = (b-a)/n
    edge = 0
    even = 0
    odd = 0
    for i in range(len(y)):
        if i == 0 or i == len(y)-1: 
            edge += y[i]
        elif i%2 == 0: 
            even += y[i]
        elif i%2 != 0:
            odd += y[i]

    return (h/3)*(edge + 4*odd + 2*even)
    
print("Резульат за методом Cімпсона:", simpson_method(a, b, n))
v,err = integrate.quad(f, 0.8, 1.6)
print("Перевірка", v)
