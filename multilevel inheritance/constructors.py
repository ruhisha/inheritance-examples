class Bank:
    def __init__(self):
        print("hello")
class Rbi(Bank):
    def show(self):
        print("hai")
class Sbi(Rbi):
    def display(self):
        print("welcome")
s=Sbi()
s.show()
s.display()
