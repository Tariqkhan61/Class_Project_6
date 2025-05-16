# # Abstract Classes and Methods
# # Assignment:
# # use the abc module to create an abstract class shap with an abstract method area().  
# #  Inherit a class rectangle that implements area().

# from abc import ABC, abstractmethod # abc = abstract base class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass # Abstract Method

#     class Rectangle(Shape):
#         def __init__(self, length, width):
#             self.length = length
#             self.width = width
#         def area(self):
#             return self.length *self.width
        
#         if __name__ == "__main__":
#             #creating an instance of Rectangle
#             rectangle = Rectangle(5, 4)
#             print("Area of rectangle:", rectangle>area())

#use the abc module to create an abstract class shap with an abstract method area().  
 #  Inherit a class square that implements area().

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side
if __name__ == "__main__":

    square = Square(4)
    print("Area of square:", square.area()) 
                
