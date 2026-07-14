# string.py
# Demonstrates string concatenation, indexing, slicing, and methods

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)

word = "Python"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Slice [0:3]:", word[0:3])
print("Slice [2:]:", word[2:])

text = "Hello World"
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Replace:", text.replace("World", "Kenya"))
print("Split:", text.split(" "))