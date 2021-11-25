import numpy as np
from scipy import integrate

def f(x):
    return 1/(0.2*x**2+1)**0.5
    
b = 2.5
a = 1.3
n = 20
    
def trapezoid_method(a, b, n):
    x = np.linspace(a, b, n+1)
    y = []
    for i in range(len(x)):
        y.append(f(x[i]))
    h = (b-a)/n
    edge = y[0]+y[len(y)-1]
    summ = 0 
    for i in range(len(y)):
        summ += y[i]
    summ = summ - edge
    return h*((edge/2)+summ)
    
print("Резульат за методом Трапеції:", trapezoid_method(a, b, n))
v,err = integrate.quad(f, 1.3, 2.5)
print("Перевірка", v)
