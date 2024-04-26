def func(x, t):
    return (x*x - t)

def deriv(x):
    return 2*x

def NewtonRaphson(n, t):
    m = func(n, t) / deriv(n)
    while(m>=0.00001):
        m = func(n, t) / deriv(n)
        n -= m
    return n

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

plt.xlabel('x')
plt.ylabel('y')

rf = open('data.txt', 'r')
mat = []
n = 0
for line in rf:
    mat.append(line.split())
    n+=1
    
mat = np.array(mat)
mat = mat.astype(np.float)

x = []
for i in range(n):
    x.append(mat[i][0])
x = np.array(x)

y = []
for i in range(n):
    y.append(mat[i][1])
y = np.array(y)

plt.scatter(x, y, s=.5)
    
sumY = 0
for i in range(n):
    sumY = sumY + y[i]

sumX = 0
for i in range(n):
    sumX = sumX + x[i]

sumXY = 0
for i in range(n):
    sumXY = sumXY + x[i]*y[i]

sumX2 = 0
for i in range(n):
    sumX2 = sumX2 + x[i]*x[i]

v = np.zeros(shape = (2, 2))
c = np.zeros(shape = (2, 1))

v = v.astype(np.float)
c = c.astype(np.float)

#First order
v[0][0] = n
v[0][1] = sumX
v[1][0] = sumX
v[1][1] = sumX2

c[0] = sumY
c[1] = sumXY

a = np.zeros(shape = (2, 1))
v = np.linalg.inv(v)

a = (v.dot(c))

Sr = 0;
St = 0;
for i in range(n):
    Sr = Sr + (y[i]-a[0]-a[1]*x[i]) * (y[i]-a[0]-a[1]*x[i])

Ybar = sumY/n
for i in range(n):
    St = St + (y[i]-Ybar) * (y[i] - Ybar)
t = (St - Sr)/St

X1 = []
X1 = np.sort(x)
Y = []
for i in X1:
    temp = a[0] + a[1]*i
    Y.append(temp)
Y = np.array(Y)

plt.plot(X1, Y, label = 'First-order curve', color = 'gold', linewidth = 2)

print('Relevent parameters for the 1st order curve are:')
print('a0 =', end=' ')
print(float(a[0]))
print('a1 =', end=' ')
print(float(a[1]))
print("The regression coefficient of the 1st order curve is:", end = " ")
r1 = NewtonRaphson(1, t)
r1 = float(r1)
print(r1)
print('\n')

#Second order
sumX2Y = 0
for i in range(n):
    sumX2Y = sumX2Y + x[i]*x[i]*y[i]

sumX3 = 0
for i in range(n):
    sumX3 = sumX3 + x[i]*x[i]*x[i]
    
sumX4 = 0
for i in range(n):
    sumX4 = sumX4 + x[i]*x[i]*x[i]*x[i]
    
v = np.zeros(shape = (3, 3))
c = np.zeros(shape = (3, 1))
a = np.zeros(shape = (3, 1))

v[0][0] = n
v[0][1] = sumX
v[0][2] = sumX2

v[1][0] = sumX
v[1][1] = sumX2
v[1][2] = sumX3

v[2][0] = sumX2
v[2][1] = sumX3
v[2][2] = sumX4

c[0] = sumY
c[1] = sumXY
c[2] = sumX2Y

v = np.linalg.inv(v)
a = v.dot(c)

Sr = 0
for i in range(n):
    Sr = Sr + (y[i] - a[0]-a[1]*x[i]-a[2]*x[i]*x[i]) * (y[i]-a[0]-a[1]*x[i]-a[2]*x[i]*x[i])

t = (St - Sr)/St
r2 = NewtonRaphson(1, t)
r2 = float(r2)

Y = []
X1 = []
X1 = np.sort(x)
for i in X1:
    temp = a[0] + a[1]*i + a[2]*i*i
    Y.append(temp)

plt.plot(X1, Y, label = 'Second-order curve', color = 'orange', linewidth = 2)

print('Relevent parameters for the 2nd order curve are:')
print('a0 =', end=' ')
print(float(a[0]))
print('a1 =', end=' ')
print(float(a[1]))
print('a2 =', end=' ')
print(float(a[2]))
print('The regression coefficient of the 2nd order curve is:', end = " ")
print(r2)
print('\n')


#third order
sumX5 = 0
sumX6 = 0
sumX3Y = 0

for i in range(n):
    sumX5 = sumX5 + x[i]*x[i]*x[i]*x[i]*x[i]

for i in range(n):
    sumX6 = sumX6 + x[i]*x[i]*x[i]*x[i]*x[i]*x[i]
    
for i in range(n):
    sumX3Y = sumX3Y + x[i]*x[i]*x[i]*y[i]

v = np.zeros(shape = (4, 4))
c = np.zeros(shape = (4, 1))
a = np.zeros(shape = (4, 1))

v[0][0] = n
v[0][1] = sumX
v[0][2] = sumX2
v[0][3] = sumX3

v[1][0] = sumX
v[1][1] = sumX2
v[1][2] = sumX3
v[1][3] = sumX4

v[2][0] = sumX2
v[2][1] = sumX3
v[2][2] = sumX4
v[2][3] = sumX5

v[3][0] = sumX3
v[3][1] = sumX4
v[3][2] = sumX5
v[3][3] = sumX6

c[0] = sumY
c[1] = sumXY
c[2] = sumX2Y
c[3] = sumX3Y

v = np.linalg.inv(v)
a = v.dot(c)

Sr = 0
for i in range(n):
    Sr = Sr + (y[i] - a[0]-a[1]*x[i]-a[2]*x[i]*x[i]-a[3]*x[i]*x[i]*x[i]) * (y[i]-a[0]-a[1]*x[i]-a[2]*x[i]*x[i]-a[3]*x[i]*x[i]*x[i])

t = (St - Sr)/St
r3 = NewtonRaphson(1, t)
r3 = float(r3)

Y = []
X1 = []
X1 = np.sort(x)
for i in X1:
    temp = a[0] + a[1]*i + a[2]*i*i + a[3]*i*i*i
    Y.append(temp)
Y = np.array(Y)
plt.plot(X1, Y, label = 'Third-order curve', color = 'lawngreen', linewidth = 2)

print('Relevent parameters for the 3rd order curve are:')
print('a0 =', end=' ')
print(float(a[0]))
print('a1 =', end=' ')
print(float(a[1]))
print('a2 =', end=' ')
print(float(a[2]))
print('a3 =', end=' ')
print(float(a[3]))
print('The regression coefficient of the 3rd order curve is:', end = " ")
print(r3)

plt.legend()
plt.show()