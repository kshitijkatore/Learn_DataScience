# Create a function in Python to generate the Fibonacci sequence up to a specified number of terms.

num = int(input("Enter the number of terms: "))

def fibonacci(n):
    a, b = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci(num))