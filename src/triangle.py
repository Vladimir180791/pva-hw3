from math import sqrt
from .figure import Figure

class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        if not self._is_valid(a, b, c):
            raise ValueError("Треугольник с такими сторонами не существует.")
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def _is_valid(a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a

    @property
    def perimeter(self) -> float:
        return self.a + self.b + self.c

    @property
    def area(self) -> float:
        p = self.perimeter / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))