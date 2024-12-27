from abc import ABC,abstractmethod
class Car(ABC):
    def mileage(self):
        pass
class Tata(Car):
    def mileage(self):
        print("Milegae 20")
class Tesla(Car):
    def mileage(self):
        print("Mileage 30")
class Ford(Car):
    def mileage(self):
        print("Mileage 40")
t1 = Tata()
t1.mileage()

t2 = Tesla()
t2.mileage()

t3 = Ford()
t3.mileage()