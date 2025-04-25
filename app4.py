#CLASS_PROJECTS-06_Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.md
#Assignment-4-Class Variables and Class Methods
#Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) 
# that allows changing the bank name. Show that it affects all instances.
class Bank:
    bank_name = "National Bank"  # class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # change the class variable

    def show_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")
        
        # Create two objects
acc1 = Bank("Ahmed")
acc2 = Bank("Babar")

# Show original bank name
acc1.show_details()
acc2.show_details()

# Change the bank name using class method
Bank.change_bank_name("Meezan Bank")

# Show updated bank name for both instances
acc1.show_details()
acc2.show_details()

# Output
# Account Holder: Ahmed
# Bank Name: National Bank
# Account Holder: Babar   
# Bank Name: National Bank
# Account Holder: Ahmed   
# Bank Name: Meezan Bank  
# Account Holder: Babar   
# Bank Name: Meezan Bank  