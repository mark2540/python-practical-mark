# set.py
# Demonstrates set creation, adding/removing elements, and duplicate removal

numbers = {1, 2, 3, 3, 2, 1}
print("Set with duplicates removed:", numbers)

numbers.add(4)
print("After add:", numbers)

numbers.remove(2)
print("After remove:", numbers)

letters = {"a", "b", "a", "c", "b"}
print("Letters set (duplicates removed automatically):", letters)