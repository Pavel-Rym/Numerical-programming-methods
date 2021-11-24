import numpy as np
import math

# вхідні дані
mas_x = [0.101, 0.111, 0.121, 0.131, 0.141, 0.151]
mas_y = [1.2618, 1.2912, 1.3213, 1.3520, 1.3835, 1.4157]
searched_x1 = 0.107
searched_x2 = 0.137

# пошук q
h = mas_x[1] - mas_x[0]

for i in range(len(mas_x)):
    if mas_x[i+1] > searched_x1:
        x0 = mas_x[i]
        i1 = i # ця змінна відповідає за запис правильних значень Y, які ми будемо використовувати в формулі 1
        break
    
q1 = ((searched_x1 - x0)/h)

for i in range(len(mas_x)):
    if mas_x[i] > searched_x2:
        x0 = mas_x[i]
        i2 = i # ця змінна відповідає за запис правильних значень Y, які ми будемо використовувати в формулі 2
        break
    
q2= ((searched_x2 - x0)/h)


# масиви для роботи 
mas = []
mas1 = []
# масиви, в які будуть записуватися потрібні дані, запис початкових даних
y = [mas_y[i1]]
yy = [mas_y[i2]]


# знаходження Y та запис потрібних у масиви
for i in range(len(mas_y)):
    mas.append(mas_y[i] - mas_y[i-1])
    
mas.pop(0)
y.append(mas[i1])
yy.append(mas[i2])
i2 = i2 - 1
mas1 = mas.copy()
mas.clear()

for j in range(len(mas_y) - 1):
    for i in range(len(mas1)):
        mas.append(mas1[i] - mas1[i-1])
    mas.pop(0)
    if len(mas) > 0: y.append(mas[i1])
    if (i2 >= 0): yy.append(mas[i2])
    i2 = i2 - 1
    mas1.clear()
    mas1 = mas.copy()
    mas.clear()

# за формулами розраховуємо потрібні нам значення 

# змінні для роботи
i = 0 
q1_1 = q1
q2_1 = q2
# змінні для запису результатів
f1 = 0 
f2 = 0

while i < len(y):
    if i == 0:
        z = y[i]
    elif i == 1:
        z = (y[i] * q1_1)
    else:
        g = 1
        q1_1 = q1_1*(q1 - g)
        g = g + 1 
        z = (y[i] * q1_1)/math.factorial(i)
    f1 = f1 + z
    i = i + 1
    
i = 0
while i < len(yy):
    if i == 0:
        z = yy[i]
    elif i == 1:
        z = (yy[i] * q2_1)
    else:
        g = 1
        q2_1 = q2_1*(q2 + g)
        g = g + 1 
        z = (yy[i] * q2_1)/math.factorial(i)
    f2 = f2 + z
    i = i + 1
    
print("Перше шукане значення:", f1)
print("Друге шукане значення:",f2)
