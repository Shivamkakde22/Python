class doctor:
    __name = "Ramesh"
    _id = 1022
    def doct(self):
        print("Name : -",self.__name)
        print("ID :-",self._id)
dr = doctor()
dr.doct()
print("ID calling outside the class :- ",dr._id)