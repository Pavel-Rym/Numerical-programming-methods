import numpy as np
from numpy.linalg import matrix_rank

 # example: 
    # 7x +3y -6z = -1
    # 7x +9y -9z = 5
    # 2x -4y +9z = 28
    
delta = np.matrix('7 3 -6; 7 9 -9; 2 -4 9')

delta_x = np.matrix('-1 3 -6; 5 9 -9; 28 -4 9')
delta_y = np.matrix('7 -1 -6; 7 5 -9; 2 28 9')
delta_z = np.matrix('7 3 -1; 7 9 5; 2 -4 28')


discr = np.linalg.det(delta)

discr_x = np.linalg.det(delta_x)
discr_y = np.linalg.det(delta_y)
discr_z = np.linalg.det(delta_z)

x = discr_x / discr
y = discr_y / discr
z = discr_z / discr

print("x = ", x)
print("y = ", y)
print("z = ", z)
