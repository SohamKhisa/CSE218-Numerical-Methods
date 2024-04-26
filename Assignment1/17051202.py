#Graphical model to estimate the value

from matplotlib import pyplot as plt

X = list()
Y = list()
zero = list()
x = .1

while x > -.1:
    X.append(x)
    y = (x**3) - ((6*(100**2))/25) * (x**2) - 3*x + 2 
    Y.append(y)
    zero.append(0)
    x-=.01
  
plt.plot(X, zero)
plt.plot(zero, Y)   
plt.plot(X, Y)
plt.title('Graphical method')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
print('From the graph we can see that .028 is a root')
print('\n')

def RelativeErr(a, b):
    return (a-b)/a * 100

#Secant method

def function(n):
    return (n**3) - ((6*(100**2))/25) * (n**2) - 3*n + 2 

def secMethod(f, guess1, guess2, approxEr, maxIter):
    count = 0
    c = 0
    flg = -1
    if(f(guess1) * f(guess2) < 0):
        while count < maxIter:
            if f(guess1) == f(guess2):
                print('no solution')
            c = (guess1*f(guess2) - guess2*f(guess1))/(f(guess2) - f(guess1))
            guess1 = guess2
            guess2 = c
            count += 1
            if abs(RelativeErr(guess2, guess1)) < approxEr:
                flg = 1
                break
    else:
        print('initial guesses are not correct')
        
    print('maximum iteration using secant method : ')
    print(count)
    print('the root of the function using secant method : ')
    if flg == 1:
        return c

#flase position method

    
def fpMethod(fun, lowB, UpB, approxEr, maxIter):
    i = 0
    flg= -1
    x = 0
    if(fun(lowB) * fun(UpB) < 0):
        while i < maxIter:
            if fun(lowB) == fun(UpB):
                print('No solution')
            x = (lowB*fun(UpB) - UpB*fun(lowB))/(fun(UpB) - fun(lowB))
            i += 1
            err = abs(RelativeErr(x, lowB))
            if fun(x) == 0:
                flg = 1
                break
            elif fun(x) * fun(lowB) < 0:
                UpB = x
            else:
                lowB = x
            if err < approxEr:
                flg = 1
                break
    else:
        print('wrong lower bound or wrong upper bound')
    print('maximum iteration using false position method: ')
    print(i)
    print('the root of the function using false position method : ')
    if flg == 1:
        return x

print(secMethod(function, 0, .5, .5, 100))
print('\n')
print(fpMethod(function, 0, .7, .5, 100))