# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price,
#  @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price # Private Attribute
    @property
    def price(self):
        print("Greeting Price...")
        return self._price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print("Setting Price...")
        self._price = value
    @price.deleter
    def price(self):
        print("Deleting Price...")
        del self.price
    # Create an Object of Product
product = Product(100)
# Accessing the pricce using the property
print(product.price) # Output: 100

# Deleting the price
del product.price # Output: Deleting Price...