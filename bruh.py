from math import * 

def f(x): 
    return (x - sin(x)) / x 

def f_prim(x):
    h = 0.001
    return (f(x + h) - f(x)) / h

x = 0.0001

while abs(f(x)) <= 0.01:
    x = x - f(x)
    print(x)

print("Den sökta roten är x =", x)






# def barn():
    # antalbarn = 0
    # n = 0
    # while n<12:
    # n = n + 1
        # antalbarn = antalbarn + 4000 + 2000 * cos(pi*n/6)
    # print (antalbarn)
# barn()




