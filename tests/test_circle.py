import math
from src.circle import Circle

class TestCircle:
    def test_area_and_perimeter(self):
        circle = Circle(3)
        assert circle.area == math.pi * 9
        assert circle.perimeter == math.pi * 6