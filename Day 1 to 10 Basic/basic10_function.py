from functools import reduce
import sys
import os
import math
from threading import Thread
''' '''
def name(e):
    r_value='Your name: {}'.format(e)
    return r_value
print(name("asad"))

def squre(n):
    return n*n
print(squre(4))

def get_sum(num1:int=0,num2:int=0):
    return num1+num2

def get_mult(*args):
    sum=0
    for arg in args:
        sum +=arg
    return sum
print(get_mult(1,2,3,3))

#return multiple values
def get_mvalue(n):
    return n + 1, n+3, n+4

l1,l2,l3=get_mvalue(1)
print(l1,l2,l3)

def mult_by(num):
    return lambda x:x*num

print(mult_by(5)(2))

print("++++++++++")

# function with function
def mult_list(list,func):
    for l in list:
        print(func(l))

mult_by_4=mult_by(4)
mult_list(list(range(0,5)),mult_by_4)

#multiple function list
power_list = [lambda x:x**2,
              lambda x:x**3]

print(power_list[0](3))
print(power_list[-1](3))
print()



print("=============MAP===============")
l1=range(1,10)
times2=lambda x:x*2
print(list(map(times2,l1)))


def myMap(x):
    return x

mapl=map(myMap,('apple','bread','rice','chicken'))

for m in mapl:
    print(m)


foods_list=[
    ("Rice",10),
    ("chicken",15),
    ("Veg",11)
]  

print(len(foods_list[0]))
print("+---------+")

for f in range(len(foods_list)):
    for g in range(len(foods_list[0])):
        print(foods_list[f][g]) 



def foods(n):
    return n[0]


food=list(map(lambda n:n[0],foods_list))

print(food)

print("===========filter===========")

noteList=filter(lambda x: x<=10,(10,9,33,56,2,3,4,3,2))
noteList1=[10,0,83,9,7,94,90,2]

def filtered(x):
    return x<10

fil=filter(filtered,noteList1)
print(list(fil))
print(list(noteList))



noteList2=['audio','document','video','picture','others']

print(list(filter(lambda x:'o' in x,noteList2)))

#reduce
print("========Reduce========")



print(reduce((lambda x,y:x+y),range(0,6)))




