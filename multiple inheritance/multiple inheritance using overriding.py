class Student:
    def display(self):
        print("this is student details")
class Address:
    def show(self):
        print("the student address is")
class Cno(Student,Address):
    def contact(self):
        print("the contact details")
        print("ok")
    def display(self):
        super().show()
        print("this is display of Cno")
        print("thanks")
c1=Cno()
c1.contact()
c1.show()
c1.display()