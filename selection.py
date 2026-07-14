# selection.py
# Demonstrates if, if-else, and if-elif-else selection structures

score = 65
if score >= 50:
    print("Student passed")
else:
    print("Student failed")

number = int(input("Enter a number to check even/odd: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

num1 = 12
num2 = 45
num3 = 30

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is:", largest)