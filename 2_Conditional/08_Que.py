password = input("Enter the length of charecter:")

if len(password) < 6:
    strength = "weak"
elif len(password) <=10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is :", strength)