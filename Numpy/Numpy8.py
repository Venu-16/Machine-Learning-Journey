"""Advanced NumPy Topics
Vectorization vs loops (Why NumPy is faster)
Memory layout (C_CONTIGUOUS, F_CONTIGUOUS)
NumPy performance optimization
Using numba and cython with NumPy for speed"""

"""Vectorization vs Loops (Why NumPy is Faster)
NumPy operations are vectorized, meaning they use optimized C and Fortran libraries instead of Python loops."""

import numpy as np

data = np.arange(1_000_000)

result = []
for x in data:
    result.append(x**2) #Using Python Loop (Slow)

result = data**2 #Using NumPy Vectorization (Fast)


"""Memory Layout (C_CONTIGUOUS vs F_CONTIGUOUS)
C_CONTIGUOUS (Row-major order) → Stored row-by-row (default in NumPy).
F_CONTIGUOUS (Column-major order) → Stored column-by-column."""

arr = np.array([[1, 2, 3], [4, 5, 6]], order='F')  # Column-major order

print(arr.flags['C_CONTIGUOUS'])  # False
print(arr.flags['F_CONTIGUOUS'])  # True


"""NumPy Performance Optimization
Use np.dot() for matrix multiplication instead of loops.
Use in-place operations (arr += 1) to reduce memory allocation.
Convert Python lists to NumPy arrays before performing calculations."""


"""Using numba and cython for Speed
numba – JIT Compilation for Fast Execution
Converts Python code to machine code for speed."""

from numba import jit
import numpy as np

@jit(nopython=True)
def fast_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

arr = np.random.rand(10**6)
print(fast_sum(arr))

"""
Function	     Purpose
np.loadtxt()	Read text/CSV files
np.savetxt()	Save arrays to text/CSV
np.genfromtxt()	Load text/CSV with missing values
np.save()	    Save arrays in binary format (.npy)
np.load()   	Load .npy files"""