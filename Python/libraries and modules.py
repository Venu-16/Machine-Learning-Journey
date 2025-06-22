# created a module name VM in another file name should Start with Capital letters
# import using import keyword
import VM

VM.v()
print(VM.location)


#built-in metods

# 1. Random Module
import random
num = random.randint(1, 10)
print(f"Random integer between 1 and 10: {num}")
fruits = ["Java", "C", "C++", "Python"]
chosen_fruit = random.choice(fruits)
print(f"Randomly chosen language: {chosen_fruit}")

# 2. Math Module
import math
sqrt_val = math.sqrt(64)
pi_const = math.pi
print(sqrt_val)
print(pi_const)

# 3. datetime
import datetime
date_today = datetime.date.today()
time_now = datetime.datetime.now().time()
print(date_today)
print(time_now)