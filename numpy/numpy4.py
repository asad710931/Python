import numpy as np

arr=np.array([1,2,3])
#print(arr+10)

matrix=np.array([[1,2,3],[4,5,6]])
vector=np.array([1,2,1])
print(matrix+vector)


print(np.average(matrix))
print(np.std(matrix))
print(np.sum(matrix,axis=1))
print(np.sum(matrix,axis=0))

np.random.seed(42)
random_arr=np.random.rand(3,3)
print(f"Random Array:\n{random_arr}")

random_int=np.random.randint(0,25, size=(5,5))
print(f"Random Integers:\n{random_int}")

random_int[random_int<10]=10
print(f"Random filtered Integers:\n{random_int}")




