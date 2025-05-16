# Assignment
# Create a class Bank with class variable bank_name. Add aclass method change_bank_name(cls,name)
# that allows changing the bank name. Show that it affects all instances of the class.

class Bank:
    bank_name = "Habib Bank" # Class variable
    # use decorator for class method
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
if __name__ == "__main__":
    user1 = Bank()
    user2 = Bank()

    print("Before changing bank name:")
    print(f"User1 Bank Name: {user1.bank_name}")
    print(f"user2 Bank Name: {user2.bank_name}")

    # Changing the bank name using the class method
    Bank.change_bank_name("Mezan Bank")

    print("\nAfter changinh bank name:")
    print(f"user1 Bank Name: {user1.bank_name}")