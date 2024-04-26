import matplotlib.pyplot as plt
import numpy as np
import math as m

def dydx(x, y):
    return m.sin(x*y) * (x + 20*y)

def Euler(Ex, Ey, inter):
    i = 1
    Ey[0] = 4
    j = inter
    while(j<=10):
        Ey[i] = Ey[i-1] + inter * dydx(Ex[i-1], Ey[i-1])
        i += 1
        j += inter
        
def RungeKutta2(X, Y, inter, a2):
    a1 = 1-a2
    p1 = 1/(2*a2)
    q11 = p1
    
    i = 1
    Y[0] = 4
    j = inter
    while(j<=10):
        k1 = dydx(X[i-1], Y[i-1])
        k2 = dydx(X[i-1]+p1*inter, Y[i-1]+q11*k1*inter)
        Y[i] = Y[i-1] + (a1*k1 + a2*k2)*inter
        i += 1
        j += inter
        
def RungeKutta4(Rx, Ry, inter):
    i = 1
    Ry[0] = 4
    j = inter
    while(j<=10):
        k1 = dydx(Rx[i-1], Ry[i-1])
        k2 = dydx(Rx[i-1]+.5*inter, Ry[i-1]+.5*k1*inter)
        k3 = dydx(Rx[i-1]+.5*inter, Ry[i-1]+.5*k2*inter)
        k4 = dydx(Rx[i-1]+inter, Ry[i-1]+k3*inter)
        
        Ry[i] = Ry[i-1] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)*inter
        i += 1
        j += inter
#Main
X1=[]
X2=[]
X3=[]
X4=[]
i=0
j=0
while(i<=10):
    X1.append(i)
    i+=.01
    j+=1
Y1 = np.empty(j, dtype=float)
i=0
j=0
while(i<=10):
    X2.append(i)
    i+=0.05
    j+=1
Y2 = np.empty(j, dtype=float)
i=0
j=0
while(i<=10):
    X3.append(i)
    i+=0.1
    j+=1
Y3 = np.empty(j, dtype=float)
i=0
j=0
while(i<=10):
    X4.append(i)
    i+=0.5
    j+=1
Y4 = np.empty(j, dtype=float)

X1 = np.array(X1)
X2 = np.array(X2)
X3 = np.array(X3)
X4 = np.array(X4)

#Euler
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
Euler(X1, Y1, 0.01)
plt.title('Euler Method')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(X1, Y1, label='interval = 0.01', color = 'gold', linewidth = 2)
Euler(X2, Y2, 0.05)
plt.plot(X2, Y2, label='interval = 0.05', color = 'blue', linewidth = 2)
Euler(X3, Y3, 0.1)
plt.plot(X3, Y3, label='interval = 0.1', color = 'lawngreen', linewidth = 2)
Euler(X4, Y4, 0.5)
plt.plot(X4, Y4, label='interval = 0.5', color = 'orange', linewidth = 2)
plt.legend()
plt.show()

#Huen
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Huen's Method")
plt.xlabel('x')
plt.ylabel('y')
RungeKutta2(X1, Y1, 0.01, 0.5)
plt.plot(X1, Y1, label='interval = 0.01', color = 'limegreen', linewidth = 2)
RungeKutta2(X2, Y2, 0.05, 0.5)
plt.plot(X2, Y2, label='interval = 0.05', color = 'yellow', linewidth = 2)
RungeKutta2(X3, Y3, 0.1, 0.5)
plt.plot(X3, Y3, label='interval = 0.1', color = 'navajowhite', linewidth = 2)
RungeKutta2(X4, Y4, 0.5, 0.5)
plt.plot(X4, Y4, label='interval = 0.5', color = 'red', linewidth = 2)
plt.legend()
plt.show()

#Midpoint
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Mindpoint Method")
plt.xlabel('x')
plt.ylabel('y')
RungeKutta2(X1, Y1, 0.01, 1)
plt.plot(X1, Y1, label='interval = 0.01', color = 'springgreen', linewidth = 2)
RungeKutta2(X2, Y2, 0.05, 1)
plt.plot(X2, Y2, label='interval = 0.05', color = 'burlywood', linewidth = 2)
RungeKutta2(X3, Y3, 0.1, 1)
plt.plot(X3, Y3, label='interval = 0.1', color = 'darkorange', linewidth = 2)
RungeKutta2(X4, Y4, 0.5, 1)
plt.plot(X4, Y4, label='interval = 0.5', color = 'slategrey', linewidth = 2)
plt.legend()
plt.show()

