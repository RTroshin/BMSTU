# Составить приложение, используя модуль создания оконных приложений Tkinter,
# реализующее индивидуальное задание (выбирается согласно номеру студента в
# списке).
# Интерфейс должен предоставлять ввод символов: как числовых, так и знаков
# операций - и с использованием клавиатуры, и с помощью кнопок приложения.
# Также в приложении необходимо создать меню, в котором должны быть
# следующие пункты:
# - заданные действия,
# - очистка полей ввода/вывода (по одному и всех сразу),
# - информация о программе и авторе.
#
# Использование встроенных функций bin(), oct(), hex() запрещено.
#
# TODO Project
# 1. Добавить файл readme.md.
# 2.

# TODO Calculator
# 1. Если знак операции последний, то при нажатии на кнопку другой операции,
#    она заменяют собой нынешнюю
# 2. При открытии калькулятора первым должен отображаться ноль
# 3. При нажатии цифры и последующем нажатии Enter (=), должна выполняться
#    операция с этим же числом (2+ = 2+2 и т.д.)
# 4. Сделать две строчки. В верхней строчке записывается история операций,
#    во второй ответ
# 5. Максимальное количество символов в окне вывода - 32
# 6. Если превышено максимальное количество символов, то перейти на
#    спецификатор(?) e (запись степени через e)
# 7. Учесть деление на ноль
# 8. Учесть ввод букв латиница и кирилицы
# 9. Релизовать ввод с клавиатуры
# 10. 
# 11. Реализовать ввод числа в степени e
# 12. Учесть невлезающие символы после запятой и если число слишком большое
# 13. Перевод в различные системы счисления сделать кнопками над CE, C, Del
# 14. При переводе в любую систему счислению отличную от 10-чной, блокировать кнопку +/-
# 15. Доработать поля ввода, чтобы туда не влезало больше 32 символов (смотри калькулятор Windows)
# 16. Уменьшать шрифт, если число становится все больше и больше
# 17. Добавить подсветку кнопок при наведении мыши
# 18. Добавить журнал операций справа, выдвигающийся по кнопке
# 19. Добавить в меню дублирование операций
# 20. Добавить в меню о программе и об авторе
# 21. Добавить смену темной темы на светлую (?)
# 22. Сделать кнопки CE и Del
# 23. Исправить маленький значок калькулятора
# 24. Сделать знак ЗАПЯТАЯ ,
# 25. Уменьшить сам калькулятор. Сделать компактнее

from tkinter import Tk, Menu, OptionMenu, PhotoImage, Entry, Button
from tkinter import messagebox
from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from os.path import dirname, join


block = False # Глобальная переменная


# Создание кнопок с 0 по 9
def makeDigitButton(calc, digit):
    return Button(bg='#000000',
                  text=digit,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#111111',
                  activeforeground="#EEEEEE",
                  command=lambda : addDigit(calc, digit))


# Создание кнопок с операциями
def makeOperationButton(calc, calcHistory, operation):
    return Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#333333',
                  activeforeground='#EEEEEE',
                  command=lambda : addOperation(calc, calcHistory, operation))


# Создание кнопок для взаимодействия с полем ввода
def makeCalculateButton(calc, calcHistory, operation):
    return Button(bg='#04346C',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#0C4487',
                  activeforeground='#EEEEEE',
                  command=lambda : calculate(calc, calcHistory))


# Создание кнопки очистки поля ввода
def makeClearButton(calc, calcHistory, operation):
    return Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#333333',
                  activeforeground='#EEEEEE',
                  command=lambda : clear(calc, calcHistory))


# Добавление цифры в поле ввода
def addDigit(calc, digit):
    global block
    if (block != True):
        value = calc.get()

        # Условие для того, чтобы по-умолчанию в меню ввода появлялся ноль
        if value[0] == '0' and len(value) == 1:
            value = value[1:]

        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + digit)
        calc['state'] = DISABLED


