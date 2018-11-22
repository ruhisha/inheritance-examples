class Student:
    def display(self):
        print("this is student details")
class Address:
    def show(self):
        print(input("the student address is"))
class Cno(Student,Address):
    def show(self):
        print(input("the contact details is"))
c1=Cno()
c1.show()
c1.display()