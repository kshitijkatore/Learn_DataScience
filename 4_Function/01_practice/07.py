# Write a Python function to sort a list of integers in ascending order.

num = int(input("Enter the number of elements in the list: "))
list = []

for i in num:
    list.append(int(input("Enter the element: ")))


def sort_list(nums):
    return sorted(nums)

print(sort_list(list))
