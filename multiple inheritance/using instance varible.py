class Student:
    def personalinfo(self,idno,name):
        self.idno=idno
        self.name=name
class Address:
    def add(self,details,contactnum):
        self.details=details
        self.contactnum=contactnum
class Marks(Student,Address):
    def display(self):
        print("DETAILS",self.details)
        print("CONTACTNUM",self.contactnum)
        print("IDNO",self.idno)
        print("NAME",self.name)
m=Marks()
m.personalinfo(100,"rani")
m.add("hyderabad",55445645)
m.display()