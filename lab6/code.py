from scipy import optimize 
import numpy as np

#вхідні дані
x0 = -1.1
y0 = -1

def f1(x):
  return np.sin(x-1) - 1.3
  
def f2(y):
  return -np.sin(y+1) - 0.8
  
#основна функція
def iteration(x,y,e):
  xn = x
  yn = y
  xn1 = f2(x)
  yn1 = f1(y)
  n = 1
  while ((abs(xn1-xn)>=e) & (abs(yn1 - yn) >=e)):
    xn = xn1
    yn = yn1
    xn1 = f2(yn)
    yn1 = f1(xn1)
    n = n + 1
    
#вивидимо результат
  print('Simple iteration:')
  print('x1=', xn, ' \n y1=', yn, ' \n The amount of iteration=', n)
  
iteration(x0, y0, 0.0001)

#перевірка
def f(x):
  return np.sin(x[1] + 1) - x[0] - 1.2, np.cos(x[0]) - 4 * x[1]
  
o = optimize.root(f, [0,0], method  = 'hybr')
print(o.x)
