import pytest
from math import pi
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi * self.r * self.r
def test_shapes_area():
    r = Rectangle(4, 5)
    c = Circle(7)
    assert r.area() == 20
    assert round(c.area(), 2) == round(pi * 49, 2)
