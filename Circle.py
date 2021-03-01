
from Shape2D import Shape2D

class Circle(Shape2D):
    ''' Circle Subclass from Shape2D '''

    def __init__(self, color, radius = None):
        super().__init__(color)
        self.radius = radius
    
    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius
    
    def computeArea(self):
        area = 3.14159 * (self.radius * self.radius)
        return area
    
    def computePerimeter(self):
        perimeter = 2 * self.radius * 3.14159
        return perimeter
    
    def getShapeProperties(self):
        area = self.computeArea()
        perimeter = self.computePerimeter()
        return "Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}".format(self.color, self.radius, area, perimeter)
       