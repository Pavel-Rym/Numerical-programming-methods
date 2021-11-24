#Створіть  прямокутну  матрицю  A,  яка  має  N  рядків і M стовпців 
#з випадковими елементами. Знайдіть суму елементів всієї матриці. 
#Визначте, яку долю в цій сумі складає сума елементів кожногостовпця.


import numpy as np
from numpy.linalg import matrix_rank

def sumColumn(matrix, column):
    total = 0
    i = 0
    while i < 3:
        total = total + A[column][i]
        i = i + 1
    return total

M = 3
N = 4

A = np.random.random((N, M))

a_sum = np.sum(A)

a_sum1 = sumColumn(A, 0)
a_sum2 = sumColumn(A, 1)
a_sum3 = sumColumn(A, 2)
a_sum4 = sumColumn(A, 3)

share_of_col1 = a_sum1 / a_sum
share_of_col2 = a_sum2 / a_sum
share_of_col3 = a_sum3 / a_sum
share_of_col4 = a_sum4 / a_sum

print('Сума матриці = ', a_sum)
print('Доля першого стовпця: ', share_of_col1)
print('Доля другого стовпця: ', share_of_col2)
print('Доля третього стовпця: ', share_of_col3)
print('Доля четвертого стовпця: ', share_of_col4)
    
