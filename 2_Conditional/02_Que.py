# Movie tickets are priced based on age: $12 for adult (18 and over), $8 for childern, Everyone gets a $2 disccount on Wednesday

age = int(input("Enter your age: "))
day = "Wednesday"

price = 12 if age >=  18 else 8
if day == "Wednesday":
    price = price - 2

print("Ticket price for you is $",price)