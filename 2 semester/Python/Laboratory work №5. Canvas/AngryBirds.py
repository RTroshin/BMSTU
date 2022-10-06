from tkinter import *
from os.path import dirname, join

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

def moveEyebrows():
    c.move(Eyebrow, 1, 0)

# Создание переменной, содержащей полный путь до файла
currentDir = dirname(__file__)
filePath = join(currentDir, "./Pictures/Red.png")

root = Tk()

# Установка иконки приложения
photo = PhotoImage(file=filePath)
root.iconphoto(False, photo)

root.title("Angry Birds") # Изменение заголовка приложения

root.geometry("{:d}x{:d}+200+200".format(WIDTH, HEIGHT))
root.resizable(False, False)
# root.config(bg='#2DFF00')

c = Canvas(root,
           width=WIDTH,
           height=HEIGHT,
           bg='lightblue')
c.pack()

# ПЕРЬЯ НА МАКУШКЕ
##############################################################################

c.create_arc((195, 70), (280, 170),
             start=0,
             extent=40,
             style=ARC,
             outline='#111111',
             width=23)
c.create_oval((255, 75), (280, 95),
              fill='#222222',
              outline='black')
c.create_arc((263, 55), (303, 185),
             start=0,
             extent=70,
             style=ARC,
             outline='#000000',
             width=33)
c.create_oval((272, 41), (303, 72),
              fill='#222222',
              outline='black')
c.create_arc((320, 65), (420, 175),
             start=180,
             extent=-60,
             style=ARC,
             outline='#111111',
             width=36)
c.create_oval((324, 55), (362, 89),
              fill='#222222',
              outline='black')

# ТУЛОВИЩЕ
##############################################################################

# Верхний овал туловища
c.create_oval((170, 110), (430, 500),
              fill='white',
              outline='white')
c.create_rectangle((150, 300), (450, 500),
                   fill='lightblue',
                   outline='lightblue')

# ФОН
##############################################################################

# Трава
c.create_oval((-300, 350), (900, 800),
              fill='#464622',
              outline='#464622')

# Трава (темная)
c.create_oval((-300, 400), (200, 800),
              fill='#1a2012',
              outline='#1a2012')

# Трава (светлая)
c.create_oval((300, 400), (800, 800),
              fill='#5a5626',
              outline='#5a5626')

# Трава (очень светлая)
c.create_oval((400, 500), (800, 800),
              fill='#72662a',
              outline='#72662a')

# Тень
c.create_oval((175, 375), (425, 425),
              fill='#222222',
              outline='#222222')

# ТУЛОВИЩЕ (ПРОДОЛЖЕНИЕ)
##############################################################################

# Левый овал туловища
c.create_oval((170, 200), (300, 400),
              fill='white',
              outline='white')

# Правый овал туловища
c.create_oval((300, 200), (430, 400),
              fill='white',
              outline='white')

# Нижний овал туловища
c.create_oval((190, 325), (410, 410),
              fill='white',
              outline='white')

# Ещё немного перьев на макушке
c.create_arc((230, 110), (370, 190),
             start=56,
             extent=60,
             style=ARC,
             outline='black',
             width=10)

# КЛЮВ
##############################################################################

# Верхняя часть ключа
c.create_arc((243, 200), (357, 560),
             start=0,
             extent=180,
             style=CHORD,
             fill='#ebbb00',
             outline='#ebbb00')

c.create_rectangle((240, 324), (360, 400),
                   fill='white',
                   outline='white')

# Нижняя часть ключа
c.create_arc((247, 295), (353, 355),
             start=0,
             extent=-180,
             style=CHORD,
             fill='#ebbb00',
             outline='#ebbb00')

# БЛИК НА КЛЮВЕ
##############################################################################

# Верхняя часть блика
c.create_arc((280, 243), (320, 393),
             start=0,
             extent=180,
             style=CHORD,
             fill='#eebf00',
             outline='#eebf00')

# Нижняя часть блика
c.create_arc((280, 290), (320, 345),
             start=180,
             extent=180,
             style=CHORD,
             fill='#eebf00',
             outline='#eebf00')

# Верхняя часть блика (светлая)
c.create_arc((292, 250), (308, 393),
             start=0,
             extent=180,
             style=CHORD,
             fill='#f6c801',
             outline='#f6c801')

# Нижняя часть блика (светлая)
c.create_arc((292, 290), (308, 340),
             start=180,
             extent=180,
             style=CHORD,
             fill='#f6c801',
             outline='#f6c801')

# Верхняя часть блика (самая светлая)
c.create_arc((297, 255), (303, 393),
             start=0,
             extent=180,
             style=CHORD,
             fill='#fad00c',
             outline='#fad00c')

# Нижняя часть блика (самая светлая)
c.create_arc((297, 290), (303, 335),
             start=180,
             extent=180,
             style=CHORD,
             fill='#fad00c',
             outline='#fad00c')

