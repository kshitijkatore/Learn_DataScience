# Write a function that variable number of arguments and retruns their sum.

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))
print(sum_all(1, 2, 3, 4, 5))