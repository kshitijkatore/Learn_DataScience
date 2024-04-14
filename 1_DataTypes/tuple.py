# sets are unorderd, mutable.
# creating sets in python in two types
# using curly brackets
my_set = {1, 2, 3, 4, 5}
print(my_set)

# set methods
my_set.add(6) # add the element to the set
print(my_set)

my_set.remove(6) # remove the element from the set
print(my_set)

my_set.pop()
print(my_set)

my_set.clear()
print(my_set)

my_set.add(1)
print(my_set)

new_set = my_set.copy()
print(my_set)


# A frozenset is an immutable version of a set. Once created, its elements cannot be changed or modified. Frozensets can be useful when you need to use a set as a key in a dictionary or as an element in another set.

my_frozenset = frozenset([1,2,3,4,5])
print(my_frozenset)

# set Comprehension
set_com = {x for x in range(1, 11) if x % 2 ==0 }
print("Set comprehension :",set_com)


# using set() cunstructor
another_set = set([1, 2,3 ,4 ,5])
print("Another set :",another_set)


