# dictionary.py
# Demonstrates dictionary creation and accessing/updating values

student = {
    "name": "Mark",
    "age": 21,
    "course": "Computer Science",
    "grade": "A"
}

print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Grade:", student["grade"])

student["age"] = 22
student["grade"] = "A+"

print("Updated student record:", student)