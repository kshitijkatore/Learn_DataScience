# Write a Python function to calculate the area of a rectangle given its length and width as parameters.

length = int(input("Enter the Length of rectangle:"))
width = int(input("Enter the Width of rectangle:"))

def rectangle_area(length, width):
    return length * width

print("Area of rectangle:", rectangle_area(length, width))