# Рот
c.create_line((248, 305), (300, 321),
              fill='#c28b00',
              width=4)
c.create_line((300, 321), (353, 305),
              fill='#c28b00',
              width=4)
c.create_line((248, 307), (300, 323),
              fill='#fad00c',
              width=4)
c.create_line((300, 323), (353, 307),
              fill='#fad00c',
              width=4)

# Пятно на нижней части яйца
c.create_arc((190, 326), (410, 411),
             start=220,
             extent=100,
             style=CHORD,
             fill='#716f56',
             outline='#716f56')

c.create_arc((240, 388), (360, 410),
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

c.create_oval((210, 200), (260, 250),
             fill='#eae265',
             outline='#eae265')

c.create_oval((185, 270), (230, 315),
             fill='#eae265',
             outline='#eae265')

# Заполнение щеки
c.create_oval((190, 230), (235, 300),
             fill='#eae265',
             outline='#eae265')

# Блик щеки
c.create_oval((195, 235), (245, 285),
              fill='#eee56e',
              outline='#eee56e')

# Блик щеки (светлая часть)
c.create_oval((205, 245), (235, 275),
              fill='#f2eb79',
              outline='#f2eb79')

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

c.create_oval((390, 200), (340, 250),
              fill='#eae265',
              outline='#eae265')

c.create_oval((415, 270), (370, 315),
              fill='#eae265',
              outline='#eae265')

# Заполнение щеки
c.create_oval((410, 230), (365, 300),
              fill='#eae265',
              outline='#eae265')

# Блик щеки
c.create_oval((405, 235), (355, 285),
              fill='#eee56e',
              outline='#eee56e')

# Блик щеки (светлая часть)
c.create_oval((395, 245), (365, 275),
              fill='#f2eb79',
              outline='#f2eb79')

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
c.create_oval((240, 210), (250, 220),
              fill='black',
              outline='black')

# Блик зрачка левого глаза
c.create_oval((245, 216), (246, 217),
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
c.create_oval((390, 200), (360, 230),
              fill='white',
              outline='white')
c.create_oval((370, 205), (340, 235),
              fill='white',
              outline='white')
c.create_polygon((390, 215), (383, 195), (330, 205), (340, 225),
                 fill='white',
                 outline='white')
c.create_polygon((375, 215), (375, 230), (355, 235), (355, 220),
                 fill='white',
                 outline='white')

# Зрачок правого глаза
c.create_oval((360, 210), (350, 220),
              fill='#000000',
              outline='#000000')

# Блик зрачка правого глаза
c.create_oval((355, 216), (354, 217),
              fill='#ffffff',
              outline='#ffffff')

# Обводка правого глаза
c.create_arc((390, 200), (360, 230),
             start=0,
             extent=-90,
             style=ARC,
             outline='black',
             width=4)
c.create_arc((370, 205), (340, 235),
             start=200,
             extent=70,
             style=ARC,
             outline='black',
             width=3)
c.create_line((390, 215), (383, 195),
              fill='black',
              width=3)
c.create_line((375, 230), (355, 235),
              fill='black',
              width=3)
c.create_line((330, 203), (342, 228),
              fill='black',
              width=3)

# БРОВИ
##############################################################################

# Левая бровь
eyebrow = c.create_polygon((207, 195), (205, 175), (288, 185), (275, 205),
                           fill='black',
                           outline='black')

# Правая бровь
eyebrow = c.create_polygon((312, 185), (325, 205), (393, 195), (395, 175),
                           fill='black',
                           outline='black')

if (c.bind('<Button-1>')):
    moveEyebrows()

# ХВОСТ
##############################################################################


# ГНЕЗДО
##############################################################################

# Оттенки коричневого
#5d3830
#815339
#56332f
#a36840
#80583f
#513426
#7e5843
#5d3830
#573529

# c.create_oval((250, 450), (550, 550),
#               fill='#ffffff',
#               outline='black')

# # c.create_line((230, 500), (350, 440),
# #               fill='grey',
# #               width=10)
# # c.create_line((330, 450), (500, 450),
# #               fill='grey',
# #               width=10)
# # c.create_line((470, 450), (550, 490),
# #               fill='grey',
# #               width=10)
# c.create_line((560, 420), (545, 510),
#               fill='grey',
#               width=10)
# c.create_line((550, 510), (470, 550),
#               fill='grey',
#               width=10)
# c.create_line((470, 550), (350, 540),
#               fill='grey',
#               width=10)
# c.create_line((350, 540), (250, 520),
#               fill='grey',
#               width=10)
# c.create_line((250, 530), (230, 460),
#               fill='grey',
#               width=10)
# c.create_line((230, 500), (400, 480),
#               fill='grey',
#               width=10)
# c.create_line((400, 480), (560, 420),
#               fill='grey',
#               width=10)

root.mainloop()
