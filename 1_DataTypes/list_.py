# List data type in python
# mutable, ordered

my_list = [1, 2, 3, 4, 5]
print(my_list)

empty_list = []
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
empty_list.append(4)
empty_list.append(5)
print(empty_list)

# Accessing elements in a list

print(my_list[0])
print(my_list[0:2])
print(my_list[::-1]) # reverse the list elements
print(my_list[-1]) # last element
print(my_list[-2]) # second last element

# Modifying Lists

my_list[0] = 10
print(my_list)

my_list[0:2] = [11, 12]
print(my_list)

my_list[0:2] = []
print(my_list)  # elements gets back to the list

my_list.append(60) # append ata the of the list
print(my_list)

my_list.insert(0, 10)
print(my_list)

my_list.insert(1, 20) # insert element at the indedx
print(my_list)

my_list.remove(10) # removes first occurence of 10
print(my_list)

my_list.pop()  # removes last element
print(my_list)

my_list.pop(0) # removes element at index 0
print(my_list)

# list operations 
a = [1, 2, 3]
b = [4, 5, 6]
print("list concatination ", a  + b)

print("list repetition ", a*3)
print(2 in a) # check if 2 is present in a 


list = [1, 2, 3, 4, 5]


