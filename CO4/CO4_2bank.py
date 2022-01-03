class bank:
    def __init__(self,an,name,tp,bal):
        self.an=an
        self.name=name
        self.tp=tp
        self.bal=bal
    def deposit(self,bal):
        self.bal=self.bal+bal
    def withdraw(self,bal):
        self.bal=self.bal-bal
    def dis(self):
        print("Name:",self.name)
        print("Account number:",self.an)
        print("Account Type:",self.tp)
        print("Balance Ammount:",self.bal)
        
an=int(input("Enter the account number"))
name=input("Enter the name")
tp=input("Enter Account type")
b1=input("Initial balance")
bn=bank(an,name,tp,b1)
print("deposit")
am=int(input("Enter the amount to deposit"))
bn.deposit(am)
print("withdraw")
am1=int(input("Enter the amount to withdraw"))
bn.withdraw(am1)
bn.dis()



        
