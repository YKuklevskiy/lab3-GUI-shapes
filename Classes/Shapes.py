from Classes.Shape import Shape
import math
from tkinter import Canvas


class Arrow(Shape):
    def __init__(self):
        self._name = 'arrow'
        self._vertices = [(-3, 1), (0, 1), (0, 2), (2, 0), (0, -2), (0, -1), (-3, -1)]
        self.scale_modifier = 100

    def draw_shape(self, canvas: Canvas, x, y, scale, rotation):
        vertices = self._vertices
        rad_rotation = rotation / 180.0 * math.pi

        for i in range(len(vertices)):
            # scale
            vertices[i][0] = vertices[i][0] * self.scale_modifier * scale
            vertices[i][1] = vertices[i][1] * self.scale_modifier * scale

            # rotation
            temp_x = vertices[i][0]
            temp_y = vertices[i][1]
            vertices[i][0] = temp_x * math.cos(rad_rotation) + temp_y * math.sin(rad_rotation)
            vertices[i][1] = temp_y * math.cos(rad_rotation) - temp_x * math.sin(rad_rotation)

            # translation
            vertices[i][0] = x + vertices[i][0]
            vertices[i][1] = y + vertices[i][1]

        canvas.create_polygon(vertices)

