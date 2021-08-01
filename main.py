# Написать программу, которая будет по нажатию на экран рисовать фигуру в месте клика. Фигура - стрелочка.
#
# 1) Сделать слайдер, который будет отвечать за размер фигуры, рядом выводить значение слайдера.
# 2) Сделать слайдер для поворота фигуры, рядом выводить значение слайдера.

# Интерфейс: Справа канвас, слева выбор фигуры, слайдер размера, слайдер поворота

from tkinter import *
from tkinter.ttk import Combobox

WINDOW_SIZE = 800
window = Tk()
window.title('Shapes!')

# Isn't required
# window.geometry(f'{WINDOW_SIZE+200}x{WINDOW_SIZE}')

param_frame = Frame(window)

scale_label = Label(param_frame, text='Shape scale:')
scale_slider = Scale(param_frame, orient=HORIZONTAL, length=200, from_=0, to_=2, resolution=.1)
scale_slider.set(1)

rotation_label = Label(param_frame, text='Shape rotation:')
rotation_slider = Scale(param_frame, orient=HORIZONTAL, length=200, from_=0, to_=359, resolution=1)
rotation_slider.set(0)

shape_menu = Combobox(param_frame)
shapes = ['Choose the shape...']
# Requires implementation of class Shape and all the needed Shape classes
# shapes.append(shape_names.keys())
shape_menu['values'] = tuple(shapes)
shape_menu.current(0)

canvas = Canvas(window, width=WINDOW_SIZE, height=WINDOW_SIZE, bg='white')

scale_label.grid(column=0, row=0)
scale_slider.grid(column=0, row=1)
rotation_label.grid(column=0, row=2)
rotation_slider.grid(column=0, row=3)
shape_menu.grid(column=0, row=4)

param_frame.grid(column=0, row=0)
canvas.grid(column=1, row=0)


def draw_polygon(coordinates):
        canvas.create_polygon(tuple())


window.resizable(0, 0)

window.mainloop()