# Добавление знака операции в поле ввода
def addOperation(calc, calcHistory, operation):
    global block
    if (block != True):
        value = calc.get()
        value = replaceSymbol(value)

        # Условие для того, чтобы операции отображались как в калькуляторе Windows
        if value[-1] in '-+/*':
            value = value[:-1]
        # Условие для того, чтобы выполнялось предварительное вычисление
        elif '+' in value or '-' in value or '/' in value or '*' in value:
            calculate(calc, calcHistory)
            value = calc.get()

        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + operation)
        calc['state'] = DISABLED


# Вычисление выражения в поле ввода
def calculate(calc, calcHistory):
    global block
    if (block != True):
        valueHistory = calcHistory.get()
        value = calc.get()
        value = replaceSymbol(value)

        # Если последним знаком стоит операция, то она выполняется 
        if value[-1] in '+-/*':
            value = value + value[:-1]

        calcHistory['state'] = NORMAL
        calcHistory.delete(0, END)
        calc['state'] = NORMAL
        calc.delete(0, END)

        try:
            calc.insert(0, eval(value))
            valueHistory += value
            calcHistory.insert(0, valueHistory)
        except (NameError, SyntaxError):
            # messagebox.showinfo('Внимание!',
            #                     'Нужно вводить только цифры! Вы ввели другие символы!')
            valueHistory += value
            calcHistory.insert(0, valueHistory)
            calc['font'] = ('Roboto', 16)
            calc['width'] = 30
            calc.insert(0, 'Нужно вводить только цифры')
            block = True
        except ZeroDivisionError:
            # messagebox.showinfo('Внимание!', 'Деление на ноль невозможно!') # Выводить в самом окне
            valueHistory += value
            calcHistory.insert(0, valueHistory)
            calc['font'] = ('Roboto', 16)
            calc['width'] = 30
            calc.insert(0, 'Деление на ноль невозможно')
            block = True

    calcHistory['state'] = DISABLED
    calc['state'] = DISABLED


# Замена декоративных знаков в строке
def replaceSymbol(value):
    if '–' in value:
        value = value.replace('–', '-')
    elif '×' in value:
        value = value.replace('×', '*')
    elif '÷' in value:
        value = value.replace('÷', '/')
    return value


# Очистка поля ввода
def clear(calc, calcHistory):
    global block
    block= False

    setDefaultSettings(calc)
    calcHistory['state'] = NORMAL
    calcHistory.delete(0, END)
    calcHistory.insert(0, '')
    calcHistory['state'] = DISABLED

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, 0)
    calc['state'] = DISABLED


# Ограничение ввода с клавиатуры. Только цифры и знаки операций
def pressKey(calc, event):

    if event.char.isdigit():
        addDigit(calc, event.char)
    elif event.char in '+-/*':
        addOperation(calc, event.char)
    elif event.char == '\r':
        calculate(calc)

# Установка настроек по-умолчанию
# Необходима после вывода сообщений об ошибках
def setDefaultSettings(calc):
    calc['font'] = ('Roboto', 32)
    calc['width'] = 15


# Выход из приложения
def exitApp(root):
    root.destroy()


