class bank:
    def __init__(self,an,name,tp,bal=0):
        self.an=an
        self.name=name
        self.tp=tp
        self.bal=bal
    def deposit(self,bal):
        self.bal=self.bal+bal
    def withdraw(self,bal):
        if(bal<self.bal):
            self.bal=self.bal-bal
        else:
            print("Insufficient Balance")
    def dis(self):
        print("Name:",self.name)
        print("Account number:",self.an)
        print("Account Type:",self.tp)
        print("Balance Ammount:",self.bal)
        
an=int(input("Enter the account number: "))
name=input("Enter the name: ")
tp=input("Enter Account type:(AC/C)")
bn=bank(an,name,tp)
print("Enter your option: ")
print("1.Deposit")
print("2.Withdraw")
print("3.Display")
print("4.Exit")
while(True):
    opt=input("Enter your option: ")
    if(opt=='1'):
        print("deposit")
        am=int(input("Enter the amount to deposit: "))
        bn.deposit(am)
    elif(opt=='2'):
        print("withdraw")
        am1=int(input("Enter the amount to withdraw: "))
        bn.withdraw(am1)
    elif(opt=='3'):
        bn.dis()
    elif(opt=='4'):
        break
    else:
        print("Invalid Input")
        



        
