import numpy as np

arr1=[1,2,3,4,5,6,7,8,9]
x=[1,2,3]
y=[4,5,6]
z=np.array([7,8,9])
my_numers=np.array([2,4,6,6,10,0,12])

print(my_numers[5])
print(my_numers[0:5])
print(my_numers[-1])
print(my_numers[:4])
print(my_numers[3:])

# creating array with np.arange
matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2=np.array([[3,8,9],[6,7,4],[2,5,1]])

print("Original Matrix")
print(matrix)
print("transpose Matrix")
print(matrix.T)

print(f"Add :\n {matrix+matrix2}")
print(f"Sub :\n {matrix-matrix2}")
print(f"Mul :\n {matrix*matrix2}")
print(f"Div :\n {matrix/matrix2}")
print(f"Mod :\n {matrix%matrix2}")










