# Create a function that accepts any number of keyword arguments and prints them in the formats

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name= "xitij", power="lazer")
