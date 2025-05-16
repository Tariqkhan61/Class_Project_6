# 1 Using Self Keyword
# Assignment:
# Create a class student with attributes name, age,and marks.Use the self keyword
# to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks =marks
    # Now we use display method, for that we make a function
    def display(self):
        print(f"name: {self.name}, age: {self.age}, marks: {self.marks}")
if __name__ == "__main__":
    # Creating an object of the class Student
    student1 = Student("Umaima Khan", 25, 90)
    student2 = Student("Ali Khan", 27, 95)
    student1.display()
    student2.display()

   