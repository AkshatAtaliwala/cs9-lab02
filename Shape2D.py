
class Shape2D:
    ''' Base class that contains what a general 2D shape is '''

    def __init__(self, color = None):
        self.color = color

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def getShapeProperties(self):
        return "Shape: N/A, Color: {}".format(self.color)