
# Basic data types
print("Basic data types in Python:")
print(type(5))          # Integer
print(type(3.14))       # Float
print(type("Hello"))    # String
print(type(True))       # Boolean

# Data structures
print("\nData structures in Python:")
print(type([]))         # List
print(type(()))         # Tuple
print(type({}))         # Dictionary
print(type(set()))      # Set

# Functions and control flow
print("\nFunctions and control flow in Python:")
def greet(name):
    print("Hello,", name)

greet("John")

# Loops
print("\nLoops in Python:")
for i in range(5):
    print(i)

# While loop
i = 0
while i < 5:
    print(i)
    i += 1

# Conditional statements
print("\nConditional statements in Python:")
x = 5
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Operators
print("\nOperators in Python:")
print(5 + 3)       # Addition
print(5 - 3)       # Subtraction
print(5 * 3)       # Multiplication
print(5 / 3)       # Division
print(5 // 3)      # Integer division
print(5 % 3)       # Modulus (remainder of division)
print(5 ** 3)      # Exponentiation

# Exception 
print("\nExceptions:")
try:
    result = 5 / 0
except ZeroDivisionError:
    print("Error! You cannot divide by zero man!!!.")

# Modules and packages
print("\nModules and packages in Python:")
import math
print(math.sqrt(25))   # Square root

# File I/O
print("\nFile I/O in Python:")
with open("example.txt", "w") as f:
    f.write("Hello, world!")

with open("example.txt", "r") as f:
    content = f.read()
    print(content)

# List comprehensions
print("\nList comprehensions in Python:")
squares = [x ** 2 for x in range(5)]
print(squares)

# Lambda functions
print("\nLambda functions in Python:")
double = lambda x: x * 2
print(double(5))

# Generators
print("\nGenerators in Python:")
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i)

# Decorators
print("\nDecorators in Python:")
def uppercase(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase
def greet():
    return "hello"

print(greet())

# Object-oriented 
print("\nObject-oriented programming:")
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I'm", self.name)

person = Person("Alice")
person.greet()
