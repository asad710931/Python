
nums_list=[2,3,4,6,3,22,77,65,4,5,22,0]
#solution 1
#give maximum value from list
def max1(nums):
    rnum=0
    for num in nums:
        if(rnum<num):
           rnum=num
    return rnum

#solution 2
#give minimum value from list
def min1(nums):
    rnum=10000000000000000
    for num in nums:
        if(rnum>num):
           rnum=num
    return rnum


print(max1(nums_list))
print(min1(nums_list))
#solution 3
#remove duplicate numbers
def delDup(nums):
    new_list=[]
    for num in nums:
        if(num not in new_list):
            new_list.append(num)
    return new_list

print(delDup(nums_list))
#solution 4
#convert number into string
number=input("Enter number:")

numToWord={
    '0':'zero',
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
output=''
for num in number:
    output+=numToWord.get(num,'')+" "
print(output)
#exception handling


while True:
    try:
        inp=int(input('Enter a number:?'))
        break
    except ValueError:
        print("You didn't enter a number" )
    except:
        print("an unknown error occurred")
print("thank you")




