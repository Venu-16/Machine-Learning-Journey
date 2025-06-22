"""OOPS in PYTHON:
Object-Oriented Programming is a way to structure code by modeling
real-world things as “objects” that combine data and behavior.
Examples:
    1. A Car as an object with properties like
    color, speed, and behaviors like drive(), brake().
    2. A LinearRegressionModel object with data
     like weights, bias and methods like train(), predict().
    """

#class defn1: blueprint of creating objects
# def2: A Template/class defines the properties and behavior
# that objects created from it will have.


class Dog:
    species = "Canis familiaris" #class Attribute
    def __init__(self, name, bread):
        self.name = name       #instace Attribute
        self.bread = bread

    def speak(self):
        print(f"{self.name} says bow bow")

my_dog = Dog("Buddy", "Labrador")
my_dog.speak()

""" Class Attribute:
A class attribute in Python is a variable that belongs to 
the class itself rather than any specific instance of the class.
It is shared among all instances of the class, meaning that if 
one instance modifies the class attribute, the change is reflected
across all instances.
Key Characteristics:
1. Shared Across Instances: All objects of the class have
    access to the same class attribute.
2. Defined Inside the Class: It is declared within the 
    class but outside any instance methods.
3. Accessed Using Class Name or Instance: You can access 
    it using ClassName.attribute or instance.attribute."""

"""Instance Attribute:
An instance attribute in Python is a variable that belongs to a
specific object (instance) of a class. Unlike class attributes, 
which are shared among all instances, instance attributes are 
unique to each object and are defined within the __init__ method.
Key Characteristics:
1. Specific to Each Object: Every instance of a class has its own
  copy of instance attributes.
2. Defined in the __init__ Method: Instance attributes are
   initialized when an object is created.
3. Accessed Using self: They are referenced using self.attribute_name."""

"""Methods :
inside class we define functions that deals with behavior of objects."""




"""Encapsulation:
Encapsulation = Bundling data + behavior inside objects and restricting
direct access to internal data."""

class BackAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        self.__balance += amount

    def getbalance(self):
        return self.__balance


"""we use __ to make attributes "private" and enforce access via methods."""

"""Inheritance:
Inheritance = One class(child) inherits from another (parent)."""

class Animal:
    def speak(self):
        return "sound"

class Cat(Animal):
    def speak(self):
        return "meow"
#Cat inherits from Animal but overrides speak()


"""Polymorphism:
same method name behaves differently for different objects"""

animals = [Dog("Max","Beagle"),Cat()]

for a in animals:
    print(a.speak())


#  __init__: Constructor
# Called when an object is created.

def __init__(self, name):
    self.name = name
# __str__: Human-readable string
# Used by print().

def __str__(self):
    return f"This is {self.name}"

# __repr__: Developer-readable string
# Used in the console or debugging.

def __repr__(self):
    return f"Dog(name='{self.name}')"
