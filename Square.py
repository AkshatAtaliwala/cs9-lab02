
from Shape2D import Shape2D

class Square(Shape2D):
    ''' Subclass with the defenition of what a 2D Square is. '''

    def __init__(self, color, side = None):
        super().__init__(color)
        self.side = side
    
    def getSide(self):
        return self.side
    
    def setSide(self, side):
        self.side = side

    def computeArea(self):
        area = self.side * self.side
        return area
    
    def computePerimeter(self):
        perimeter = self.side * 4
        return perimeter
    
    def getShapeProperties(self):
        area = self.computeArea()
        perimeter = self.computePerimeter()
        return "Shape: SQUARE, Color: {}, Side: {}, Area: {}, Perimeter: {}".format(self.color, self.side, area, perimeter)
