"""
functions:
Block of statements that perform a specific task.

Syntax:#func declaration
def func_name(param1,param2....)
    #some work
    return val

func_name(arg1,arg2) #func call
"""

def addition(a,b):
    return a+b #optional
    #print(a+b)

print(addition(3,5))

def addition(a,b):
    # return a+b #optional
    print(a+b)

op = addition(2,3) #prints none because of no return type
print(op)

#Built-in functions
# print(),len(),add()..etc

#default parameters

def calc_prod(a,b=3):
    return a*b

print(calc_prod(2))

#program to print length of the string
s = "venumadhav"
print(len(s))

#program to print the all character in a single line

def pr(a):
    for i in range(len(a)):
        print(a[i], end=" ")

pr(s)

#program to find factorial of a number
def fact(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return f

print(fact(6))

#program to convert usd to INR

def usdtoinr(a):
    return a*87

print(usdtoinr(9))

"""Recursion:
When a function calls itself repeatedly.
#it is call Stack
"""
def show(n):
    if n==1:
        return 1
    print(n)
    show(n-1)

print(show(9))
#program to fact using recursion
def fact(n):
    if n==0 or n==1:
        return 1

    return fact(n-1)*n

print(fact(9))

#program to calculate sum of first n natural numbers

def sn(n):
    if n==1:
        return 1
    return sn(n-1)+n

print(sn(10))

#program to print all elements in a list using recursion

def printlist(l,index):
    if index ==len(l):
        return
    else:
        print(l[index], end=" ")
    return printlist(l,index+1)
l = [1,2,3,45,6,7,8,9,0,6]
print(printlist(l,0))