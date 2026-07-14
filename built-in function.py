# builtin_functions.py
# Demonstrates at least 10 built-in Python functions

numbers = [4, 8, 15, 16, 23, 42]

print("len():", len(numbers))
print("max():", max(numbers))
print("min():", min(numbers))
print("sum():", sum(numbers))
print("type():", type(numbers))
print("sorted():", sorted(numbers, reverse=True))
print("abs():", abs(-25))
print("round():", round(3.14159, 2))
print("str():", str(123))
print("int():", int("50"))
print("float():", float("9.5"))
print("list():", list("abc"))

name = input("Enter your name for print()/input() demo: ")
print("Hello,", name)