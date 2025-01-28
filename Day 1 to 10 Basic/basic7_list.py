import sys
import os


list1 = [28,'tarek',5.11,True]

print(list1[0:-1:3])
print(list1)

print("length",len(list1))

print("1st ",list1[0])

print("last ",list1[-1])

print(list1[0:len(list1)])

print(list1[0:-1])

list1[0]=26

list2=['brown',224]

list3=list1+list2

list1[2:4]=[6.88,True]
list1[2:2]=[7.88,True]
print(list1)
list3.remove('brown')
list3.pop(4)
print(list3)
m_list=[['asad',25,False],
        ['sabed',12,False],
        ['sahed',34,True]]

print(m_list[0:len(m_list)][1])
print('asad' in m_list)
print('max:',max([2,4,5]))
print('min:',min(1,4,0))
print('reverse:',list1[::-1])




print("=========list========")
numbers=[2,3,2,4,5,8,9,7,0]

#add new item on list
numbers.append(10)
#make copy of list
numbers2=numbers.copy()
#insert a new value in desire index
numbers.insert(0,1)
print(numbers)

#sort out list value
numbers.sort()
print(numbers)
#reverse the value in the list
""
numbers.reverse()
print(numbers)

#count how many index with same values exist in the list 
print(numbers.count(2))



numbers.clear()

