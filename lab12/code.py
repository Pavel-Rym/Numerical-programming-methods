import matplotlib.pyplot as plt
import numpy as np

#функція 
def f(x):
  return np.sin(4*x)

x = [0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.47, 0.5]
y = []
_x = 0
_x2 = 0
_y = 0
_yx = 0

result = []

l = len(x)

for i in range(l):
  y.append(f(x[i]))
  
for i in range(l-1):
  if i == 0:
    _x = x[i]+x[i+1]
    _x2 = x[i]**2 + x[i+1]**2
    _y = y[i]+y[i+1]
    _yx = x[i]*y[i] + x[i+1]*y[i+1]
  else:
    _x += x[i+1]
    _x2 += x[i+1]**2
    _y += y[i+1]
    _yx += x[i+1]*y[i+1]

_x = _x / l
_x2 = _x2 / l
_y = _y / l
_yx = _yx / l

a1 = (_yx + _x*_y)/(_x2 - _x**2)
a0 = _y - a1 * _x

for i in range(l):
  result.append(a0 + a1 * x[i])

plt.plot(x, y, 'b', x, result, 'y') 
plt.grid()
plt.show()
