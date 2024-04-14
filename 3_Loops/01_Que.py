# Given the list of numbers, count how many are positive.

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_Count = 0
for num in numbers:
    if num > 0:
        positive_number_Count += 1

print("Final count of positive number:", positive_number_Count)
