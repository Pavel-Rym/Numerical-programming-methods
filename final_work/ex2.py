import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

#вхідні дані
N = 1000000
S0 = 990000
I0 = 7000
R0 = 3000
alpha = 0.5
beta = 0.3
#крок t = 0.25
t = np.linspace(0, 20, 81)

#фукнція для знаходження швидкості зростання S та I
def diff_susceptible_infected(S0_I0, t, alpha, beta):
    S0, I0 = S0_I0
    diff_susceptible = -alpha*S0
    diff_infected = S0*alpha-I0*beta
    return [diff_susceptible, diff_infected]  

#спираючись на перше завдання, підставляємо diff_s та diff_i в інтеграл, аби отримати значення функції
#оскільки нам треба графік, необхідно мати масив значень функції. для цього підійде функція odeint
susceptible_infected_arr = scipy.integrate.odeint(diff_susceptible_infected, [S0, I0], t, args=(alpha,beta))

susceptible_arr = susceptible_infected_arr[:, 0] #вибираємо перший стовпчик масиву, що є значеннями функції S(t)
infected_arr = susceptible_infected_arr[:, 1] #вибираємо другий стовпчик масиву, що є значеннями функції I(t)

recovered_arr = []
#віднімаємо від N суму отриманих значень, аби отримати R
for i in range(len(susceptible_arr)):
  recovered_arr.append(N-(susceptible_arr[i]+infected_arr[i]))
  
#інтерполюємо значення R(t)
f = interpolate.interp1d(t, recovered_arr, kind='cubic')

#виводимо графіки 
plt.plot(t, susceptible_arr, 'b')
plt.plot(t, infected_arr, 'r')
plt.plot(t, f(t), 'g')
plt.title("Epidemic model")
plt.legend(["S(t)", "I(t)", "R(t)"])
plt.grid()
plt.show()
