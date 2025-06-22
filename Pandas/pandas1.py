"""
In computer programming, pandas is a software library written for
the python programming language for data manipulation and analysis.
In particular, It offers data structures and operations for manipulating
numerical tables and time series.
"""
import numpy as np
import pandas as pd

df = pd.read_csv("sample_data.csv")
# print(df)
head = df.head(6)
# print(head)

taill = df.tail(5)
# print(tail)
shape = type(df)
print(shape)