#Ralston
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Ralston's Method")
plt.xlabel('x')
plt.ylabel('y')
RungeKutta2(X1, Y1, 0.01, 2/3)
plt.plot(X1, Y1, label='interval = 0.01', color = 'green', linewidth = 2)
RungeKutta2(X2, Y2, 0.05, 2/3)
plt.plot(X2, Y2, label='interval = 0.05', color = 'tan', linewidth = 2)
RungeKutta2(X3, Y3, 0.1, 2/3)
plt.plot(X3, Y3, label='interval = 0.1', color = 'lightsteelblue', linewidth = 2)
RungeKutta2(X4, Y4, 0.5, 2/3)
plt.plot(X4, Y4, label='interval = 0.5', color = 'violet', linewidth = 2)
plt.legend()
plt.show()

#Runge-Kutta 4th
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("4th order RK Method")
plt.xlabel('x')
plt.ylabel('y')
RungeKutta4(X1, Y1, 0.01)
plt.plot(X1, Y1, label='interval = 0.01', color = 'springgreen', linewidth = 2)
RungeKutta4(X2, Y2, 0.05)
plt.plot(X2, Y2, label='interval = 0.05', color = 'burlywood', linewidth = 2)
RungeKutta4(X3, Y3, 0.1)
plt.plot(X3, Y3, label='interval = 0.1', color = 'chocolate', linewidth = 2)
RungeKutta4(X4, Y4, 0.5)
plt.plot(X4, Y4, label='interval = 0.5', color = 'deepskyblue', linewidth = 2)
plt.legend()
plt.show()

#step = .01
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Step size = .01")
plt.xlabel('x')
plt.ylabel('y')
Euler(X1, Y1, 0.01)
plt.plot(X1, Y1, label='Euler method', color = 'gold', linewidth = 2)
RungeKutta2(X1, Y1, 0.01, 0.5)
plt.plot(X1, Y1, label="Huen's method", color = 'limegreen', linewidth = 2)
RungeKutta2(X1, Y1, 0.01, 1)
plt.plot(X1, Y1, label='Midpoint method', color = 'hotpink', linewidth = 2)
RungeKutta2(X1, Y1, 0.01, 2/3)
plt.plot(X1, Y1, label="Ralston's method", color = 'darkgrey', linewidth = 2)
RungeKutta4(X1, Y1, 0.01)
plt.plot(X1, Y1, label='Rk 4th order', color = 'coral', linewidth = 2)
plt.legend()
plt.show()

#Step = .05
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Step size = .05")
plt.xlabel('x')
plt.ylabel('y')
Euler(X2, Y2, 0.05)
plt.plot(X2, Y2, label='Euler method', color = 'gold', linewidth = 2)
RungeKutta2(X2, Y2, 0.05, 0.5)
plt.plot(X2, Y2, label="Huen's method", color = 'limegreen', linewidth = 2)
RungeKutta2(X2, Y2, 0.05, 1)
plt.plot(X2, Y2, label='Midpoint method', color = 'blue', linewidth = 2)
RungeKutta2(X2, Y2, 0.05, 2/3)
plt.plot(X2, Y2, label="Ralston's method", color = 'darkgrey', linewidth = 2)
RungeKutta4(X2, Y2, 0.05)
plt.plot(X2, Y2, label='Rk 4th order', color = 'coral', linewidth = 2)
plt.legend()
plt.show()

#Step = .1
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Step size = .1")
plt.xlabel('x')
plt.ylabel('y')
Euler(X3, Y3, 0.1)
plt.plot(X3, Y3, label='Euler method', color = 'khaki', linewidth = 2)
RungeKutta2(X3, Y3, 0.1, 0.5)
plt.plot(X3, Y3, label="Huen's method", color = 'limegreen', linewidth = 2)
RungeKutta2(X3, Y3, 0.1, 1)
plt.plot(X3, Y3, label='Midpoint method', color = 'olive', linewidth = 2)
RungeKutta2(X3, Y3, 0.1, 2/3)
plt.plot(X3, Y3, label="Ralston's method", color = 'darkgrey', linewidth = 2)
RungeKutta4(X3, Y3, 0.1)
plt.plot(X3, Y3, label='Rk 4th order', color = 'magenta', linewidth = 2)
plt.legend()
plt.show()

#Step = .5
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
plt.grid(True, which='both')
plt.title("Step size = .5")
plt.xlabel('x')
plt.ylabel('y')
Euler(X4, Y4, 0.5)
plt.plot(X4, Y4, label='Euler method', color = 'khaki', linewidth = 2)
RungeKutta2(X4, Y4, 0.5, 0.5)
plt.plot(X4, Y4, label="Huen's method", color = 'limegreen', linewidth = 2)
RungeKutta2(X4, Y4, 0.5, 1)
plt.plot(X4, Y4, label='Midpoint method', color = 'olive', linewidth = 2)
RungeKutta2(X4, Y4, 0.5, 2/3)
plt.plot(X4, Y4, label="Ralston's method", color = 'darkgrey', linewidth = 2)
RungeKutta4(X4, Y4, 0.5)
plt.plot(X4, Y4, label='Rk 4th order', color = 'greenyellow', linewidth = 2)
plt.legend()
plt.show()