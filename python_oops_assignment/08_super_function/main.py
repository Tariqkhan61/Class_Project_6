# # Step 1: Parent Class
# class Person:
#     def __init__(self, name):
#         self.name = name

# # Step 2: Child Class
# class Teacher(Person):  # Inheriting from Person
#     def __init__(self, name, subject):
#         super().__init__(name)  # Call to the base class constructor
#         self.subject = subject  # Set the subject

#     # Step 3: Displaying the result
#     def display(self):
#         print(f"Name: {self.name}, Subject: {self.subject}")

# # Main Execution Block
# if __name__ == "__main__":
#     # Creating an instance of Teacher
#     teacher = Teacher("Muhammad Tariq Mahboob", "Python Programming")
#     teacher.display()

# Class definition
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show_info(self):
        print(f"My name is {self.name} and my roll number is {self.roll_no}.")

# Object creation
student1 = Student("Ali", 101)
student2 = Student("Sara", 102)
student3 = Student("Tariq", 103)

# Method call
student1.show_info()
student2.show_info()
student3.show_info()

