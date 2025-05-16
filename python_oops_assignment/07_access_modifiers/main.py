# # 7 Access Modifiers: Public, Protected, Private
# # Assignment:
# # Create a class employ with 
# # 1. Public variable name
# # 2. Protected variable _salary.and
# # 3. Private variable __ssn.
# # Try all three variables from an object of the class and document what happens.

# class Employee:
#     def __init__(self, name, salary, ssn):
#         self.name = name  # Public variable
#         self._salary = salary  # Protected variable
#         self.__ssn = ssn  # Private variable

# if __name__ == "__main__":
#         emp = Employee("Subhan Ali", 50000, "123-45-6789")
#         # Now accessing public variable
#         print("public variable name:",emp.name)
#         # Now accessing protected variable
#         print("protected variable :",emp._salary)
#         # Now accessing private variable
#        # print("private variable :", emp.__ssn) # This will raise an AttributeError
#         # ye code error dega is liye is ko neat bananay k liye (try except) ka use karen gy
#         try:
#             print("private variable:", emp.__ssn)
#         except AttributeError :
#             print("Can not access private variable __ssn.")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

c = Circle()
print(c.area())  # ✅ Output: 78.5
