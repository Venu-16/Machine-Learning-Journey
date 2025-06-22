"""
File I/O in python

python can be used to perform operations on a file.(read and write data)

Types of files:
1. text files: .txt, .docx, .log etc...
2. Bin files: .mp4, .mov, .png, .jpeg etc...

Open, read & close File:
we have to open a file before reading or writing

f = open("file_name", mode)

file_name = demo.docx
mode = r, w
"""

f= open("venu.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()

"""MODES:
'r' : open for reading( default )
'w' : open for writing, truncating thr file first.
'x' : create a new file and open it for writing.
'a' : open for writing, appending to the end of the file if it exists.
'b' : binary mode
't' : text mode (default)
'+' : open a disk file for updating (reading and writing).
"""
f = open("venu.txt","r")

data = f.read(5)

print(data)
print(f.readline(5))

#writing to a file
f = open("venu.txt", "w")
f.write("\ni want to become a data scientist at amazon")
f.close()

#syntax
with open("venu.txt", "r") as f:
    data = f.read()
    print(data)
    #doesn't need to close the file

#deleting file
""" Using the OS module 
Module(like a code library) is a file written by
another programmer that generally has a functions we can use.
"""
#import os
#os.remove("demo.py")
