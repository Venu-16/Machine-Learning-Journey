"""
reshape() function gives a new shape to an array without changing its data.
resize() function return a new array with the specified shape.
"""
import numpy as np
# help(np.reshape)
a = np.arange(1,7)
print(a.shape)
print(a)
b= np.reshape(a,(3,2),"F")
print(b)

# help(np.resize)
c = np.arange(18)
d=np.resize(c,(3,3,2))
print(d)

"""
flatten() return a copy of the array collapsed into one dimension"""

a = np.array([[5,6],[7,8]])
print(a)
print(a.flatten())
print(a.flatten("F"))

"""
ravel()
used to change a 2-dimensional array or a multi-dimensional array into 
a contiguous flattened array."""
# help(np.ravel)
k = np.array([[5,6,4],[7,8,7],[4,5,3]])
print(k)
print(np.ravel(k,"F"))

"""
transpose() function is nothing but transpose operation in matrix
"""
# help(np.transpose)
a = np.array([[1, 2], [3, 4]])
np.transpose(a)
print(a, "Transpose")


"""Vertical Stacking (np.vstack())
Stacks arrays on top of each other (row-wise stacking)
Requires that the number of columns must be the same in all arrays."""
p = np.array([[1,2],[3,4]])
v = np.array([[5,6],[7,8]])
print(np.vstack((p,v)),"vstack")

""" Horizontal Stacking (np.hstack())
Stacks arrays side by side (column-wise stacking)
Requires that the number of rows must be the same in all arrays.
"""
p = np.array([[1,2],[3,4]])
v = np.array([[5,6],[7,8]])
print(np.hstack((p,v)),"hstack")




"""
swapaxes(): This function interchanges the two axes of an array.
"""
# help(np.swapaxes)
a = np.array([[11,2],[33,65]])
print(a)
print(np.swapaxes(a,0,1))

b = np.array([[1,2,3]])
print(np.swapaxes(b,1,0))

"""
concatenate function
"""
# help(np.concatenate)
p = np.arange(1,6)
v = np.arange(6)
print(p)
print(v)
print(np.concatenate((p,v)))

m = np.arange(4)
print(np.concatenate((p,v,m)))

"""
Matrix addition and transpose"""

p = np.array([[1,2],[3,4]])
v = np.array([[5,6],[7,8]])
print(p)
print(v)
print(p+v)

"""Matrix Multiplication"""
p = np.array([[1,2],[3,4]])
v = np.array([[5,6],[7,8]])
m = np.matmul(p,v)
print(m)
print(np.dot(p,v))
# help(np.dot)
# help(np.matmul)

"""linalg"""

p = np.array([[1,2],[3,4]])
v = np.array([[5,6],[7,8]])
# help(np.linalg.inv)
print(np.linalg.inv(p))
# help(np.linalg)

m = np.array([5,6,7,8])
# print(np.linalg.inv)
"""powerofmat"""


v = np.array([[5,6],[7,8]])

p = np.linalg.matrix_power(v,3)
print(p)
"""det"""
print(np.linalg.det(p))


# help(np.vstack)

"""Changing data types (arr.astype())"""
a = np.array([1,2,3,4])
c = a.astype(float)
d = a.astype(complex)
print(d)
print(c)


#Eigenvalues and eigenvectors (np.linalg.eig())

a = np.array([[1,3,6],[2,3,4],[3,6,7]])
print(np.linalg.eig(a))

#Solving linear equations (np.linalg.solve())

a = np.array([[1,3,6],[2,3,4],[3,6,7]])
b = np.array([[1],[2],[3]])
print(np.linalg.solve(a,b))

