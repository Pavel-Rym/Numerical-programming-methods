import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + np.sin(y/(15)**0.5)


x0 = 0.2
y0 = 1.1
h = 0.1

x = []
y = []

x.append(x0)
y.append(y0)


while x0 != 1.2:
    y0 = y0 + h*f(x0, y0)
    x0 = x0 + h
    x.append(x0)
    y.append(y0)
print(y)
    
plt.plot(x, y)
plt.title('Eyler method')
plt.grid()
plt.show()
