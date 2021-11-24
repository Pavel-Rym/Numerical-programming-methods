import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from numpy import *

// вхідні дані
x = [0.6, 0.8, 1.1, 1.6, 2]
y = [1.76, 2.61, 3.89, 2.18, 4.35]

def spline(x, y, search):
  h = []
  m = []
  k = []
  u = []
  alpha = []
  beta = []
  
  a = []
  b = []
  c = []
  d = []
  
  i = 0
  while i < len(x)-1:
      h.append(x[i+1] - x[i]) 
      u.append((y[i+1]-y[i])/(x[i+1]-x[i]))
      a.append(y[i])
      i = i + 1
      
  i = 0
  while i < len(x)-2:
      m.append(2*(h[i]+h[i+1]))
      k.append(3*(((y[i+2]-y[i+1])/h[i+1])-((y[i+1]-y[i])/h[i])))
      i = i + 1
   
  i = 0   
  while i < len(x)-1:
      if i == 0: 
          alpha.append(0)
          beta.append(0)
      elif i == 1:
          alpha.append(k[i-1]/m[i-1])
          beta.append(h[i]/m[i-1])
      else: 
          alpha.append((k[i-1]-h[i-1]*alpha[i-1])/(m[i-1]-h[i-1]*beta[i-1]))
          beta.append(h[i]/(m[i-1]-h[i-1]*beta[i-1]))
          
      i = i + 1
  i = 0
  while i < len(x):
      if i == 0: c.append(0)
      else:
          c.append(alpha[(len(x)-1)-i] - beta[(len(x)-1)-i]*c[i-1])
      i = i + 1
      
  c.reverse()
  
  i = 0
  while i < len(x)-1:
      d.append((c[i+1]-c[i])/ (3*h[i]))
      b.append(((y[i+1]-y[i])/h[i])-((c[i+1]+2*c[i])*h[i])/3)
      i = i + 1
     
      
  i = 0
  while i <= len(x)-2:
      if x[i] <= search <= x[i+1]:
          return a[i]+b[i]*(search-x[i])+c[i]*(search-x[i])**2+d[i]*(search-x[i])**3
      i = i + 1
  print("Помилка: вкажіть шукане число в межах масиву х")
  return 0
      
      
  
  
arr = []
i = 0
xs = linspace(0.6, 2)

while i < len(xs):
  arr.append(round(spline(x, y, xs[i]),5))
  i = i + 1
  
plt.plot(x, y, 'ro', xs, arr, 'g')
plt.title("Function 'spline'")
plt.legend(['array_x', 'def spline'])
plt.show()
