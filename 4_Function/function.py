# Function in python are block of code reusable code that perform the specific task.

def greet():
    print("Hey, whats Up...!")
greet()

# fucntion argument
def greet(name):
    print("Hello, " + name + "!")
greet("Xitij")


# callback function
def sum(a, b, callback):
    val1 = callback(a)
    val2 = callback(b)

    return val1 + val2

result = sum(2, 3, lambda x: x**2)
print(result)

# Default argumets
def greet(name="xitij"):
    print("Hello, " + name + "!")

greet() # Hello, xitij!
greet("Rahul") # Hello, Rahul!

# Variable-Length arguments
def my_function(*args,**kwargs):
    print("Positional arguments: ", args)
    print("Keyword arguments: ", kwargs)

my_function(1, 2, 3, name="xitij", age=20)

# lambda Function --> Lambda function, alos know as anonymous function, are small, inline function defined suinf the 'lambda keyword

def multiply(x,y, callback):
    val1 = callback(x)
    val2 = callback(y)
    return val1 * val2

mul = multiply(2,3, lambda x: x)
print(mul)


#Docstring
def greet(name):
    """This function greets the person with the given name."""
    print("Hello, " + name + "!")

print(greet.__doc__)


# Scope of variable

x = 10
def func():
    print(x*2)
func()


# Recursion --> Function can call themselves recursively, enabling elegant solution for porblem that exhibit resursive patterns.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("factorial of :", factorial(5))

