class Employee():
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
    def display(self):
        print(self.name)
        print(self.id)

class Company(Employee):
    def __init__(self,cname):
        self.cname=cname
        super().display(name,id)

    def display(self):
        print(self.cname,self.name,self.id)

c1 = Company("Infosys","Shivam",101)
c1.display()

