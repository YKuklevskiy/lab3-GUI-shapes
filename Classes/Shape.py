from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self):
        self._name = 'name'
        self._vertices = list()
        self.scale_modifier = 1

    def get_name(self):
        return self._name

    @abstractmethod
    def draw_shape(self, canvas, x, y, scale, rotation):
        pass

