from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printArea(cls):
        return 0


class Square(Shape):
    def __init__(self):
        self.side = 4

    def printArea(cls):
        result = (cls.side *cls.side)
        print("square is ",result)

s =Square()
s.printArea()
