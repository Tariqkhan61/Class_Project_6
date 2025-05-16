# Public Variable and Method
# Assignment
# Create a class Car with a public variable 'brand' and a public method start(). 
# Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):  # Fixed the parameter name to match the assignment
        self.brand = brand  # Public variable, accessible inside and outside the class

    def start(self):  # Public method
        print(f"{self.brand} car is starting...")  # Fixed f-string syntax

if __name__ == "__main__":  # This block should be outside the class
    # Creating an object of the Car class
    my_car = Car("Toyota")
    print(my_car.brand)
    my_car.start()




