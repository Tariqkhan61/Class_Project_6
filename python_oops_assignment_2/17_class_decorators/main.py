# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method
#  returning "Hello from Decorator!". Apply it to a class Person.

# Class Decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls
# Apply the decorator to the person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object and call the new method
person = Person("Muhammaad Tariq Mahboob")
print(person.greet()) 