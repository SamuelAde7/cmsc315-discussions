"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:

    school = "UMGC"  # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, School: {ParentClass.school}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):

    program = "Data Structures"  # new class variable

    def __init__(self, name, age, major, courses):
        super().__init__(name, age)
        self.major = major
        self.courses = courses

    def study(self):
        print(f"{self.name} is studying {self.major}.")

    # overriding parent method
    def display_info(self):
        return (f"Name: {self.name}, Age: {self.age}, "
                f"Major: {self.major}, Program: {ChildClass.program}")


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    student1 = ChildClass("Alice", 20, "Computer Science", ["CMSC315"])
    student2 = ChildClass("Bob", 22, "Data Science", ["DATA300"])

    print("Class variable through class:")
    print(ChildClass.program)

    print("\nClass variable through object:")
    print(student1.program)

    # add attribute to only one object
    student1.club = "Coding Club"

    print("\nStudent 1 namespace:")
    print(student1.__dict__)

    print("\nStudent 2 namespace:")
    print(student2.__dict__)

    print("\nClass namespace keys:")
    print(list(ChildClass.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = {
        "name": "Alice",
        "scores": [90, 95, 100]
    }

    # Shallow copy shares nested mutable objects
    shallow_copy = copy(original)

    # Deep copy creates completely independent objects
    deep_copy = deepcopy(original)

    original["scores"].append(85)

    print("Original:", original)
    print("Shallow Copy:", shallow_copy)
    print("Deep Copy:", deep_copy)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nParent Object:")
    parent = ParentClass("John", 40)
    print(parent.display_info())

    print("\nChild Object:")
    child = ChildClass("Emma", 21, "Computer Science", ["CMSC315"])
    print(child.display_info())

    child.study()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()