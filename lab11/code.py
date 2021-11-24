import matplotlib.pyplot as plt
import numpy as np

#функція та її похідні 
def f(x):
  return np.cos(3*x-1)+x
def f1(x):
  return 1 - 3*np.sin(3*x-1)
def f2(x):
  return -9*np.cos(3*x-1)
def f3(x):
  return 27*np.sin(3*x-1)

#функція наближення за многочленом Тейлора 
def tailor(x): 
  a = 0
  y = f(a) + f1(a)*x + f2(a)*(x**2/2) + f3(a)*(x**3/6)
  
  return y


x = np.linspace(-2, 1.5)
y = f(x)
y_tailor = tailor(x)
plt.plot(x, y, 'b', x, y_tailor, 'y') 
plt.title('Графік функції та наближення за многочленом Тейлора')
plt.legend(['Графік функції', 'Графік наближення'])
plt.show()
