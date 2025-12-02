class BankAccount:
    # Constructor - initializes objects
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
        
        # self - refrences the object
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Insufficient funds"
        
    def deposit(self,amount):
        self.balance+= amount
        
    def display_info(self):
        return f"====Welcome {self.owner_name} account number {self.account_number}, balance is {self.balance}, account created at {self.date_opened}==="
    
        
# Object creation and method calling
Account1 = BankAccount(1234,100000.00,"Peace","12-10-2004")
Account2 = BankAccount(2345,200000.00,"Letting","13-10-2003")
Account1.deposit(1000)
Account1.withdraw(500)
Account2.deposit(1000)
Account2.withdraw(500)
    
print(Account1.display_info())
print(Account2.display_info())


