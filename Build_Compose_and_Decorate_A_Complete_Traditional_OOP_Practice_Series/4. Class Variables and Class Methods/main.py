class Bank:
    # Class variable
    bank_name = "Default Bank"
    
    def __init__(self, branch):
        self.branch = branch
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def display_info(self):
        print(f"Bank: {Bank.bank_name}")
        print(f"Branch: {self.branch}")

# Example usage
if __name__ == "__main__":
    # Create two bank instances
    branch1 = Bank("Downtown")
    branch2 = Bank("Uptown")
    
    # Display initial information
    print("Initial bank information:")
    branch1.display_info()
    branch2.display_info()
    
    # Change the bank name using class method
    Bank.change_bank_name("Global Bank")
    
    # Display information after change
    print("\nAfter changing bank name:")
    branch1.display_info()
    branch2.display_info()
