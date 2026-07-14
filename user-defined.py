# user_defined_functions.py
# Demonstrates user-defined functions

def add_numbers(a, b):
    return a + b

def rectangle_area(length, width):
    return length * width

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def display_student(name, admission_no, course):
    print(f"Name: {name}, Admission No: {admission_no}, Course: {course}")


print("Add numbers:", add_numbers(5, 7))
print("Rectangle area:", rectangle_area(4, 6))
print("Is 17 prime?", is_prime(17))
print("Is 20 prime?", is_prime(20))
print("Factorial of 5:", factorial(5))
display_student("Mark", "CS/001/2023", "Computer Science")