import pytest
from src.triangle import Triangle

class TestTriangle:
    def test_valid_triangle(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.area == 6.0
        assert triangle.perimeter == 12

    def test_invalid_triangle(self):
        with pytest.raises(ValueError, match="Треугольник с такими сторонами не существует."):
            Triangle(1, 1, 10)