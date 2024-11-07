import numpy as np

# a = np.array([1,2,3,4])
# print("shape : ",a.shape)
# print(a)


# zero_array = np.zeros((2,2))
# print(zero_array)

# c = np.full((2, 2), 7)
# print(c) 

# random_value_array = np.random.random((2,2))
# print(random_value_array)

# a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# print(a[0,1])

# col1 = a[:, 1]
# col2 = a[:, 1:2]
# print(col1)
# print(col2)
# copy do,nt chnage orignal array but in view chnage in view will also effect in orignal array
# a = np.array([1,2,3,4])
# b = a.copy()
# b[0] = 21
# b[1] = 54
# a[2] = 3435
# print(id(a))
# print(id(b))

# print(a)
# print(b)

# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# b = a.reshape(4,3)
# print(b)


# x = a.reshape(2,3,2,1)
# print(x)

# y = x.reshape(-1)
# print(y)

# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])

# xyz = np.concatenate((arr1,arr2), axis=0)
# print(xyz)

arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr)
# newarr = np.array_split(arr, 3)
# print(newarr)

x = np.where(arr == 4)
print(x)
