# Разработать приложение с графическим интерфейсом для решения поставленной
# задачи. Приложение позволяет пользователю задавать параметры фигур как с
# помощью клавиатуры, вводя цифровые значения, так и задавая мышкой
# характеристики фигуры на поле графического экрана.
# (Только для групп ИУ7-24Б-25Б. Остальным только ввод с клавиатуры).
#
# Также необходимо сделать графическую интерпретацию* полученного решения.
#
# Индивидуальные задания
# Заданы два множества точек. Найти такой треугольник с вершинами – точками
# первого множества, внутри которого находится одинаковое количество точек
# из первого и из второго множеств.
#
# Дать графическое изображение результатов.
#
# * -- изображение создается с использованием виджета Canvas tkinter.

# Функционал
# 1. Кнопка "Очистить"
# 2. Кнопка "Отменить последнее действие"
# 3. Ввод кординат через поля
# 4. Блокировать ввод букв
# 5. Добавление точек во множества с помощью нажатий на клавиши мыши
# 6. Меню
# 7. "О программе" в меню
# 8. Нарисовать шкалу с пикселями (как в Gimp) на полотне
# 9. Подсказки (сделать приложение так, чтобы было понятно, что в нем нужно делать)

from tkinter import *

# Параметры поля
WIDTH = 1000
HEIGHT = 700
WIDTH_CANVAS = 600
HEIGHT_CANVAS = 700

# Цвета
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

# Создание кнопки для первого множества
def makeBlackButton(cnvs, entryX, entryY, name, blackSet):
    button = Button(bg='#000000',
                    text=name,
                    font=('Roboto', 16),
                    fg='#EEEEEE',
                    activebackground='#222222',
                    activeforeground="#EEEEEE",
                    command=lambda : addBlackPoint(cnvs, entryX, entryY, blackSet))
    return button

# Создание кнопки для второго множества
def makeRedButton(cnvs, entryX, entryY, name, redSet):
    button = Button(bg='#000000',
                    text=name,
                    font=('Roboto', 16),
                    fg='#EEEEEE',
                    activebackground='#222222',
                    activeforeground="#EEEEEE",
                    command=lambda : addRedPoint(cnvs, entryX, entryY, redSet))
    return button

# Добавление точки в множество через клик мыши
def addBlackPoint(x, y, cnvs, blackSet):
    blackSet.append([x, y])
    # print(blackSet)
    i = len(blackSet) - 1
    # entry.insert(0, value + digit) # TO DO При вводе с помощью мышки, дублировать координаты в окна ввода
    cnvs.create_oval((int(blackSet[i][0]), int(blackSet[i][1])),
                     (int(blackSet[i][0]) + 5, int(blackSet[i][1]) + 5),
                     fill='#000000',
                     outline='#000000')

# Добавление точки в множество через клик мыши
def addRedPoint(x, y, cnvs, redSet):
    redSet.append([x, y])
    # print(redSet)
    i = len(redSet) - 1
    # entry.insert(0, value + digit) # TO DO При вводе с помощью мышки, дублировать координаты в окна ввода
    cnvs.create_oval((int(redSet[i][0]), int(redSet[i][1])),
                     (int(redSet[i][0]) + 5, int(redSet[i][1]) + 5),
                     fill='#ff0800',
                     outline='#ff0800')

# Ограничение ввода с клавиатуры (только цифры и знаки операций)
def pressLeftKey(event, cnvs, blackSet):
    # print(event.x)
    # print(event.y)
    x = event.x
    y = event.y

    # Если в множестве уже есть данная точка, то повторно не добавлять
    if [x, y] not in blackSet:
        addBlackPoint(x, y, cnvs, blackSet)

# Нажатие на правую кнопку мыши
def pressRightKey(event, cnvs, redSet):
    # print(event.x)
    # print(event.y)
    x = event.x
    y = event.y

    # Если в множестве уже есть данная точка, то повторно не добавлять
    if [x, y] not in redSet:
        addRedPoint(x, y, cnvs, redSet)

