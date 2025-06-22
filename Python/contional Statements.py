#Conditional Statements
#if - condition
'''
Note: Python is Indentation Language
'''

a = 40
if a%2==0:
    print("even")

#if-else Condition

a = 43
if a%2==0:
    print("even")
else:
    print("odd")

#elif Condition
a =5
if a>0:
    print("+ve")
elif a<0:
    print("-ve")
else:
    print("zero")

#single line if /Ternary operator
a = -1
b = "positive" if a>0 else "negative"
print(b)

#Clever if / Ternary operator
age =14
vote = ("yes","no") [age<18]
#<var> = (false_value, true_value) [<condition>]
print(vote)


