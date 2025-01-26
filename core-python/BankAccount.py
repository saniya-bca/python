#creation of simple application

class BankAccount:
    def __init__(self,initialAmt,accHolder):
        self.balance=initialAmt
        self.name=accHolder
        print("Account is created")
        print(f"Account created for '{self.name}' with opening balance {self.balance}")
    def getData(self):
        print(f"Account  '{self.name}' has balance{self.balance}")
    def deposite(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited successfully")
        self.getData()
        print("Thank You")
    def withdraw(self,withdraw):
        self.balance=self.balance-withdraw
        print(f"Account  '{self.name}' has balance{self.balance}")
        print("Amount withraw successfully")
        print("Thank You")
  
