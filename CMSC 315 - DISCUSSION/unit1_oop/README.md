# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying.

## Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles 

## Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.
5. 
6.Student Implementation Summary
Parent Class
Created a ParentClass with:

Class variable: school
Instance variables: name and age
Constructor (init)
display_info() method
Child Class
Created a ChildClass that:

Inherits from ParentClass
Adds class variable: program
Adds instance variables: major and courses
Adds study() method
Overrides display_info()
Namespace Demonstration
Created two ChildClass objects
Accessed class variables from both the class and an object
Added a unique attribute to one object
Displayed object namespaces using dict
Displayed class namespace information
Copy Demonstration
Created nested mutable data
Demonstrated shallow copy using copy()
Demonstrated deep copy using deepcopy()
Modified original data and compared results
Student Extension
Added a study() method to demonstrate additional ChildClass behavior.