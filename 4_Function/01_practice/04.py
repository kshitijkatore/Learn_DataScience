# Write a Python function to calculate the sum of all elements in a list.

num = int(input("Enter the number of elements: "))
list = []
for i in range(num):
    list.append(int(input("Enter the element: ")))
print(list)


def sum_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    
    return sum

print("Sum of all elements in the list is: ", sum_list(list))