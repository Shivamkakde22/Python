from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,heigth):
        self.width=width
        self.height=heigth

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return 2*(self.width+self.height)

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*(self.radius**2)

rect = Rectangle(5,3)
print('Area of reactangle',rect.area())

cir = Circle(5)
print(cir.area())