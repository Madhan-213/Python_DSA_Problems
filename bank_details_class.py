# class bank:
#     def __init__(self, account_number, account_holder, balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited: {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew: {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds or invalid withdrawal amount.")

#     def get_balance(self):
#         return self.balance

# # Example usage:
# my_account = bank("123456789", "John Doe", 1000)
# my_account.deposit(500)
# my_account.withdraw(200)

class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def info(self):
        print("name is = "+self.name)
        print("balance is = "+str(self.balance))

    def deposit(self,amount):
        self.balance+=amount
        print(f"after deposit {amount}rs balance is = ",str(self.balance))

    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print("after withdraw balance is = "+str(self.balance))
b1=bank("madhu",5000)

b1.info()
b1.deposit(2000)
b1.withdraw(1000)