import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from scipy import integrate

speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65]
time = np.linspace(0, 11, 12)
print("Масив часу time:", time)
f = interpolate.interp1d(time, speed, kind='cubic')
x = np.linspace(0, 11, 10000)
y = f(x)
S = integrate.quad(f, 0, 11)
print("Пройдений шлях:", S[0])

plt.plot(time, speed, 'g--')
plt.plot(x, y, 'r')
plt.xlim(0, 11)
plt.ylim(0, 130)
plt.title('Графік швидкості')
plt.legend(['Точковий графік', 'Інтерпольований графік'])
plt.grid()
plt.show()
