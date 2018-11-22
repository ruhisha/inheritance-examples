class A:
    @staticmethod
    def m1():
        print("this is A class method")
class B:
    def show(self):
        print("this is B class method")
class C(A,B):
    def display(self):
        print("this is C class method")
c=C()
c.display()
c.m1()
c.show()