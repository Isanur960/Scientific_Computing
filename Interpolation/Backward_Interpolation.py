import numpy as np

y = [1891, 1901, 1911, 1921, 1931]
fx = [46, 66, 81, 93, 101]

temp_li = fx
temp_matr = []
#traget
x = 2005
#base
a = y[0]
#difference
h = y[1] - y[0]

u = (x - a)/h

print(h, u)

def dell(li):
  out_li = np.diff(li)
  return out_li
def fact(x):
  res = 1
  for i in range(1,x+1):
    res = res * i
  return res



counter = 0
for i in range(1, len(y)):
  temp_li = dell(temp_li)
  temp_matr.append(temp_li)
  counter = counter + 1

result = fx[0]
add_temp = 1
counter_1 = 0
while True:
  try:
    ind = len(temp_matr)-1
    add0 = temp_matr[counter_1][ind]
  except:
    break
  f = counter_1 + 1
  add1 = 1/fact(f)
  add3 = u - counter_1
  if add3 == 0:
    break
  
  add = add_temp * add0 * add1 * add3
  add_temp = add3 * add_temp
  result = result + add
  counter_1 = counter_1 + 1
  
print(result)
