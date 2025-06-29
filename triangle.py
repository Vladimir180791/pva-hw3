from math import sqrt
from .figure import Figure

class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        if not self._is_valid_triangle(side_a, side_b, side_c):
            raise ValueError("Invalid triangle sides")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a

    def get_area(self) -> float:
        s = self.get_perimeter() / 2
        return sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    def get_perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c