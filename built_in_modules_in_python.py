#Python built in modules are math, random, Time, Threading

import math
print(dir(math))

#to see all the modules in maths
l = dir(math)
for i in l:
    print(i)

#to see value of modules in math
import math as m
print(m.pi)
print(m.e)
print(m.pow(2, 3))

#to import specific modules 
from math import pi , pow , e

print(pi)
print(e)
print(pow(3, 5))

#to import all the module form math
from math import *
print(sqrt(25))


import math

print(math.sqrt(25))
print(math.floor(25.57))    #gives the gratest integer
print(math.ceil(25.57))     #give next int as output
print(math.pow(2, 5))       #convert 2 power 5 which is 32
print(math.gcd(24, 78))     #gives gratest comman divisor
print(math.sin(1))          #give value of sin1
print(math.cos(1))
print(math.pi)              #give the value of pi

#creating a program that calculate area of circle
import math

r = float(input("Enter Radius:"))
print(math.pi*r**2)
print(math.pi*r*r)
print(math.pi*math.pow(r, 2))