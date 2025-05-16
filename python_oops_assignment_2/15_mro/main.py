#15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("show from class A")

class B(A):
    def show(self):
        print("show from class B")

class C(A):
    def show(self):
        print("show from class C")

class D(B, C):
    pass

# Now create an object of class D and call show()
obj = D()
obj.show() # It will call the show() method from cclass B due to MRO

# Print MRO of class D
print("Method Resolution Order (MRO) of class D:", D.__mro__)