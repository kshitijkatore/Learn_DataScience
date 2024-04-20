# Implement a function in Python to check if a given year is a leap year or not.

num = int(input("Enter a year: "))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False
    
print(is_leap_year(num))