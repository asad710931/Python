import sys
import os
import math
from threading import Thread
''' '''


x=0

while x<10:
    print('Looping:',x)
    x += 1

i=0
while i<20:
    if i % 2==0:
        print(i)
    elif i==19:
        print('got 19')
        break
    else:
        i += 1
        continue
    i +=1


onUser=True
books=['c','c++','c#','java','python']
price=[222,230,190,100,99]

print('we have c,c++,java,python')
book=input('Enter name of book:')

while onUser:   
    if book.lower()=='quit':
        onUser=False
        #break
    else:
        for i in range(len(books)):
            if book.lower()==books[i]:
                print('You looking for {} it will be {} taka'.format(books[i],price[i]))
                break
            i+=1
        book=input('Enter name of book:')


li=[34,45,True,'looping']
i=0
while len(li):
    print(li.pop(0))

#for loop
for x in range(0,10):
    print(x,' ',end='')
print()

l1=[2,4,5,6,'junk']
for i in l1:
    print(i,'  ',end='')
print()    

for j in ['asad',25,True]:
    print(j,end="\' \'")
#iterator as iter 
l3=[2,4,5,'Asad']
itr=iter(l3)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
#range as list
l2=list(range(0,3))
print(l2)

oneToTen= range(1,11)
print(oneToTen)


b_list=[2,4,5,6],[5,3,2,3],[4,6,2,4]
for x in range(0,3):
    for y in range(0,4):
        print(b_list[x][y]*b_list[x][y],end=' ')
    print()



