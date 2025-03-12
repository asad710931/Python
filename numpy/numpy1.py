import numpy as np

# create array with numpy
arr=[2,3,1,4,5,6]

arr1=np.array(arr)
# print(arr)
numShape=np.array([[[1,3,8,5],[4,5,6,2],[4,5,6,2]],[[2,7,9,1],[2,7,9,1],[0,2,7,9]]])
print(numShape)
print(numShape.shape)
print(numShape.ndim)
print(numShape.size)
print(numShape.dtype)
print(numShape.itemsize)


# creating array of 0 to 24 as float type number within 2 dimension
newArray=np.array(range(24),dtype='float',ndmin=2)

print(newArray)
print(newArray.reshape((2,12)))
print(newArray.reshape((2,3,4)))

axis=newArray.reshape((2,12))[:,np.newaxis]

print(axis)
# np.zeros[3,2] and ones will create an matrix of 0/1 with 3 columns with 2 rows
zeroes=np.zeros([3,5])
zeroes2=np.zeros((3,3,2))
# print(zeroes)
ones1=np.ones((2,3))

#creating 3 to 9 array
arange_arr=np.arange(3,9)
print(f"arange \n {arange_arr}")
#np.arange will create a list of number from first value1 upto next value gives every 3 number in after
arange_arr=np.arange(0,20,2)
print(arange_arr)
#evenly spaced number from 1 to 10 evenly spread them 4 times
linspace_array=np.linspace(0,10,5)
print(linspace_array)

# reshape number

arr1=[1,2,3,4,5,6,7,8,9]
arr1=np.array(arr1)

# print(arr1.reshape((3,3)))
# print(np.array([1,2,3,4,5,6]).reshape((3,2)))
# print(np.array([1,2,3,4,5,6])[:,np.newaxis])

arr2=np.array(arr1)
expand=arr2[:,np.newaxis]
# print(arr2)
print(expand)







