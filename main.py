# Написать программу, которая будет по нажатию на экран рисовать фигуру в месте клика. Фигура - стрелочка.
#
# 1) Сделать слайдер, который будет отвечать за размер фигуры, рядом выводить значение слайдера.
# 2) Сделать слайдер для поворота фигуры, рядом выводить значение слайдера.

# Интерфейс: Справа канвас, слева выбор фигуры, слайдер размера, слайдер поворота, сообщения об ошибках

from tkinter import *
from tkinter.ttk import Combobox
from Classes.Shapes import *

CANVAS_SIZE = 800
window = Tk()
window.title('Shapes!')

param_frame = Frame(window)  # main widget frame

# scaling widgets
scale_label = Label(param_frame, text='Shape scale:')
scale_slider = Scale(param_frame, orient=HORIZONTAL, length=200, from_=0, to_=2, resolution=.1)
scale_slider.set(1)

# rotation widgets
rotation_label = Label(param_frame, text='Shape rotation:')
rotation_slider = Scale(param_frame, orient=HORIZONTAL, length=200, from_=0, to_=359, resolution=1)
rotation_slider.set(0)

# dropdown menu for available
shape_names = {'Arrow': Arrow(), 'Triangle': Triangle(), 'Square': Square(), 'Circle': Circle()}
shape_menu = Combobox(param_frame)
shapes = list(shape_names.keys())
shapes.insert(0, 'Choose the shape...')
shape_menu['values'] = tuple(shapes)
shape_menu.current(0)

# label for error messages etc
info_label = Label(param_frame, text='', fg='red')

canvas = Canvas(window, width=CANVAS_SIZE, height=CANVAS_SIZE, bg='white')

# main frame setup
scale_label.grid(column=0, row=0)
scale_slider.grid(column=0, row=1)
rotation_label.grid(column=0, row=2)
rotation_slider.grid(column=0, row=3)
shape_menu.grid(column=0, row=4)
info_label.grid(column=0, row=5)

# gui layout setup
param_frame.grid(column=0, row=0)
canvas.grid(column=1, row=0)

# draw chosen polygon on m1 click
def draw_polygon(event):
    shape = shape_menu.get()
    if shape in shape_names:  # correct shape chosen
        info_label.configure(text='')
        shape_names[shape].draw_shape(canvas, event.x, event.y, scale_slider.get(), rotation_slider.get())
    else:
        info_label.configure(text='Please, choose \nthe correct shape')


canvas.bind('<Button-1>', draw_polygon)

window.resizable(0, 0)
window.mainloop()
