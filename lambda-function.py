# lambda_functions.py
# Demonstrates lambda functions

add = lambda a, b: a + b
print("Add:", add(4, 5))

multiply = lambda a, b: a * b
print("Multiply:", multiply(4, 5))

students = [("Mark", 85), ("Ann", 92), ("Tom", 78)]
sorted_students = sorted(students, key=lambda student: student[1])
print("Sorted by score:", sorted_students)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)