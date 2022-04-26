from tkinter import *
from random import randint


def graph_py(x, y, w, h):        
    window = Tk()
    canv = Canvas(window, width=w, height=h, bg='#000000', highlightthickness=0)
    canv.pack()

    x.sort()
    for index, i in enumerate(x):
        if index + 1 != len(x):
            canv.create_line(i, y[index], x[index + 1], y[index + 1], fill="#FFFFFF")
            canv.create_text(i, y[index], fill='#BFFF00', text='●')
        canv.after(1)
        canv.update()
    window.mainloop()

w, h = 630, 360

n = 40
list_x = [randint(0, w) for i in range(n)]
list_y = [randint(0, h) for i in range(n)]

graph_py(list_x, list_y, w, h)