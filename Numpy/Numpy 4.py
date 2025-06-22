""" Working with Missing Data
Identifying missing values (np.isnan())
Replacing missing values (np.nan_to_num())
"""
import numpy as np

a = np.array([45,np.nan,35,np.nan,65])
print(a)

missing_val = np.isnan(a)
print(missing_val)

"""Replacing Missing Values (np.nan_to_num())
The np.nan_to_num() function replaces NaN values 
with a specified number (default is 0)."""

cleaned_a = np.nan_to_num(a,nan=0)
print(cleaned_a)

#Replacing NaN with the Mean Value

mean_val = np.nanmean(a)
c = np.nan_to_num(a,nan=mean_val)
print(c)

"""
Summary
Function	                     Purpose
np.isnan(arr)	                 Identifies NaN values (returns a boolean array)
np.nan_to_num(arr, nan=value)    Replaces NaN values with a specified value
np.nanmean(arr)	                 Computes mean while ignoring NaN values"""