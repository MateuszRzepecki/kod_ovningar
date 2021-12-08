from math import * 

def f(x): 
    return sin(x)

def f_prim(x):
    h = 0.001
    return (f(x + h) - f(x)) / h

x = 0.5

while abs(f(x)) >= 0.01:
    x = x - f(x)/x
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




