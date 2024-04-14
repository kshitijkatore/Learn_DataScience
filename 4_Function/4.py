# Create a function that retruns both the area and ciccumference of a cirlce given its radius.

def circle(radius):
    area = 3.14*(radius**2)
    circumference = 2*3.14 * radius
    return area , circumference

a, c = circle(3)
print("Area:", a, "Circumference:", c)


