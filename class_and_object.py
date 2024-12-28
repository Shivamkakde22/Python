# INHERITANCE
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return 'some sound'
class Dog(Animal):
    def speak(self):
        return 'bark'

class Cat(Animal):
    def speak(self):
        return 'Meow'

my_dog = Dog('Bunny')
my_cat = Cat('Whisper')

print(my_dog.name)
print(my_dog.speak())

print(my_cat.name)
print(my_cat.speak())

