# 05 Static Variable and Static Method
# Assignment
#vCreate a class mathUtils with a static method add(a,b) that returns the sum of a and b.
# No class or intance variable should be used.
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
if __name__ == "__main__":
        # Using the static method without creating an instance of the class
        result = MathUtils.add(5, 10)
        print(f"The sum is: {result}")