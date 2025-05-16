 # 2. Using cls
    #Assignment:
    #Create a class counter that keep track of how many objects have beemn ceated. Use a class
    #  variable and a class method with cls to manage and display the count of objects.
class Counter:
    count = 0  # Class variable to keep track of the number of objects

    # Now we make function to initialize the class variable
    def __init__(self):
        Counter.count += 1  # Increment the count whenever a new object is created

        # Now we use decorator of class method
    @classmethod
    def display_count(cls):
        print(f"Number of objects created:{cls.count}")
if __name__ == "__main__":
        # Creating objects of the Counter class.
        obj1 = Counter()
        obj2 = Counter()
        obj3 = Counter()
        obj3 = Counter()
        Counter.display_count()

# Public Variable and Method
# Assignment
# Create a class car with a public variable and brand and a public method start(). Instantiate
# the class and access both from outside the class.
        