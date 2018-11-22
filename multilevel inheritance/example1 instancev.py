class Bank:
    def deposit(self,accountnumber,amount):
        self.accountnumber=accountnumber
        self.amount=amount
class Rbi(Bank):
    def withdraw(self,pinno):
      self.pinno = pinno
class Sbi(Rbi):
    def balancecheck(self,type):
        self.type=type
    def display(self):
        print("balancecheck:",self.type)
        print("pinnumber:",self.pinno)
        print("accountnumber:",self.accountnumber)
        print("amount",self.amount)
s=Sbi()
s.balancecheck("savings")
s.deposit(1234561104,15000)
s.withdraw(5231)
s.display()

