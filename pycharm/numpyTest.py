import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array(10)
C = (A * B).flatten()
D = np.sum(A*B)
# print(C)
# print(C > 15)
# print(C[C > 15])
print(D)
