# dictionaries in python are powerful data structure used to store collection of key-vlaue pairs. They are unorders, mutable , versatile making them highly useful in varios programming scenarios.
# creating dictionaries in python

my_dict = {
    'name': "xitij",
    "age": 20,
    "city": "Nagpur"
}

print(my_dict)
for key, value in my_dict.items():
    print("Keys are :",key, "Values are :",value)

my_dict["gender"] = "male" # Adding new key-value pair
print(my_dict)

my_dict["age"] = 21 # updating the value for an existing key
print(my_dict)

age = my_dict.pop("age")
print(age)
print(my_dict)

# implementing the daabase

student = {
    101: {"name": "xitij", "age": 20, "city": "Nagpur"},
    102: {"name": "abhishek", "age": 21, "city": "Hinganghat"},
    103: {"name": "sagar", "age": 22, "city": "Nagpur"}
}
print(student)

student[104] = {"name": "sahil", "age": 23, "city": "Nagpur"}

student[104]["age"] = 20
student[104]["city"] = "yavatmal"
print(student)

# remove a student
del student[104]
print(student)

for roll_no, info in student.items():
    print(f"Roll NO: {roll_no}, Name: {info['name']}, Age: {info['age']}, City: {info['city']}")


text = "Python is a popular programming language. Python is versatile and easy to learn."

word_freq = {}
words = text.split()

for word in words:
    word = word.lower()
    word_freq[word] = word_freq.get(word, 0) +1
print(word_freq) 


#Que: 1 What is the output of the following code?

student = {
    "name": "xitij",
    "age": 20,
    "grades": {"math": 90, "science": 80, "history": 70}
}
print(student.keys())

# Que: 2 How can you access the value associated with the key "science" in the student dictionary?
print("Age :",student['age'])

# Que: 3 Explain the difference between dict.keys() and dict.values() methods in Python dictionaries.
print(student.keys())
print(student.values())

# Que: 4 How do you add a new key-value pair to an existing dictionary in Python?
student["Gender"]  = "male"
print(student)

# Que: 5 Write a code snippet to remove the key "grades" from the student dictionary.
del student["grades"]
print(student)

# Que: 6 Explain the purpose of the dict.get() method in Python dictionaries. Provide an example.
print(student.get("name"))
print(student.get("age"))
print(student.get("Gender"))
print(student.get("grades"))

# Que: 7 What does the dict.update() method do? Provide a scenario where you would use it.
student.update({"name": "sahil"})

# Que 8: Write a Python code snippet to count the frequency of each character in a given string using a dictionary.

text = "Python is a popular programming language."
char_freq = {}

for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1

print(char_freq)

del char_freq[' ']
print(char_freq)

for char in char_freq:
    print(char,"-->",char_freq[char])

# Que 9: Can a dictionary key be of any data type in Python? Explain with an example.
my_dict = {
    1: "xitij",
    2: "sagar",
    3: "sahil",
    4: "abhishek",
    5: "shivam"
}
print(my_dict.values(), my_dict.keys())

# Que: 10 How would you check if a key exists in a dictionary before accessing its value to avoid a KeyError?
if "name" in student:
    print(student["name"])

# Que: 11 Explain the purpose of dictionary comprehension in Python. Provide an example.
my_dict = {x: x**2 for x in range(1, 11)}
print(my_dict)

# Que: 12 Write a Python code snippet to create a dictionary containing the multiples of two numbers from 1 to 10.
my_dict = {x: x*2 for x in range(1 ,11)}
print(my_dict)

