def forwardElimination(A, n, L):
    lim = 0
    for m in range(0, n-1):
        lim += 1
        for i in range(lim, n):
            c = A[i][m]
            x = c/A[m][m]
            solveL(L, i, m, x)
            for j in range(0, n):
                A[i][j] = A[i][j] - (A[m][j]/A[m][m])*c
 
def solveL(L, i, j, x):
    L[i][j] = x
          
    
def forwardSubs(M, n, t, L, B, x):    
    if(t == 0):
        y = (B[0][0])
        x = y
    else:
        y = (B[t][0] - (L[t][0])*x)
        for i in range(1, t):
            y = y - M[i][0]*L[t][i]
        
    M[t][0] = y
    if(t+1==n):
        return
    forwardSubs(M, n, t+1, L, B, x)


def BackSubs(X, n, t, U, Y, y, c):
    if(t==n-1):
        x = (Y[n-1][0])/U[n-1][n-1]
        y = x
    else:
        x = (Y[t][0]-U[t][n-1]*y)
        for i in range(n-2, -1, -1):
            x = x - X[i][0]*U[t][i]
        x = x/U[t][n-c]

    X[t][0] = x
    if(t-1 < 0):
        return
    BackSubs(X, n, t-1, U, Y, y, c+1)


def isSolution(U):
    res = U.any(axis=1)
    for item in res:
        if(item == False):
            return item
    return item

rf = open('in1.txt', 'r')
n = int(rf.readline(), 10)
rf.seek(3)
matrix = []
it = 0
for line in rf:
    matrix.append((line.split()))
    it += 1
    if(it == n):
        break
    
import numpy as np 
#np.set_printoptions(formatter={'float': lambda x: "{0:0.4f}".format(x)})
matrix = np.array(matrix)

A = matrix.astype(np.float)

matrix = [[0 for c in range(1)] for r in range(n)]
for i in range(n):
    st = float(rf.readline())
    matrix[i][0] = st

rf.close()

matrix = np.array(matrix)
B = matrix.astype(np.float)

matrix = [[0 for c in range(n)] for r in range(n)]
for i in range(n):
     matrix[i][i] = float(1)
L = np.array(matrix)

forwardElimination(A, n, L)

verdict = isSolution(A)

wf = open('out1.txt', 'w')

i = 0
for r in range(n):
    if(r != 0):
        wf.write('\n')
    i = 0
    while(i<n):
        c = L[r][i]
        upto = "{:.4f}".format(c)
        p = (str(upto))
        wf.write(p)
        wf.write(" ")
        i += 1

wf.write('\n' + '\n')

for r in range(n):
    if(r != 0):
        wf.write('\n')
    i = 0
    while(i<n):
        c = A[r][i]
        upto = "{:.4f}".format(c)
        p = (str(upto))
        wf.write(p)
        wf.write(" ")
        i += 1

wf.write('\n' + '\n')

if(verdict == True):    
    matrix = [[0 for c in range(1)] for r in range(n)]
    Y = np.array(matrix)
    X = np.array(matrix)
    X = X.astype('float64')
    Y = Y.astype('float64')
    
    x=0
    forwardSubs(Y, n, 0, L, B, x)

    c=1
    x=0
    BackSubs(X, n, n-1, A, Y, x, c)
    print('\n')
    
    for r in range(n):
        if(r != 0):
            wf.write('\n')
        i = 0
        while(i<1):
            c = Y[r][i]
            upto = "{:.4f}".format(c)
            p = (str(upto))
            wf.write(p)
            i += 1

    wf.write('\n\n')
    
    for r in range(n):
        if(r != 0):
            wf.write('\n')
        i = 0
        while(i<1):
            c = X[r][i]
            upto = "{:.4f}".format(c)
            p = (str(upto))
            wf.write(p)
            i += 1
    
    wf.write('\n\n')
        
    wf.close()
else:
    wf.write('No unique solution')
    wf.close
    sys.exit(0)