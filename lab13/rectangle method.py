from scipy import integrate
import numpy as np

def f(x):
    return 1/((3*x-1)**0.5)
    
b = 2.1
a = 1.4
n = 10
    
def rectangle_method(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    summ = 0
    for i in range(len(y)):
        summ += y[i]
        
    
    left = h*(summ-y[len(y)-1])
    right = h*(summ-y[0])
    x_mid = []
    y_mid = []
    for i in range(len(y)-1):
        x_mid.append(round(((x[i]+x[i+1])/2),3))
    for i in range(len(x_mid)):
        y_mid.append(f(x_mid[i]))
    summ_mid = 0 
    for i in range(len(y_mid)):
        summ_mid += y_mid[i]
    mid = h*summ_mid
    
    print("Відповідь: \n за формулою лівих прямокутників", left, "\n за формулою правих прямокутників", right, "\n за формулою середніх прямокутників", mid)
        
    
rectangle_method(a, b, n)
v,err = integrate.quad(f, 1.4, 2.1)
print("Перевірка", v)
