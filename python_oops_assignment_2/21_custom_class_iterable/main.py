# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. 
# Implement __iter__() and __next__() to make the object iterable in a for-loop,
#  counting down to 0.

# Once you are done submit this form ASAP:

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self  # The iterator object is self

    def __next__(self):
        if self.current < 0:
            raise StopIteration  # Signals the end of iteration
        value = self.current
        self.current -= 1
        return value


# ✅ Using the Countdown class in a for-loop
print("Countdown:")
for number in Countdown(5):
    print(number)

    #  Explanation:
# __iter__() returns the iterator object (in this case, the instance itself).

# __next__() returns the next value and decreases the counter.

# When the counter goes below 0, StopIteration is raised to end the loop.


