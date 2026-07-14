# classes.py
# Demonstrates creating a class and objects

class Student:
    def __init__(self, name, admission_number, course):
        self.name = name
        self.admission_number = admission_number
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Admission No: {self.admission_number}, Course: {self.course}")


student1 = Student("Mark", "CS/001/2023", "Computer Science")
student2 = Student("Ann", "CS/002/2023", "Information Technology")
student3 = Student("Tom", "CS/003/2023", "Software Engineering")

student1.display_info()
student2.display_info()
student3.display_info()