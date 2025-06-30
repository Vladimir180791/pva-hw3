import math
import pytest
from src.circle import Circle

class TestCircle:
    @pytest.mark.parametrize(
        "radius, expected_area, expected_perimeter",
        [
            (3, math.pi * 9, math.pi * 6),
            (5, math.pi * 25, math.pi * 10),
            (0, 0, 0),
            (1, math.pi * 1, math.pi * 2),
        ],
    )
    def test_area_and_perimeter(self, radius, expected_area, expected_perimeter):
        circle = Circle(radius)
        assert circle.area == expected_area
        assert circle.perimeter == expected_perimeter