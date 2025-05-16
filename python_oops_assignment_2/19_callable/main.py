# 9. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor.
#  Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
# Create an instance of with a factor of 5
multiply_by_5 = Multiplier(5)
# Test with callable()
print("Is multiply_by_5 callable?", callable(multiply_by_5))  # Should return True
# Call the object like a function
result = multiply_by_5(10) # Should return 50
print("Result of calling multiply_by_5 with 10:", result)  # Should return 50
