import matplotlib.pyplot as plt
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

def Trapezoid(X, Y, up, low):
    Fxi = 0
    fx = []
    n = 0
    i = low
    while(i <= up):
        fx.append(Y[i])
        n += 1
        i += 1
    n = n-1
    i = 1
    while(i <= n-1):
        Fxi += fx[i]
        i += 1
    t = X[up] - X[low]
    I = t*(fx[0]+fx[n]+2*Fxi) / (2*(up-low))
    
    return I



def Simp13(X, Y, up, low):
    Fxi = 0
    Fxj = 0
    n = 0
    i = low
    fx = []
    while(i <= up):
        fx.append(Y[i])
        n += 1
        i += 1
    n = n-1
    i = 1
    j = 2
    while(i <= n-1):
        Fxi += fx[i]
        i += 2
    while(j <= n-2):
        Fxj += fx[i]
        j += 2
    
    t = X[up] - X[low]
    I = t*(fx[0]+fx[n]+4*Fxi+2*Fxj) / (3*(up-low))
    
    return I



def Simp38(X, Y, up, low):
    Fxi = 0
    Fxj = 0
    fx = []
    n = 0
    i = low
    while(i <= up):
        fx.append(Y[i])
        i += 1
        n += 1
    n = n-1
    i = 1
    while(i <= n-1):
        if(i%3 == 0):
            Fxj += fx[i]
        else:
            Fxi += fx[i]
        i += 1
        
    t = X[up]-X[low]
    I = t*3*(fx[0]+fx[n]+3*Fxi+2*Fxj) / (8*(up-low))
    
    return I




import numpy as np
rf = open('input.txt', 'r')

N = int(rf.readline())

temp = []
for line in rf:
    temp.append(line.split())

temp = np.array(temp)
temp = temp.astype(np.float)

X = []
Fx = []
for i in range(N):
    X.append(temp[i][0])
    Fx.append(temp[i][1])
N = N-1
I = 0
i = 1

Espace = []
count = 1
d = X[1] - X[0]
while(i<=N-1):
    d1 = X[i+1] - X[i]
    if(abs(d1-d) <= .0001):
        count += 1
    else:
        Espace.append(count)
        count = 1
        d = d1
    i += 1

Espace.append(count)
plt.xlabel("X")
plt.ylabel("F(X)")
plt.title('Numerical Integration', color='orange')
plt.grid(True)
i = j = k = 0
x = y = z = 0
ab = []
ordi = []
for el in Espace:
    if(el%3 == 0):
        I += Simp38(X, Fx, i+el, i)
        k = i
        while(k<=i+el):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='lawngreen', label='Simpson3/8')
        i = i+el
        z += el
        ab = []
        ordi = []
    elif(el%3 == 1 and el==4):
        I += Simp13(X, Fx, i+el, i)
        k = i
        while(k<=i+el):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='aqua', label='Simpson1/3')
        i += el
        y += el
        ab = []
        ordi = []
    elif(el%3 == 1 and el>4):
        I += Simp13(X, Fx, i+4, i)
        k = i
        while(k<=i+4):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='aqua', label='Simpson1/3')
        ab = []
        ordi = []
        j = i
        i += 4
        y += 4
        I += Simp38(X, Fx, j+el, i)
        k = i
        while(k<=j+el):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='lawngreen', label='Simpson3/8')
        i = j+el
        z += el-4
        ab = []
        ordi = []
    elif(el%3 == 2 and el>3):
        I += Simp13(X, Fx, i+2, i)
        k = i
        while(k<=i+2):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='aqua', label='Simpson1/3')
        ab = []
        ordi = []
        j = i
        i += 2
        y += 2
        I += Simp38(X, Fx, j+el, i)
        k = i
        while(k<=j+el):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='lawngreen', label='Simpson3/8')
        i = j+el
        z += el-2
        ab = []
        ordi = []
    elif(el%3 == 1 and el<3):
        I += Trapezoid(X, Fx, i+el, i)
        k = i
        while(k<=i+el):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='wheat', label='Trapezoid')
        i = i+el
        x += el
        ab = []
        ordi = []
    elif(el%3 == 2 and el<3):
        I += Simp13(X, Fx, i+el, i)
        k = i
        while(k<=i+el):
            ab.append(X[k])
            ordi.append(Fx[k])
            k += 1
        plt.fill_between(x=ab, y1=0, y2=ordi, color='aqua', label='Simpson1/3')
        i = i+el
        y += el
        ab = []
        ordi = []
        
plt.scatter(X, Fx, color = 'brown')
plt.legend()
print("Trapeziod:", end=" ")
print(x, end=" intervals\n")

print("1/3 rule:", end=" ")
print(y, end=" intervals\n")

print("3/8 rule:", end=" ")
print(z, end=" intervals\n\n")

print("Integral value:", end=' ')
I = "{:.5f}".format(I)
print(I)
plt.show()