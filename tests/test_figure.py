import pytest
from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle

class TestFigure:
    @pytest.mark.parametrize(
        "figure1, figure2, expected_sum",
        [
            (Circle(5), Rectangle(4, 5), Circle(5).area + Rectangle(4, 5).area),
            (Circle(3), Circle(2), Circle(3).area + Circle(2).area),
            (Rectangle(2, 3), Rectangle(4, 5), Rectangle(2, 3).area + Rectangle(4, 5).area),
        ],
    )
    def test_add_area(self, figure1, figure2, expected_sum):
        """Проверяет, что метод add_area корректно складывает площади двух фигур."""
        assert figure1.add_area(figure2) == expected_sum

    @pytest.mark.parametrize(
        "figure, invalid_object, expected_error_msg",
        [
            (Circle(5), "not a figure", "Переданный объект не является геометрической фигурой."),
            (Rectangle(4, 5), 123, "Переданный объект не является геометрической фигурой."),
            (Circle(3), None, "Переданный объект не является геометрической фигурой."),
        ],
    )
    def test_add_area_invalid_type(self, figure, invalid_object, expected_error_msg):
        """Проверяет, что при передаче неверного типа вызывается ValueError."""
        with pytest.raises(ValueError, match=expected_error_msg):
            figure.add_area(invalid_object)