from math import pi
from .figure import Figure

class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def perimeter(self) -> float:
        return 2 * pi * self.radius

    @property
    def area(self) -> float:
        return pi * self.radius ** 2