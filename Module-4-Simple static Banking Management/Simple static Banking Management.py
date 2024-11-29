class Bankinkg:
    def __init__(self,user_name,initial_balance):
        self.name=user_name
        self.balance=initial_balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return amount

    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            return amount

        else:
            print(f"Insufficient amount.")


bank=Bankinkg("IBBL",40000)
print(f"Account name: {bank.name}")
print(f"Initial balance: {bank.balance}")
print(f"Depsoited amount is : {bank.deposit(20000)}")
print(f"After deposited , new balance is: {bank.get_balance()}")
print(f"Withdrwan amount is: {bank.withdraw(30000)}.")
print(f"After withdrawn new balance is: {bank.get_balance()}")
