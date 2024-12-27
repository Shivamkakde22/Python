                                                              # ENCAPSULATION
class A:
    _a=10
    __b=20
    def show(self):
        print(self._a)
        print(self.__b)
        print(self._a+self.__b)
class B:
    _c = 200
    __d = 30
    def display(self):
        print(self._c)
obj = A()
obj.show()
print(obj._a)

obj1 = B()
obj1.display()