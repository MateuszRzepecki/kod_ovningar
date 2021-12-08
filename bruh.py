from math import * 

def f(x): 
    return 5*cos(x) - (4*x)

def f_prim(x):
    h = 0.001
    return (f(x + h) - f(x)) / h

x = 0.5

while abs(f(x)) >= 0.0000001:
    x = x - f(x)/f_prim(x)
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




