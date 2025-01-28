from math import floor as f, radians
import math
num1=332
num2=345.008

#math function 
#give as max value from list of values
print("max : ",max(num1,num2,455,67,90))
#give min value from list of values
print("min :",min(num1,num2,455,67,90))
#absolute value turn nagetive num to positive  
print("abs(-1):",abs(-81))
#power multiplies fist number with time second number
print("pow(5,2) :",pow(5,2))
#round off the number removing number after dot if number (after dot) is equel or greather than .5 +1 with abs number or
#keep abs number
print("round(5.6):",round(5.4))
print("ceil(5.002) :",math.ceil(5.100))
print("floor(5.5) :",math.floor(5.9))
print("exp(1) :",math.exp(0))
print("sqrt(100) :",math.sqrt(10))
print('log(e) :',math.log(math.exp(10)))
print("log(100) : ",math.log(100,10))
print("radians(1) :",math.radians(1))
print("hypot(0) :",math.hypot(1,1))
print("degrees :",math.degrees(3))
print("pi:",math.pi)

print(math.inf<0)
print(math.inf-math.inf)
#===================random===============

print("==============Random===========")
import random

print(int(random.random()*100))

for h in range(5):
    print(int(random.random()*100))

names=['john','ali','haider','kader']

print(random.choice(names))

class Dice:
    def roll():
        x,y = random.randint(1,6),random.randint(1,6)
        return x,y

print(Dice.roll())

