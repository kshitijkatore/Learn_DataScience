# Check if all elements in alist are unique. if a duplicate is found, exit the looop and print duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate:", item)
        break
    else:
        unique_item.add(item)