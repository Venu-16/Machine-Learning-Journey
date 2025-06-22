"""Statistical & Probability Functions in NumPy
NumPy provides built-in functions for statistical analysis and probability calculations, including measures of central tendency, dispersion,
and relationships between variables."""
from statistics import median

import numpy as np
#Mean, Median, Variance, and Standard Deviation
a = np.array([10,20,30,40,50])
mean_val = np.mean(a)
print(mean_val)
median_val = np.median(a)
print(median_val)
var_val = np.var(a)
print(var_val)
Std_val = np.std(a)
print(Std_val)

#Percentiles and Quantiles

# help(np.percentile)

q25 = np.percentile(a, 25)
q50 = np.percentile(a, 50)
q75 = np.percentile(a, 75)

print("25 percentile:",q25)
print("50 percentile(median): ",q50)
print("75 percentile:",q75)

"""Quantiles (np.quantile())
Similar to percentiles but expressed as fractions."""

q1 = np.quantile(a, 0.25)
q2 = np.quantile(a, 0.5)
q3 = np.quantile(a, 0.75)

print(q1,q2,q3)


"""Correlation and Covariance
 Correlation (np.corrcoef())
Measures the relationship between two datasets.
Values range from -1 to 1:
+1: Strong positive correlation
0: No correlation
-1: Strong negative correlation"""

x = np.array([1,2,3,4,5])
y = np.array([6,7,8,9,10])
corre_mat = np.corrcoef(x,y)
print(corre_mat)

#covariance

cov_mat = np.cov(x,y)
print(cov_mat)

"""
 Summary Table
Function	             Description
np.mean(arr)	        Mean (average)
np.median(arr)          Median (middle value)
np.var(arr)	            Variance (spread of data)
np.std(arr)	            Standard deviation (variation from mean)
np.percentile(arr, p) 	pth percentile (e.g., Q1, Q3)
np.quantile(arr, q)	    Quantile (same as percentile but in fractions)
np.corrcoef(x, y)	    Correlation coefficient (-1 to 1)
np.cov(x, y)	        Covariance (measure of joint variability)"""