# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# lambda arguments : expression
x = lambda a : a+10
print(x(5))

# Lambda functions can take any number of arguments:
y = lambda a, b : a * b
print(y(5, 6))

# The power of lambda is better shown when you use them as
# an anonymous function inside another function.

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))

# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))

# Lambda with List Comprehension
# Combining lambda with list comprehensions enables
# us to apply transformations to data in a concise way.

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res)


# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

# The lambda function doubles each number.
# map() iterates through a and applies the transformation.

