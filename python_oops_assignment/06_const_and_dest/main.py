# Constructor and Destructor
# Assignment
# Creat a class logger that points a message when an object is created(constructor)
# and another message when it is destroyed(destructor).

class Logger:
    def __init__(self):
        print("Logger Object Created") # Constructor

    def __del__(self):
        print("Logger Object Destroyed") # Destructor

if __name__ == "__main__":
    log = Logger() # Creating an object of the Logger class
    del log