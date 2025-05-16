# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Example usage:
temp_celsius = 39
temp_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius}°C is {temp_fahrenheit}°F")

class TemperatureConverter:
    @staticmethod
    def fahrenheit_to_celsius(f):
        return (f - 32) * 5 / 9

# Example usage (outside the class)
temp_fahrenheit = 103
temp_celsius = TemperatureConverter.fahrenheit_to_celsius(temp_fahrenheit)
print(f"{temp_fahrenheit}°F is {temp_celsius:.2f}°C")
