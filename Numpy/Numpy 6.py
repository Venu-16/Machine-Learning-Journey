""" Random Number Generation
Generating random numbers (np.random.rand(), np.random.randint(), np.random.randn())
Setting random seed (np.random.seed())"""

"""
Generating Random Numbers
NumPy’s np.random module provides different ways to generate random numbers.
Uniform Random Numbers (np.random.rand())
Generates random floats between 0 and 1 (from a uniform distribution)."""

import numpy as np
ran_num = np.random.rand(5)
print(ran_num)

#np.random.randint()
rand_int = np.random.randint(1,10, size=5)
print(rand_int)

#np.random.randn()
random_normal = np.random.randn(5)
print(random_normal)

"""Setting a Random Seed (np.random.seed())
A random seed ensures that the same random numbers 
are generated every time, making results reproducible."""

np.random.seed(42)
ran = np.random.rand(3)
print(ran)