def main():

    # Создание переменной, содержащей полный путь до файла
    currentDir = dirname(__file__)
    filePath = join(currentDir, "./Pictures/Calculator icon 9.png")

    root = Tk() # Объявление переменной Tk (окно в котором будем работать)

    width = 364
    height = 449

    # Установка иконки приложения
    photo = PhotoImage(file=filePath)
    root.iconphoto(False, photo)

    root.title("Калькулятор") # Изменение заголовка приложения
    root.config(bg='#222222') # Установить фон
    root.geometry(f"{width}x{height}+100+200") # Установка размеров окна приложения
    root.resizable(False, False) # Блокировка возможности изменения размеров окна

    root.wait_visibility(root)
    root.attributes("-alpha", 0.97) # Делает фон прозрачным

    # root.overrideredirect(True) # Убирает верхнее меню
    # root.attributes("-transparentcolor", "black") # Делает фон совсем прозрачным

    # Создание меню
    mainMenu = Menu(root)

    root.config(menu=mainMenu)

    firstItem = Menu(mainMenu,
                     tearoff=0,
                     bg='#222222',
                     fg='#EEEEEE',
                     activebackground='#333333')

    mainMenu.add_cascade(label='Вид',
                         menu=firstItem)

    firstItem.add_command(label='Обычный') # command
    firstItem.add_command(label='Программист')
    firstItem.add_command(label='Выход',
                          command=lambda : exitApp(root))

    secondItem = Menu(mainMenu,
                      tearoff=0,
                      bg='#222222',
                      fg='#EEEEEE',
                      activebackground='#333333')

    mainMenu.add_cascade(label='Справка', menu=secondItem)
    secondItem.add_command(label='О программе')

    # w = OptionMenu(root, mainMenu, "Обычный", "Программист", "Выход")
    # w.config(bg = "#222222", bd=0)
    # w["menu"].config(bg="#222222", bd=0)
    # w.grid(row=0,
    #        column=0,
    #        columnspan=4,
    #        stick='wens')

    # Создание окна ввода
    calcHistory = Entry(root,
                 bd = 0,
                 disabledbackground='#222222',
                 disabledforeground='#EEEEEE',
                 justify=RIGHT,
                 font=('Roboto', 14),
                 width=15)

    calcHistory.grid(row=1,
              column=0,
              columnspan=4,
              stick='wens',
              padx=1)

    calcHistory['state'] = DISABLED

    calc = Entry(root,
                 bd = 0,
                 disabledbackground='#222222',
                 disabledforeground='#EEEEEE',
                 justify=RIGHT,
                 font=('Roboto', 32), # Arial, Roboto Black, Monserat ExtraBold, Play
                 width=15)

    calc.insert(0, 0)
    calc.grid(row=2,
              column=0,
              columnspan=4,
              stick='wens',
              padx=1)


    calc['state'] = DISABLED

    # Обработка событий
    root.bind('<Key>', lambda event : pressKey(calc, event))

    # Создание кнопок
    makeDigitButton(calc, '1').grid(row=6,
                                    column=0,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '2').grid(row=6,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '3').grid(row=6,
                                    column=2,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '4').grid(row=5,
                                    column=0,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '5').grid(row=5,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '6').grid(row=5,
                                    column=2,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '7').grid(row=4,
                                    column=0,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '8').grid(row=4,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '9').grid(row=4,
                                    column=2,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '0').grid(row=7,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeOperationButton(calc, calcHistory, '±').grid(row=7,
                                                     column=0,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeOperationButton(calc, calcHistory, ',').grid(row=7,
                                                     column=2,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeOperationButton(calc, calcHistory, '÷').grid(row=3,
                                                     column=3,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeOperationButton(calc, calcHistory, '×').grid(row=4,
                                                     column=3,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeOperationButton(calc, calcHistory, '–').grid(row=5,
                                                     column=3,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeOperationButton(calc, calcHistory, '+').grid(row=6,
                                                     column=3,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeCalculateButton(calc, calcHistory, '=').grid(row=7,
                                                     column=3,
                                                     stick='wens',
                                                     padx=1,
                                                     pady=1)

    makeClearButton(calc, calcHistory, 'CE').grid(row=3,
                                                  column=0,
                                                  stick='wens',
                                                  padx=1,
                                                  pady=1)

    makeClearButton(calc, calcHistory, 'C').grid(row=3,
                                                 column=1,
                                                 stick='wens',
                                                 padx=1,
                                                 pady=1)

    makeClearButton(calc, calcHistory, 'Del').grid(row=3,
                                                   column=2,
                                                   stick='wens',
                                                   padx=1,
                                                   pady=1)

    # Установка минимальных размеров кнопок
    root.grid_columnconfigure(0, minsize=50)
    root.grid_columnconfigure(1, minsize=50)
    root.grid_columnconfigure(2, minsize=50)
    root.grid_columnconfigure(3, minsize=50)

    root.grid_rowconfigure(0, minsize=10)
    root.grid_rowconfigure(1, minsize=60)
    root.grid_rowconfigure(2, minsize=60)
    root.grid_rowconfigure(3, minsize=60)
    root.grid_rowconfigure(4, minsize=60)
    root.grid_rowconfigure(5, minsize=60)
    root.grid_rowconfigure(6, minsize=60)
    root.grid_rowconfigure(7, minsize=60)

    root.mainloop()


if __name__ == "__main__":
    main()