class Bank:
    def __init__(self,accountnumber):
        self.accountnumber=accountnumber
class Rbi:
    def deposit(self,name):
        self.name=name
class Sbi(Bank,Rbi):
    def display(self):
        print("accountnumber",self.accountnumber)
        print("holdername",self.name)

s=Sbi(52231669)
s.deposit("robert")
s.display()



