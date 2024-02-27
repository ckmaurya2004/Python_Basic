class Parant:
    var1 = 5
    var2 = 4
    def add(self):
        print(self.var1+self.var2)

class Child(Parant):
    def minus(self):
        print(self.var1-self.var2)


ch = Child()
ch.add()
ch.minus()
