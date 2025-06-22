"""
loops:
Loops are used to repeat instructions.
"""
#while Loops
"""
while condition:
    #somework
"""
count =1
while count<=5:
    print("hello")
    count += 1

#3print numbers from 1 to 10
i=1
while i<=10:
    print(i)
    i += 1

#print numbers from 10 to 1
j=10
while j>0:
    print(j)
    j -=1
#print the multiplication table for n
n = 4
i=1
while i<=10:
    print(n*i)
    i +=1

#print the elements of following list using the while loop
lis =[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(lis):
    print(lis[i])
    i+=1

#search for a number in this tuple
lis =[1,4,9,16,25,36,49,64,81,100]
i=0
x = 64
while i<len(lis):
    if lis[i]==x:
        print("found at i= ",i)
    i+=1

"""
For loop:
loops are used for sequential traversal. for traversing list, string, tuples etc."""
#for loop

for el in lis:
    print(el)

#for loop with else
for el in lis:
    print(el)
else:
    print("end")


"""Range():
range functions returns a sequence of numbers, starting from 0 by default, 
and increments by 1(by default), and stops before a specified number. """

#Syntax: range(start?, stop, step?) start and step are optional

for i in range(5):
    print(i)

for i in range(2,8):
    print(i)

for i in range(0,10,2):
    print(i)

#print numbers from 100 to 1

for i in range(100,0,-1):
    print(i)

"""Pass statement:
pass is a null statement tha does nothing. It is used as a placeholder for future code.
"""

for i in range(10):
    pass

print("some work had done.")

#program for writing sum of n natural numbers using while loop
i =1
n=19
s=0
while i<=n:
    s = s + i
    i+=1
print(s)

#program for factorial of first n numbers;


n =10
f=1
for i in range(1,11):
    f = f*i
    print(f)

