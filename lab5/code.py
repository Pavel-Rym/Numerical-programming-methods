import numpy as np

A = np.matrix('3 -5 3; 1 2 1; 2 7 -1')
B = np.matrix('1; 4; 8')
n = len(B)
k = 1

while k <= n - 1:
    i = k + 1
    while i < n:
        if A[i, k] != 0.0:
            A[i, k+1:n] = A[i,k+1:n] - A[i,k]/A[k,k] * A[k,k+1:n]
            B[i] = B[i] - A[i, k]/A[k, k] * B[k]
        i = i + 1
    k = k + 1
k = n - 1
while k > -1:
    B[k] = (B[k] - np.dot(A[k, k+1:n], B[k+1:n]))/A[k,k]
    print('Method of Gauss', B[k])
    k -= 1
print('Check', np.linalg.solve (A, B))
print('Method of Jordan - Gauss', np.linalg.inv(A)*B)
