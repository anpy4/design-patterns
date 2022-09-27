from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    '''
    Basic Shape representation
    '''
    @abstractmethod
    def __init__(self, size:int):
        '''Prepares Shape object'''

    @abstractmethod
    def get_perimeter(self):
        '''Calculates the perimeter'''

    @abstractmethod
    def get_area(self):
        '''Calculates the area'''


class Circle(Shape):
    '''Implements circle shape logic'''

    def __init__(self, size:int):
        self.size = size

    def get_perimeter(self):
        return 2*pi*self.size

    def get_area(self):
        return pi*self.size*self.size


class Square(Shape):
    '''Implements square shape logic'''

    def __init__(self, size: int):
        self.size = size

    def get_perimeter(self):
        return 4 * self.size

    def get_area(self):
        return self.size * self.size



class AbstractFactory(ABC):
    '''Abstract factory implementation'''

    @abstractmethod
    def get_shape(self, shapeType:str, size:int):
        ''' Return shape object'''


class ShapeFactory(AbstractFactory):
    '''Creates the shape instances'''

    def get_shape(self, shapeType:str, size:int):
        '''Return shape object'''

        if size <= 0:
            raise ValueError("Received wrong size")

        if shapeType == "circle":
            return Circle(size=size)
        elif shapeType == "square":
            return Square(size=size)
        else:
            raise ValueError("Received unknown shape")
