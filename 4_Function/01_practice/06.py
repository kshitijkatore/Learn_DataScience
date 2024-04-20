# Create a function in Python to check if a string is a palindrome.

str = input("Enter a string: ")

def is_palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    
print("IS Palindrom: ", is_palindrome(str))

    

