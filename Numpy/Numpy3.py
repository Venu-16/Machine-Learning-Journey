import numpy as np
from torch.cuda.nccl import broadcast
#arithmetic  operations
a = np.array([1,2,3,4,5,9,8,3])
b = np.array([1,2,3,4,5,6,7,8])

add_r = a+b
sub_r = a-b
mul_r = a*b
div_r = a/b

print(add_r)
print(sub_r)
print(mul_r)
print(div_r)


#broadcasting : Broadcasting allows operations on arrays of different shapes without explicitly replicating them.
c =a*2
print(c)

#Broadcasting with Different Shapes

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([10,11,13])

res = arr2+arr1
print(res)

"""
Universal Functions (ufuncs)
These are optimized functions
that operate element-wise on NumPy arrays.

Common ufuncs:
Function	Description
np.exp(x)	Exponential (eˣ)
np.sqrt(x)	Square root
np.log(x)	Natural logarithm (ln x)
np.abs(x)	Absolute value
np.sin(x)
np.cos(x)
np.tan(x)	Trigonometric functions
np.round(x, decimals=n)	Rounding

Key Point: ufuncs are much faster than using for loops.
"""

a = np.array([3,4,5,6,8])

print("sq root", np.sqrt(a))
print("exponential", np.exp(a))
print("Logarithm", np.log(a))
print("Absolute value",np.abs(-43))
print("sin , cos ,tan ",np.sin(a),np.cos(a),np.tan(a) )
print("rounding", np.round(43.9879, 2))

"""
 Aggregation Functions
Aggregation functions compute summary statistics over arrays.

Common Aggregation Functions:
Function	  Description
np.sum(x)	  Sum of all elements
np.mean(x)	  Mean (average)
np.min(x)
np.max(x)	  Minimum and maximum values
np.median(x)	Median value
np.std(x)       Standard deviation 
np.var(x)	  variance

 Key Point: These functions help analyze data efficiently.
"""

arr = np.array([10,20,30,40,50])
print("sum", np.sum(arr))
print("mean ", np.mean(arr))
print("min value",np.min(arr))
print("max value", np.max(arr))
print("median", np.median(arr))
print("Standard deviavtion: ", np.std(arr))


"""------------------|--------------------------------|----------------------------------------|
| Category           |	Function                      |  	Description                        |
|--------------------|--------------------------------|----------------------------------------|
| Arithmetic         |    +, -, *, /	              | Element-wise operations                |
| Broadcasting       |    arr + scalar                |	Operations on different shaped arrays  |
| Universal Functions|	np.exp(), np.log(), np.sqrt() |	Element-wise mathematical operations   |
| Aggregations       |	np.sum(), np.mean(), np.std() |	Summary statistics                     |
|--------------------|--------------------------------|----------------------------------------|"""

