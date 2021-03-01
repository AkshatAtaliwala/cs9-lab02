from Shape2D import Shape2D
from Circle import Circle
from Square import Square

def test_Shape2D():
    a = Shape2D()
    assert a.color == None
    assert a.getColor() == None
    assert a.getShapeProperties() == "Shape: N/A, Color: None"
    a.setColor("blue")
    assert a.getColor() == 'blue'
    assert a.color == 'blue'
    assert a.getShapeProperties() == "Shape: N/A, Color: blue"

def test_Circle():
    a = Circle('blue' , 4)
    assert a.color == 'blue'
    assert a.radius == 4
    a.setRadius(5)
    assert a.getRadius() == 5
    assert a.computeArea() == 78.53975
    assert a.computePerimeter() == 31.4159
    assert a.getShapeProperties() == "Shape: CIRCLE, Color: blue, Radius: 5, Area: 78.53975, Perimeter: 31.4159"

def test_Square():
    a = Square('blue', 4)
    assert a.color == 'blue'
    assert a.side == 4
    a.setSide(5)
    assert a.getSide() == 5
    assert a.computeArea() == 25
    assert a.computePerimeter() == 20
    assert a.getShapeProperties() == "Shape: SQUARE, Color: blue, Side: 5, Area: 25, Perimeter: 20"