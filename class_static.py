class Student:
    grade = 40
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_data(self):
        print("Name:-",self.name,"Age :- ",self.age,"Grade :- ",self.grade)

    @classmethod
    def update(cls,grade):
        cls.grade = grade

    @staticmethod
    def check_age(age):
        if(age>18):
            print("Above 18")
        else:
            print("Below 18")


s1 = Student("Ramesh",23)
s1.get_data()

s2 = Student("Mahesh",32)
s2.get_data()

Student.update(23)
Student.check_age(10)
