from abc import ABC, abstractmethod

class Figure(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    def add_area(self, figure: 'Figure') -> float:
        if not isinstance(figure, Figure):
            raise ValueError("Переданный объект не является геометрической фигурой.")
        return self.area + figure.area