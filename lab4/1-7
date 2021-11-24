import numpy as np
from numpy.linalg import matrix_rank

print("Example 1")
A1 = np.matrix('2 3 1; -1 1 0; 1 2 -1')
A2 = np.matrix('1 2 1; 0 1 2; 3 1 1')
print(A1*A2-A2*A1)


print("Example 2")
B = np.matrix('-1 2; 0 1')
degree = np.linalg.matrix_power(B, 2)
print(degree)

print("Example 3")
C1 = np.matrix('5 8 4; 6 9 -5; 4 7 -3')
C2 = np.matrix('3 2 5; 4 -1 3; 9 6 5')
product = C1.dot(C2)
print(product)

print("Example 4")
D = np.matrix('0 2 0; 3 4 5; 6 7 8')
module = np.linalg.det(D)
print(module)

print("Example 5")
E = np.matrix('2 3 4 1; 1 2 3 4; 3 4 1 2; 4 1 2 3')
module1 = np.linalg.det(E)
print(module1)

print("Example 6")
F = np.matrix('2 5 7; 6 3 4; 5 -2 -3')
inverted = np.linalg.inv(F)
print(inverted)

print("Example 7")
G = np.matrix('-2 3 1 -1; 3 2 1 4; 1 2 3 4; 0 2 3 3')
rank = np.linalg.matrix_rank(G)
print (rank)
