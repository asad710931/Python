import sys
import os
import math
from threading import Thread


#tuble like list but cant change values
print("===========Python Tubles=============")
t1=('Asad',25,5.93,True)
print('length : ',len(t1))
print('1st : ',t1[0])
print('last : ',t1[-1])
print('from 2nd one to two',t1[1:3])
print('every other : ',t1[0:-1:2] )
print('reverse : ',t1[::-1])
print(end="\n\n\n")

#python Dictionary
print("=========python Dictionary==========")
person={
    "doc":"korshed",
    "eng":"shaiful",
    "driver":"Rajo"
}
#add new person
person["teacher"]="anamul"
person["driver"]="rajo"
print('Doc : ',person["doc"])
print('Driver : ',person["driver"])
print('Teacher : ',person["teacher"])
print('length : ',len(person))
print('List : ',list(person.items()))
print('keys : ',list(person.keys()))
print('values : ',list(person.values()))
del person['driver']
print('List : ',list(person.items()))
print(person.pop("teacher"))
print("anamul" in person)

for p in person:
    print('person: ', p, end=", ")
print()
for v in person.values():
    print('Values: ',v,end=", ") 
print()
for k in person.keys():
    print('keys : ', k,end=", ")
print()



#another way to dictionary
person1=dict([
    ("name","Asad"),
    ("age",25),
    ("Occupation","programmer")
])
    
print("%(name)s he is %(age)d year old" % person1)

# python set
print("==========Python Set")

s1=set(["sabed",2,4])
s2=set(["asad",3,4])

#join sets
s3=s1|s2
print("length:",len(s3))

#add new data on sets
s3.add('atik')
print(s3)
#remove from sets
s3.discard('asad')
print(s3)
#remove random set
print(s3.pop())
#return common value
print(s1.intersection(s2))
#return non-common value
print(s1.symmetric_difference(s2))

#add value whois is not exist in s3 from s2
s3 |= s2
print(s3)

#clear sets
s3.clear()
print(s3)
s4=frozenset(['dougles',8])
print(s4)







