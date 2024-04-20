# Create a function in Python to find the factorial of a given number.
num = int(input("Enter a number:"))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
print("Factorial of :", num, "is :", factorial(num))