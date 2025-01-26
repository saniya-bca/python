#create banking application using class and object in python
class BankAccount:
    # Constructor to initialize account details
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = initial_balance

    # Method to display account details
    def display_account_details(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Available Balance: ₹", self.balance)

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. New balance: ₹{self.balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    # Method to check balance
    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

# Main Program
if __name__ == "__main__":
    print("Welcome to the Banking Application!\n")

    # Create an account
    name = input("Enter Account Holder's Name: ")
    account_no = input("Enter Account Number: ")
    initial_deposit = float(input("Enter Initial Deposit Amount: ₹ "))
    account = BankAccount(name, account_no, initial_deposit)

    while True:
        print("\nSelect an Option:")
        print("1. Display Account Details")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            account.display_account_details()
        elif choice == '2':
            deposit_amount = float(input("Enter amount to deposit: ₹ "))
            account.deposit(deposit_amount)
        elif choice == '3':
            withdraw_amount = float(input("Enter amount to withdraw: ₹ "))
            account.withdraw(withdraw_amount)
        elif choice == '4':
            account.check_balance()
        elif choice == '5':
            print("Thank you for using the Banking Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
