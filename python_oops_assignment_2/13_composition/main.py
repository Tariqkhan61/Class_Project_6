# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object
#  to the Car class during initialization.
#  Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car has an Engine

    def start_car(self):
        return self.engine.start()  # Accessing Engine's method

# Create an Engine object
my_engine = Engine()

# Pass the Engine object to the Car
my_car = Car(my_engine)

# Use the Car method that accesses the Engine method
print(my_car.start_car())  # Output: Engine started



