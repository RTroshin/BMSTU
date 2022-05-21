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
c.create_arc(247, 295, 353, 355, 
             start=0,
             extent=-180, 
             style=CHORD,
             fill='#ebbb00',
             outline='#ebbb00')

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
c.create_line(247, 305, 300, 321,
              fill='black')
c.create_line(300, 321, 354, 305,
              fill='black')

# Пятно на нижней части яйца
c.create_arc(190, 326, 410, 411, 
             start=220,
             extent=100, 
             style=CHORD,
             fill='#716f56',
             outline='#716f56')

c.create_arc(240, 388, 360, 410, 
             start=0,
             extent=180, 
             style=CHORD,
             fill='#716f56',
             outline='#716f56')

# ЩЕКИ
##############################################################################

# Левая щека
c.create_arc((182, 200), (292, 445),
             start=90,
             extent=75, 
             style=CHORD,
             fill='#eae265',
             outline='#eae265')

c.create_arc((150, 70), (262, 315),
             start=0,
             extent=-100, 
             style=CHORD,
             fill='#eae265',
             outline='#eae265')

c.create_oval(210, 200, 260, 250, 
             fill='#eae265',
             outline='#eae265')

c.create_oval(185, 270, 230, 315, 
             fill='#eae265',
             outline='#eae265')

# Правая щека
c.create_arc((418, 200), (308, 445),
             start=90,
             extent=-75, 
             style=CHORD,
             fill='#eae265',
             outline='#eae265')

c.create_arc((450, 70), (338, 315),
             start=180,
             extent=100, 
             style=CHORD,
             fill='#eae265',
             outline='#eae265')

c.create_oval(390, 200, 340, 250, 
             fill='#eae265',
             outline='#eae265')

c.create_oval(415, 270, 370, 315, 
             fill='#eae265',
             outline='#eae265')

# ГЛАЗА
##############################################################################

# Левый глаз
c.create_oval((210, 200), (240, 230), 
              fill='white',
              outline='white')
c.create_oval((230, 205), (260, 235), 
              fill='white',
              outline='white')
c.create_polygon((210, 215), (217, 195), (270, 205), (260, 225), 
                  fill='white',
                  outline='white')
c.create_polygon((225, 230), (225, 215), (245, 220), (245, 235), 
                  fill='white',
                  outline='white')

# Зрачок левого глаза
c.create_oval(240, 210, 250, 220, 
              fill='black',
              outline='black')

# Блик зрачка правого глаза
c.create_oval(245, 216, 246, 217, 
              fill='#ffffff',
              outline='#ffffff')

# Обводка левого глаза
c.create_arc((210, 200), (240, 230), 
             start=180,
             extent=90, 
             style=ARC,
             outline='black',
             width=4)
c.create_arc((230, 205), (260, 235), 
             start=-20,
             extent=-70, 
             style=ARC,
             outline='black',
             width=3)
c.create_line((210, 215), (217, 195),
              fill='black',
              width=3)
c.create_line((225, 230), (245, 235),
              fill='black',
              width=3)
c.create_line((270, 203), (258, 228),
              fill='black',
              width=3)

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