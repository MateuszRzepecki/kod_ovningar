from math import * 

def barn():
    antalbarn = 0
    n = 0
    while n<12:
        n = n + 1
        antalbarn = antalbarn + 4000 + 2000 * cos(pi*n/6)
    print (antalbarn)
barn()

m = 0
summa = 0 
while m < 179:
    degree = sin(radians(m))   
    m = m + 1
     
print(degree)


