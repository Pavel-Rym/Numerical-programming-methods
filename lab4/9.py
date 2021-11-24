import numpy as np
from numpy.linalg import matrix_rank

 # example: 
    # 2x -y +z = 5
    # 3x +4y -2z = -3
    # x -3y +z = 4
    
    
A = np.matrix('2 -1 1; 3 4 -2; 1 -3 1')
B = np.matrix('5; -3; 4')

A_inv = np.linalg.inv(A)

result = A_inv.dot(B)

x = result[0][0]
y = result[1][0]
z = result[2][0]

print("x =", x)
print("y =", y)
print("z =", z)
