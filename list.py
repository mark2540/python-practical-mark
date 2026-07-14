# list.py
# Demonstrates list creation, adding/removing/updating items, and looping

fruits = ["apple", "banana", "mango"]
print("Original list:", fruits)

fruits.append("orange")
print("After append:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits[0] = "pineapple"
print("After update:", fruits)

print("Looping through list:")
for fruit in fruits:
    print("-", fruit)