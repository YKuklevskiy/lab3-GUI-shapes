from Classes.Shape import Shape
from tkinter import Canvas
import random


class Arrow(Shape):
    def __init__(self):
        self._name = 'arrow'
        self.scale_modifier = 21

    _vertices = ([-3, 1], [0, 1], [0, 2], [2, 0], [0, -2], [0, -1], [-3, -1])


class Triangle(Shape):
    def __init__(self):
        self._name = 'triangle'
        self.scale_modifier = 40

    _vertices = ([0, 1], [1, -1], [-1, -1])


class Square(Shape):
    def __init__(self):
        self._name = 'square'
        self.scale_modifier = 40

    _vertices = ([-1, -1], [1, -1], [1, 1], [-1, 1])


class Circle(Shape):
    def __init__(self):
        self._name = 'circle'
        self.scale_modifier = 40

    _vertices = (-1, -1, 1, 1)

    def draw_shape(self, canvas: Canvas, x, y, scale, rotation):
        border_vertices = [x + scale * self.scale_modifier * -1,
                           y + scale * self.scale_modifier * -1,
                           x + scale * self.scale_modifier * 1,
                           y + scale * self.scale_modifier * 1]

        color = '#' + hex(random.randint(0, 16777215))[2:].zfill(6)
        canvas.create_oval(border_vertices, fill=color)
