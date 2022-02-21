class Bank():
    def __init__(self,own,bal=0):
        self.own = own
        self.bal = bal
    
    def deposit(self,amount):
        self.bal = self.bal + amount
        
        print(f"deposited amount{amount} total balace ={self.bal}")
    
    def withdraw(self,amount):
        if amount>self.bal:
            print("not enough fund")
        else:
            self.bal = self.bal - amount
            print(f"withdrawed amount{amount} total balace ={self.bal}")
    def __str__(self):
        return f"name = {self.own} balance = {self.bal}"
    
c = Bank("saurabh",500)
print(c)
print(c.own)
c.deposit(1000)
c.withdraw(750)
c.withdraw(1000)
    


