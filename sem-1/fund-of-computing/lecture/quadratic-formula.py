#Brandon Perez
#Quadratic Formula that WORKS

import math

def quad():
    print("insert corresponding values: ax^2+bx+c")
    a = eval(input("a: "))
    b = eval(input("b: "))
    c = eval(input("c: "))

    sqrtSect = b*b - 4*a*c
    signOfSect = math.copysign(1, sqrtSect)
    sqrtSect = math.sqrt((sqrtSect+(sqrtSect*signOfSect))/2)

    x1 = (-b + sqrtSect) / (2*a)
    x2 = (-b - sqrtSect) / (2*a)

    check = a*x1*x1+b*x1+c

    print(f"\nx = {x1} ; x = {x2} \nsolution is not imaginary as long as this says 0: {check}")
    
