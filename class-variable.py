# class_variables.py
# Demonstrates class variables shared across all instances

class Student:
    school_name = "The Cooperative University of Kenya"

    def __init__(self, name, course):
        self.name = name
        self.course = course


student1 = Student("Mark", "Computer Science")
student2 = Student("Ann", "Information Technology")

print(f"{student1.name} studies at {student1.school_name}")
print(f"{student2.name} studies at {student2.school_name}")

print("Accessed via class:", Student.school_name)

Student.school_name = "Cooperative University (Main Campus)"
print(f"{student1.name} now studies at {student1.school_name}")
print(f"{student2.name} now studies at {student2.school_name}")