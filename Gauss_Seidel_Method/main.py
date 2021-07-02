import numpy as np

A = np.array([[1,1,1],
              [1,2,3],
              [1,4,9]], dtype = 'f')
B = np.array([4,7,15], dtype ='f')
l = len(A)
x = np.array([1, 1, 1], dtype ='f')

L = np.tril(A)
U = A - L
L_i = np.linalg.inv(L)
T = np.dot(L_i, U) * -1
C = np.dot(L_i, B)
err = 0

while err < 10000:
  n_x = np.dot(T,x) + C
  err = err + 1
  x = n_x

print(x)
