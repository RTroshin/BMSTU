from tkinter import *

WIDTH = 600
HEIGHT = 600

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

root = Tk()

root.geometry("{:d}x{:d}+200+200".format(WIDTH, HEIGHT))
root.resizable(False, False)
# root.config(bg='#2DFF00')

c = Canvas(root, width=800, height=800, bg='lightblue')
c.pack()

# ВОЛОСЫ НА МАКУШКЕ
##############################################################################

c.create_arc((195, 70), (280, 170), 
             start=0,
             extent=40, 
             style=ARC,
             outline='#111111',
             width=23)
c.create_oval(255, 75, 280, 95, 
              fill='#222222',
              outline='black')
c.create_arc((263, 55), (303, 185), 
             start=0,
             extent=70, 
             style=ARC,
             outline='#000000',
             width=33)
c.create_oval(272, 41, 303, 72, 
              fill='#222222',
              outline='black')
c.create_arc((320, 65), (420, 175), 
             start=180,
             extent=-60, 
             style=ARC,
             outline='#111111',
             width=36)
c.create_oval(324, 55, 362, 89, 
              fill='#222222',
              outline='black')

# ТУЛОВИЩЕ
##############################################################################

# Верхний овал туловища
c.create_oval(170, 110, 430, 500,
              fill='white',
              outline='white')
c.create_rectangle(150, 300, 450, 500,
                   fill='lightblue',
                   outline='lightblue')
# Левый овал туловища
c.create_oval(170, 200, 300, 400,
              fill='white',
              outline='white')
# Правый овал туловища
c.create_oval(300, 200, 430, 400,
              fill='white',
              outline='white')
# Нижний овал туловища
c.create_oval(190, 325, 410, 410,
              fill='white',
              outline='white')

# Ещё немного волос на макушке
c.create_arc((230, 110), (370, 190), 
             start=56,
             extent=60, 
             style=ARC,
             outline='black',
             width=10)

# КЛЮВ
##############################################################################

# Верхняя часть ключа
c.create_arc(243, 200, 357, 560, 
             start=0,
             extent=180, 
             style=CHORD,
             fill='#ebbb00',
             outline='#ebbb00')
c.create_rectangle(240, 324, 360, 400,
                   fill='white',
                   outline='white')

# Нижняя часть ключа
c.create_arc(245, 290, 355, 345, 
             start=0,
             extent=-180, 
             style=CHORD,
             fill='orange',
             outline='orange')

# Блин на клюве
# Верхняя часть блика
# c.create_arc(390, 243, 410, 393, 
#              start=0, extent=180, 
#              style=CHORD, fill='white',
#              outline='white')

# Нижняя часть блика
# c.create_arc(390, 300, 410, 325, 
#              start=180, extent=180, 
#              style=CHORD, fill='white',
#              outline='white')

# Рот
# c.create_line(360, 300, 400, 308,
#               fill='black')
# c.create_line(400, 308, 440, 300,
#               fill='black')

# ЩЕКИ
##############################################################################

# Левая щека
c.create_oval(190, 190, 250, 250, 
             fill='yellow',
             outline='black')

c.create_oval(185, 270, 230, 315, 
             fill='yellow',
             outline='black')

# Правая щека
c.create_oval(410, 190, 350, 250, 
             fill='yellow',
             outline='black')

c.create_oval(415, 270, 370, 315, 
             fill='yellow',
             outline='black')

# ГЛАЗА
##############################################################################

# Левый глаз
c.create_oval(210, 200, 240, 230, 
              fill='white',
              outline='black')
c.create_oval(230, 205, 260, 235, 
              fill='white',
              outline='black')
c.create_polygon((210, 215), (217, 195), (270, 205), (260, 225), 
                  fill='white',
                  outline='black')
c.create_polygon((225, 230), (225, 215), (245, 220), (245, 235), 
                  fill='white',
                  outline='black')

# Зрачок левого глаза
c.create_oval(240, 210, 250, 220, 
              fill='black',
              outline='black')

# Обводка левого глаза

# Правый глаз
c.create_oval(390, 200, 360, 230, 
              fill='white',
              outline='black')
c.create_oval(370, 205, 340, 235, 
              fill='white',
              outline='black')
c.create_polygon((390, 215), (383, 195), (330, 205), (340, 225), 
                  fill='white',
                  outline='black')
c.create_polygon((375, 215), (375, 230), (355, 235), (355, 220), 
                  fill='white',
                  outline='black')

# Зрачок правого глаза
c.create_oval(360, 210, 350, 220, 
              fill='black',
              outline='black')

# БРОВИ
##############################################################################

# Левая бровь
c.create_polygon((205, 195), (203, 175), (288, 185), (275, 205), 
                   fill='black',
                   outline='black')

# Правая бровь
c.create_polygon((312, 185), (325, 205), (395, 195), (397, 175), 
                   fill='black',
                   outline='black')

# ХВОСТ
##############################################################################


# ГНЕЗДО
##############################################################################

# # Трава
# x1 = 5
# x2 = 55
# for i in range(26):
#     c.create_arc(x1, 400, x2, 310, start=180, extent=-65, style=ARC, outline='green', width=3)
#     x1 += 15
#     x2 += 15

root.mainloop()