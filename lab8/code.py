import numpy as np
import math

def yd(h, y1, y2, y3, y4):
    return 1/h*(y1 - (y2/2) + (y3/3) - (y4/4))
    
def ydd(h, y2, y3, y4):
    return 1/pow(h, 2)*(y2 - y3 + ((11/12)* y4))
    

mas_x = [1.5, 2, 2.5, 3, 3.5, 4]
mas_y = [10.517, 10.193, 9.807, 9.387, 8.977, 8.637]
h = mas_x[1] - mas_x[0]
mas = []
mas1 = []
y = []


for i in range(len(mas_y)):
    mas.append(mas_y[i] - mas_y[i-1])
    
mas.pop(0)
y.append(mas[1])
mas1 = mas.copy()
mas.clear()

for j in range(len(mas_y) - 2):
    for i in range(len(mas1)):
        mas.append(mas1[i] - mas1[i-1])
    mas.pop(0)
    if len(mas) > 1: y.append(mas[1])
    mas1.clear()
    mas1 = mas.copy()
    mas.clear()


print('Отримуємо значення, близьке до нуля \n', mas1, '\n')

print('Значення, необхідні для обчислень:\n', y, '\n')

print('Похідна першого порядку дорівнює:', yd(h, y[0], y[1], y[2], y[3]))
print('Похідна другого порядку дорівнює:', ydd(h, y[1], y[2], y[3]))
