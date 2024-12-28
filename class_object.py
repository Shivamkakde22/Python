class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        return self.name


animal = Animal('bunny')
print(animal)
