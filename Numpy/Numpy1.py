import numpy as np
# help(np.array)
a=np.array([1,2,3,4,5])
print(a)
b = np.array([[1,2,3],[1,2,3]])
print(b)
c = np.array([1,2,3,4],"complex")
print(c)
"""
NumPy arange() is one of the array creatiom routines based on numerical ranges.
It creates an instance of ndarray with evenly space values and returns
the reference to it.
"""

#help(np.arange)

x = np.arange(5)
print(x)

y = np.arange(1,7)
print(y)

z = np.arange(1,9.0)
print(z)

s = np.arange(2,20,2)
print(s)

d = np.arange(10, dtype="complex")
print(d)

"""
The numpy.zeros() function returns a new array of given shape and type, with zeros.
----------------------------------------------------------------------
Ones() function returns a new of given shape and type, where the element's value is set to 1.
------------------------------------------------------------------------------
empty() return a new array of given shape and type, with random values.
"""
# help(np.zeros)
f = np.zeros(5)
print(f)

f = np.zeros(5, "int")
print(f)

f = np.zeros((2,3),"int")
print(f)

#Ones
# help(np.ones)
g = np.ones(4)
print(g)

g = np.ones(4,"int")
print(g)

g = np.ones((6,8))
print(g)

#empty()
# help(np.empty)
h = np.empty(3)
print(h)

h = np.empty(3,"int")
print(h)

h = np.empty([3,4], "int")
print(h)
#fill
x = np.full((2,3), 8)
print(x)

"""
Linespace():
linspace() function return evenly spaced number over a specified interval.
"""
# help(np.linspace)
h = np.linspace(0,100,num=9,dtype="int")
print(h)
b = np.linspace(1,50,num=5,endpoint=False)
print(b)

d = np.linspace(1,50,num=5,retstep=True)
print(d)

"""
identity() function return the identity array.
The identity array is a square array with ones
on the diagonal
-------------------------------------------------
eye() function return a 2-d array with 1's as 
the diagonal and 0's elsewhere"""
# help(np.identity)
c = np.identity(3)
print(c)
p = np.identity(3,"int")
print(p)

#eye
# help(np.eye)
a = np.eye(3)
print(a)

v = np.eye(2,4)
print(v)
e = np.eye(3, k=-1)
print(e)

n = np.eye(3, k=1)
print(n)

u = np.eye(3,k=1, dtype="int")
print(u)

#Attributes of array
#---Dimension------
m = np.array([1,2,3,4,5])
print(m.ndim)

b = np.array([[1,2],[2,3]])
print(b.ndim)

#-----shape----
print(b.shape)

#-----DataType---
print(m.dtype)

#-----size----
print(m.itemsize)

########-------------indexing of array---------------##############
r = np.array([9,8,7,6,5,4])
print(r[1])
a = np.array([[1,2],[2,3]])
print(a[0][0])



#slicing vm[st:end:step], st = 0 (default), end= len(vm) (default) , step = 1 (default)
i = np.array([9,8,7,6,5,4])
print(i[:3])
print(i[1::2])
print(i[1:6:2])

#Artimatic operations
s = np.arange(1,5)
print(s)
print(s+2)
print(s-2)
print(s*3)
print(s/3)
print(s**2)

y = np.array([[5,6],[7,8]])
print(y*2)
print(y[0]*2)


a = np.arange(1,5)
b = np.arange(5,9)
print(a+b)
print(a*b)


