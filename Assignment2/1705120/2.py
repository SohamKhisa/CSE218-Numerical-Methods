def calculation(Tab, Z, n, m, S):
    
    count = 0
    for item in Z:
        if(item >= 0):
            count += 1
    if(count == (m+n)):
        return
    else:
        Z1 = np.round(Z, 2)
        Tab1 = np.round(Tab, 2)
        print(Z1)
        print(Tab1)
        miniC = 0
        for i in range(1, n+m):
            if(Z[miniC] > Z[i]):
                miniC = i
        
        for i in range(n):                          #to find the intercepts
            x = Tab[i][m+n-1]/Tab[i][miniC]
            Tab[i][m+n] = x
            
            miniR = 0
            for i in range(1, n):
                if(Tab[miniR][m+n] > Tab[i][m+n]):
                    miniR = i
        
        x = Tab[miniR][miniC]
        for i in range(m+n):
            Tab[miniR][i] = Tab[miniR][i]/x
    
        print("\n")
        Z1 = np.round(Z, 2)
        Tab1 = np.round(Tab, 2)
        print(Z1)
        print(Tab1)
        r = miniR    
        for i in range(n):
            c = Tab[i][0]/x
            if(i == miniR and miniR < (n-1)):
                i += 1
            elif(i == (n-1) and miniR == (n-1)):
                break
            for j in range(n+m):
                Tab[i][j] = Tab[i][j] - Tab[r][j]*c
    
        c = Z[0]/x

        for i in range(m+n):
            Z[i] = Z[i] - c*Tab[r][i]
        
        print("\n")
        Z1 = np.round(Z, 2)
        Tab1 = np.round(Tab, 2)
        print(Z1)
        print(Tab1)
        
        S[miniC] = Tab[miniR][m+n-1]
    calculation(Tab, Z, n, m, S)
        

    
import numpy as np
np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
rf = open('in2.txt', 'r')

Z = np.array(rf.readline().split())
Z = Z.astype('float64')

count = 0
for i in Z:
    count += 1

temp = []
n = 0

for line in rf:
    n += 1
    temp.append(line.split())

G = np.array(temp)
G = G.astype(np.float)
S = np.array(temp)
S = S.astype(np.float)

m = 0
for i in S[1]:
    m += 1

Tab = np.empty([n, (m+n+1)], dtype = float)         #table

zed = np.empty([m+n], dtype = float)                #Cj

for i in range(m+n):
    if(i < m-1):
        zed[i] = Z[i]*-1
    else:
        zed[i] = float(0)


for i in range(0, n):
    k = 0
    for j in range(m+n+1):
        if(k < m-1):
            Tab[i][j] = S[i][k]
            k += 1
        elif(j == m+n-1):
            Tab[i][j] = S[i][k]
        elif(j == m-1+i):
            Tab[i][j] = float(1)
        else:
            Tab[i][j] = float(0)

S = np.zeros([count], dtype = float)
calculation(Tab, zed, n, m, S)

print('\n')
List = []
List.append(zed[m+n-1])
for i in S:
    List.append(i)
    #List.append(Tab[i][m+n-1])
List1 = np.round(List, 2)
print(List1)

#bonus:
if(count == 2):
    import matplotlib.pyplot as plt
    X1 = []
    Y1 = []
    X0 = []
    Y0 = []
    plt.hlines(0,-200,1000,color='k')
    plt.vlines(0,-1000,1000,color='k')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Feasible region')
    plt.grid(True)
    for i in range(n+1):
        if(i != 0):
            plt.plot(X1, Y1)
        if(i == n):
            break
        del X1[:]
        del Y1[:]
        x = 0
        while(x<1000):
            y = (G[i][count]-G[i][0]*x)/G[i][1]
            X1.append(x)
            x += .1
            Y1.append(y)
        
    for i in range(n):
        X0.append(G[i][count]/G[i][0])
        Y0.append(G[i][count]/G[i][1])
        
    miniX = 0
    miniY = 0

    for i in range(1, n):
        if(X0[i]<X0[miniX] and X0[i]>0):
            miniX = i
        if(Y0[i]<Y0[miniY] and Y0[i]>0):
            miniY = i
       
    del X1[:]
    del Y1[:]
    if(miniX == miniY):
        SminX = 0
        SminY = 0
        if(miniX == 0):
            SminX = 1
            SminY = 1

        for i in range(1, n):
            if(i!=miniX):
                if(X0[i]<X0[SminX]):
                    SminX = i
                if(Y0[i]<Y0[SminY]):
                    SminY = i
        
        x = np.arange(0, 350, 0.1)
        y1 = (G[SminX][count] - G[SminX][0]*x)/G[SminX][1]
        y2 = (G[SminY][count] - G[SminY][0]*x)/G[SminY][1]
        y3 = (G[miniX][count] - G[miniX][0]*x)/G[miniX][1]
        
        y5 = np.minimum(y1, y2)
        y4 = np.zeros(350)
        bottom = np.maximum(y3, 0)
        plt.fill_between(x, y5, bottom, color='grey')
        plt.show()
        
    else:
        x = np.arange(0, 350, 0.1)
        y1 = (G[miniX][count] - G[miniX][0]*x)/G[miniX][1]
        y2 = (G[miniY][count] - G[miniY][0]*x)/G[miniY][1]
        
        y4 = np.zeroes(350)
        y3 = np.minimum(y1, y2)
        plt.fill_between(x, y4, y3, color = 'grey')
        plt.show()
        
        
        