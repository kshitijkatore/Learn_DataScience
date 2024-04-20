# Implement a function in Python to reverse a given string.

# str = input("Enter a String:")
# def reverse_string(str):
#     return str[::-1]

# print("Reversed string is :",reverse_string(str))

# second apporoach to solving
str = input("Enter a String:")
def reverse_string(str):
    s = ""
    for i in str:
        s = i + s
    return s 

print("Reversed string is :",reverse_string(str))

# Third apporoach to solving
