"""ile Handling with NumPy
Reading and writing files (np.loadtxt(), np.savetxt(),
np.genfromtxt(), np.save(), np.load())"""

"""NumPy provides functions for reading and writing 
data to text (.txt, .csv) and binary (.npy, .npz) files."""

import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt("data.txt", data, delimiter=",")

loaded_data = np.loadtxt("data.txt", delimiter=",")
print(loaded_data)

#np.genfromtxt() – Read Files with Missing Data
#Works like np.loadtxt() but handles missing values.


data_with_missing = np.genfromtxt("data.txt", delimiter=",", filling_values=0)
print(data_with_missing)

# Save with 2 decimal places
np.savetxt("output.csv", data, delimiter=",", fmt="%.2f")

np.save("data.npy", data)  # Save as binary file

loaded_binary = np.load("data.npy")
print(loaded_binary)
