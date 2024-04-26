def lnOnePlusX(x, n):
    sum = 0
    for i in range(n):
        if i%2==0:
            sum = sum + (x**(i+1))/(i+1)
        else:
            sum = sum - (x**(i+1))/(i+1)
    return sum

#Answer of 1(a)
    
print("1(a)")    
x = float(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))
print("ln(1+x) = ", end="")
print(lnOnePlusX(x, n))

from matplotlib import pyplot as plt
import math as m

#Answer of 1(b)

print("1(b)")
x = -1 + .1
X = list()
Y = list()
    
while x <= 1:
    X.append(x)
    Y.append(m.log(1+x))
    x += .1

plt.xlim(-1, 1)    
plt.plot(X, Y)
plt.title('Graph of ln(1+x) using built in function')
plt.ylabel("ln(1+x)")
plt.xlabel("x")
plt.legend()
plt.show()

#Answer of 1(c)

print("1(c)")
Y1 = list()
Y3 = list()
Y5 = list()
Y20 = list()
Y50 = list()
nOfT = [1, 3, 5, 20, 50]

for x in X:
    Y1.append(lnOnePlusX(x, 1))
plt.plot(X, Y1, label = "term = 1", color = "red")

for x in X:
    Y3.append(lnOnePlusX(x, 3))
plt.plot(X, Y3, label = "term = 3", color = "indigo")

for x in X:
    Y5.append(lnOnePlusX(x, 5))
plt.plot(X, Y5, label = "term = 5", color = "yellow")

for x in X:
    Y20.append(lnOnePlusX(x, 20))
plt.plot(X, Y20, label = "term = 20", color = "maroon")

for x in X:
    Y50.append(lnOnePlusX(x, 50))
plt.plot(X, Y50, label = "term = 50", color = "grey")
    
plt.plot(X, Y, label ="real value", color = "green")
plt.xlabel('x')
plt.ylabel('ln(1+x)')
plt.xlim(-1, 1)
plt.legend()
plt.show()

#Answer of 1(d)

print("1(d)")
X.clear()
Y.clear()
i = 0
for i in range(49):
    result = abs((lnOnePlusX(.5, i+1) - lnOnePlusX(.5, i))/(lnOnePlusX(.5, i+1)))
    Y.append(result)
    X.append(i)

plt.plot(X, Y)
plt.title("Relative Approximate error")
plt.xlabel("number of iteration")
plt.ylabel("Error / true value")
plt.show()