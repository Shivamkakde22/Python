class Computer():
    def __init__(self):
        self.ram = "8gb"
        self.storage = "1tb"
        print("Computer")

    def __del__(self):
        print("This is Destructor ")
class Mobile(Computer):
    def __init__(self):
        super().__init__()
        self.model = "Android"
        print("Mobile")


mob = Mobile()
print(mob.__dict__)
