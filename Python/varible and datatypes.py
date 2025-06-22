print("venu madhav")
#variables
name = "Venu Madhav" #string
age = 23  #int
price = 25.99 #float

print("My name is : ",name)
print("My age is:" ,age)
# , ==> tab space

'''rules for identifiers:
1. identifiers can be combination of uppercase and lowercase letters,
 digits or an underscore
2. An identifier can not start with digit. So while variable1 is valid, 
1variable is not valid.
3. We can't use Special symbols like !,#@%$ etc in our identifier.
4. Identifier can be any length.
'''

#type of variable
print(type(name))
print(type(age))
print(type(price))

#Datatypes
#Integer
a = 32
b = 45

#String
name1 = "venu"
name2 = 'venu'
name3 = '''venu'''
name4 = """venu"""

print(name1)
print(name2)
print(name3)
print(name4)

#float
price = 45.98
print(price)

#boolean
a = True
b = False

#None
c = None
print(a,b,c)

# do not use keywords as identifier
#sum
a = 2
b = 3
sum = a+b
print(sum)
print(a-b)

#punctuators
#(),{},[],# etc...
#python is an implicit language ==> it can recognise type of variable automatically

#Operators
'''An operator is a symbol that performs a certain operation between operands.
 1. Arithmetic Operators ( + , - ,*, / , % ,**,// )
 2.Relational / Comparison Operators ( == , != , > , < , >= , <= )
 3.Assignment Operators ( = , +=, -= ,*= , /= , %= ,**= )
 4.Logical Operators ( not , and , or )
'''
#Expression Execution

#String & numeric values can operate together with *

A,B = 2, 3
txt = "@"
print(2*txt*3)



#String & String can operate with +

A,B = "2", 3
txt = "@"
print((A+txt)*3)

#numeric values can operate with all arithmetic operators

A,B = 2,3
C=4
print(A+B*C)

#Arithmetic expression with Integer and float will result in float

A,B = 2, 3.0
C = A+B
print(C)

#Result of division operator with two integer will be a float

A,B = 2, 3
C = A/B
print(C)

#Integer division with and int will give int displayed as float

A,B = 1.3, 4
C = A//B
print(C, A/B)

#Remainder is negative when denominator is negative
a=5
b=-4
print(a/b)

#comments use # for single line or '''multi-line''' or """multi-line"""


#Input in python from user
#for String
name = input("name: ")
#for int
a = int(input())
#for float
b = float(input())
print(name, a, b)

#Operator Precedence in Logical operator  not>and>or

#Assaignment Operators

a =5
c =8
a+=c
print(a)
a-=c
print(a)
a*=c
print(a)
a/=c
print(a)
a %=c
print(a)
a**=c
print(a)

#Type conversion

a = 2
b = 8
c = a/b
print(c) #implicit conversion {int to float conversion}

#explicit conversion also called as "Type Casting"
a = "2"
b = 4
c = int(a)+b
print(c)
