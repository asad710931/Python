
import numpy as np

# =========math operator==========
arr1=[1,2,3,4,5,6,7,8,9]
x=[1,2,3]
y=[4,5,6]
z=np.array([7,8,9])
e1=np.array([2,4,6])

print(f"Add: {(np.array(x)+np.array(y))}")
print(np.array(x)-np.array(y))
print(np.array(x)*np.array(y))
print(np.array(x)/np.array(y))
print("===============")
print(z+z)
print(z-z)
print(z/z)
print(z*z)
print("Module : {0} Add: {1}".format(z%e1,z+z))

# buildin method in numpy
print(np.sqrt(y))
print(np.sum(x+y))
print(np.mean(x))
print(np.max(x))
print(np.min(x))
print(np.average(arr1))
print(np.abs([9.560,8.988098009001,7]))
print(np.absolute([9.560,8.988098009001,7]))
print(np.round([9.560,8.988098009001,7],2))
print(np.ceil([9.460,8.988098009001,7]))
print(np.floor([9.560,8.988098009001,7]))