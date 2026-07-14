# class_methods.py
# Demonstrates constructor, instance variables, class variable, and @classmethod

class Student:
    school_name = "The Cooperative University of Kenya"

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Course: {self.course}, School: {self.school_name}")

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


student1 = Student("Mark", "Computer Science")
student2 = Student("Ann", "Information Technology")

student1.display_info()
student2.display_info()

Student.change_school_name("Cooperative University - Karen Campus")

print("After using class method:")
student1.display_info()
student2.display_info()