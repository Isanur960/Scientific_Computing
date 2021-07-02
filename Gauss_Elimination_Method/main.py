import numpy as np

A = np.array([[-2,1,3],
              [1,2,1],
              [3,1,-2]], dtype = 'f')
B = np.array([0,0,0], dtype ='f')
l = len(A)
 
for i in range(l - 1):
  for j in range(i+1, l):
    if A[j][i] == 0:
      pass
    else:
      ratio = A[i][i] / A[j][i]
      A[j] = A[i] - (A[j] * ratio)
      B[j] = B[i] - (B[j] * ratio)

print(A)

solutions = []
n = l - 2
x4 = B[-1] / A[l-1][l-1]
print(x4)
solutions.append(x4)
while n > -1 :
  sum = 0
  sol_ind = 0
  for i in range(n+1, l):
    sum = sum + A[n][i] * solutions[sol_ind]
    sol_ind =+ 1
  x = (B[n] - sum ) / A[n][n]
  solutions.insert(0,x)
  n = n - 1
print(solutions)
