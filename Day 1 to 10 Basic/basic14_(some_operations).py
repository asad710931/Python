

#Work with one liner loops

numslist=[x+1 for x in range(10)]
#print(numslist)
squres=[x**2 for x in range(10)]
#print(squres)

cubic=[x**3 for x in range(10)]
#print(cubic)


#operate list in single line loop
#list,tuples
nums=[3,4,3,2,5,10,34,8,15]

num=[x*2 for x in nums]
# print(num)

#get odd and even numbers only
evens=[x for x in range(100) if x%2==0]
odd=[x for x in range(100) if x%2!=0]

# print(f"Even: {evens} \nOdd: {odd}")

# ======== lamda buildin python function is one line smaller function for limited and smaller tasks

squreOfNumer=lambda x:x*x
squreOfNumer1=lambda x:x**2

#print(squreOfNumer(16),squreOfNumer1(16))
sumOfNums=lambda x,y,z : sum([x,y,z])

# print(sumOfNums(2,3,44))

# map,filter,reduce

foods=["Mix Veg","Rice","Beef","Chicken","Milk"]
#print(foods)

map1=map(str.upper,foods)
map2=map(lambda s:s[-1],foods)
map3=map(lambda s:f'{s}-> Good',foods)
# print(list(map3))


#filter 
filter1=filter(lambda x:'i'in x,foods)
filter2=filter(lambda x: x>=14,nums)

#print(list(filter2))

# reduce function


from functools import reduce as rd

someNums=[1,3,4,5,6]
sumofRd=rd(lambda a,b:a+b,someNums)
sumo=rd(lambda a,b:f"{a} {b}",foods)
print(sumo)






