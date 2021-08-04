import math
from copy import deepcopy
import random


# base class for shape classes
class Shape:
    def __init__(self):
        self._name = 'name'
        self.scale_modifier = 1
        # base scale modifier - so that it would be easier to input base vertex coordinates for shapes

    _vertices = list()

    def get_name(self):
        return self._name

    def transform_poly(self, vertices, x, y, scale=1, rotation=0):
        for i in range(len(vertices)):
            # scale
            vertices[i][0] = vertices[i][0] * self.scale_modifier * scale
            vertices[i][1] = vertices[i][1] * self.scale_modifier * scale

            # rotation
            temp_x = vertices[i][0]
            temp_y = vertices[i][1]
            vertices[i][0] = temp_x * math.cos(rotation) + temp_y * math.sin(rotation)
            vertices[i][1] = -(temp_y * math.cos(rotation) - temp_x * math.sin(rotation))
            # Negative due to OY axis directed down

            # translation
            vertices[i][0] = x + vertices[i][0]
            vertices[i][1] = y + vertices[i][1]
        return vertices

    def draw_shape(self, canvas, x, y, scale, rotation):  # not abstract as its not same for every shape (e.g. circle)
        rad_rotation = rotation / 180.0 * math.pi
        vertices = self.transform_poly(deepcopy(self._vertices), x, y, scale, rad_rotation)

        color = '#' + hex(random.randint(0, 2**24-1))[2:].zfill(6)  # random shape fill color
        canvas.create_polygon(vertices, fill=color, outline='black')