def main():

    # Множества точек
    blackSet = []
    redSet = []

    root = Tk()

    # TO DO Изменить значок приложения

    root.title("Планиметрия")
    root.config(bg='#222222') # Установить фон
    root.geometry("{:d}x{:d}+200+200".format(WIDTH, HEIGHT))
    root.resizable(False, False)

    root.attributes("-alpha", 0.97) # Делает фон прозрачным

    label1 = Label(root,
                   text='Введите координаты точки в первое множество',
                   bg='#222222',
                   fg='white',
                   font=('Roboto', 14, 'bold'),
                   padx=20,
                   pady=20,
                   width=40,
                   anchor="sw",
                   justify=LEFT)

    label2 = Label(root,
                   text='Введите координаты точки во второе множество',
                   bg='#222222',
                   fg='white',
                   font=('Roboto', 14, 'bold'),
                   padx=20,
                   pady=20,
                   width=40,
                   anchor="sw",
                   justify=LEFT)

    labelX1 = Label(root,
                    text='X1',
                    bg='#222222',
                    fg='white',
                    font=('Roboto', 14, 'bold'),
                    padx=20,
                    pady=20,
                    width=40,
                    anchor="sw",
                    justify=LEFT)

    labelY1 = Label(root, text='Y1',
                    bg='#222222',
                    fg='white',
                    font=('Roboto', 14, 'bold'),
                    padx=20,
                    pady=20,
                    width=40,
                    anchor="sw",
                    justify=LEFT)

    labelX2 = Label(root, text='X_2',
                    bg='#222222',
                    fg='white',
                    font=('Roboto', 14, 'bold'),
                    padx=20,
                    pady=20,
                    width=40,
                    anchor="sw",
                    justify=LEFT)

    labelY2 = Label(root, text='Y2',
                    bg='#222222',
                    fg='white',
                    font=('Roboto', 14, 'bold'),
                    padx=20,
                    pady=20,
                    width=40,
                    anchor="sw",
                    justify=LEFT)

    # Создание окна ввода
    entryX1 = Entry(root,
                    bd = 0,
                    disabledbackground='#222222',
                    disabledforeground='#EEEEEE',
                    justify=RIGHT,
                    font=('Roboto', 14),
                    width=15)
    entryY1 = Entry(root,
                    bd = 0,
                    disabledbackground='#222222',
                    disabledforeground='#EEEEEE',
                    justify=RIGHT,
                    font=('Roboto', 14),
                    width=15)

    entryX2 = Entry(root,
                    bd = 0,
                    disabledbackground='#222222',
                    disabledforeground='#EEEEEE',
                    justify=RIGHT,
                    font=('Roboto', 14),
                    width=15)
    entryY2 = Entry(root,
                    bd = 0,
                    disabledbackground='#222222',
                    disabledforeground='#EEEEEE',
                    justify=RIGHT,
                    font=('Roboto', 14),
                    width=15)

# Размещение элементов

    label1.grid(row=0,
                column=0,
                columnspan=4,
                stick='wens',
                padx=1)

    label2.grid(row=3,
                column=0,
                columnspan=4,
                stick='wens',
                padx=1)

    labelX1.grid(row=1,
                 column=0,
                 stick='wens',
                 padx=1)

    labelY1.grid(row=1,
                 column=2,
                 stick='wens',
                 padx=1)

    labelX2.grid(row=4,
                 column=0,
                 stick='wens',
                 padx=1)

    labelY2.grid(row=4,
                 column=2,
                 stick='wens',
                 padx=1)


    entryX1.grid(row=1,
                 column=1,
                 stick='wens',
                 padx=1)

    entryY1.grid(row=1,
                 column=3,
                 stick='wens',
                 padx=1)

    entryX2.grid(row=4,
                 column=1,
                 stick='wens',
                 padx=1)

    entryY2.grid(row=4,
                 column=3,
                 stick='wens',
                 padx=1)

    cnvs = Canvas(root,
                  width=WIDTH_CANVAS,
                  height=HEIGHT_CANVAS,
                  bg='#ffffff')

    cnvs.grid(row=0,
              column=4,
              rowspan=6,
              stick='wens',
              padx=1)

    button1 = makeBlackButton(cnvs, entryX1, entryY1, 'Добавить точку', blackSet)
    button1.grid(row=2,
                 column=0,
                 columnspan=4,
                 stick='wens',
                 padx=1,
                 pady=1)

    button2 = makeBlackButton(cnvs, entryX2, entryY2, 'Добавить точку', blackSet)
    button2.grid(row=5,
                 column=0,
                 columnspan=4,
                 stick='wens',
                 padx=1,
                 pady=1)
    # button1.bind("<Enter>", lambda event : on_enter_digit(button1, event))
    # button1.bind("<Leave>", lambda event : on_leave_digit(button1, event))

    # button2 = makeDigitButton(cnvs, coordinates, 'Найти треугольник')
    # button2.grid(row=7,
    #              column=1,
    #              stick='wens',
    #              padx=1,
    #              pady=1)
    # button2.bind("<Enter>", lambda event : on_enter_digit(button2, event))
    # button2.bind("<Leave>", lambda event : on_leave_digit(button2, event))

    cnvs.bind('<Button-1>', lambda event : pressLeftKey(event, cnvs, blackSet))
    cnvs.bind('<Button-3>', lambda event : pressRightKey(event, cnvs, redSet))

    print(blackSet)
    print(redSet)

    # Установка минимальных размеров кнопок
    root.grid_columnconfigure(0, minsize=10)
    root.grid_columnconfigure(1, minsize=10)
    root.grid_columnconfigure(2, minsize=10)
    root.grid_columnconfigure(3, minsize=10)
    root.grid_columnconfigure(4, minsize=700)

    root.grid_rowconfigure(0, minsize=10)
    root.grid_rowconfigure(1, minsize=10)
    root.grid_rowconfigure(2, minsize=10)
    root.grid_rowconfigure(3, minsize=10)
    root.grid_rowconfigure(4, minsize=10)
    root.grid_rowconfigure(5, minsize=10)

    root.mainloop()

if __name__ == '__main__':
    main()
