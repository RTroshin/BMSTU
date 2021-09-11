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
# 13.
# 14. При переводе в любую систему счислению отличную от 10-чной, блокировать кнопку +/-
# 15. Доработать поля ввода, чтобы туда не влезало больше 32 символов (смотри калькулятор Windows)
# 16. Уменьшать шрифт, если число становится все больше и больше
# 17. Добавить подсветку кнопок при наведении мыши
# 18. Добавить журнал операций справа, выдвигающийся по кнопке
# 19. Добавить в меню дублирование операций
# 20. Добавить в меню о программе и об авторе
# 21. Добавить смену темной темы на светлую (?)
# 22.
# 23. Исправить маленький значок калькулятора
# 24. Сделать знак ЗАПЯТАЯ ,
# 25. Уменьшить сам калькулятор. Сделать компактнее
# 26. Добавить "Правки" в меню
# 27. ПРИ НАЖАТИИ НА РАВНО В САМОМ НАЧАЛЕ НОЛЬ ЗАПИСЫВАЕТСЯ В ИСТОРИЮ!
# 28. СДЕЛАТЬ ВЫВОД В СТОРИИ 55 + 5 = 60 ТАКОЙ ВОТ
# 29. ПОСЛЕ ЗНАКА ОПЕРАЦИИ НЕЛЬЗЯ ВВОДИТЬ НОЛЬ!
# 30. 

from tkinter import Tk, Menu, OptionMenu, PhotoImage, Entry, Button
from tkinter import messagebox
from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from os.path import dirname, join


block = False # Глобальная переменная


# Создание кнопок с 0 по 9
def makeDigitButton(calc, digit):
    button = Button(bg='#000000',
                      text=digit,
                      font=('Roboto', 16),
                      fg='#EEEEEE',
                      activebackground='#222222',
                      activeforeground="#EEEEEE",
                      command=lambda : addDigit(calc, digit))
    return button


# Создание кнопки с операцией перевода в двоичную систему счисления
def makeNumSystemBinButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : decToBin(calc))
    return button


# Создание кнопок с операциями по переводу системам счисления
def makeNumSystemOctButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : decToOct(calc))
    return button


# Создание кнопок с операциями по переводу системам счисления
def makeNumSystemDecButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : decToDec(calc))
    return button


# Создание кнопок с операциями по переводу системам счисления
def makeNumSystemHexButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : decToHex(calc))
    return button


# Создание кнопок с операциями
def makeOperationButton(calc, calcHistory, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : addOperation(calc, calcHistory, operation))
    return button


# Создание кнопок для взаимодействия с полем ввода
def makeCalculateButton(calc, calcHistory, operation):
    return Button(bg='#04346C',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#1A5090',
                  activeforeground='#EEEEEE',
                  command=lambda : calculate(calc, calcHistory))


# Создание кнопки очистки поля ввода CE
def makeClearButtonCE(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#333333',
                  activeforeground='#EEEEEE',
                  command=lambda : clearCE(calc))
    return button


# Создание кнопки очистки поля ввода C
def makeClearButtonC(calc, calcHistory, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#333333',
                  activeforeground='#EEEEEE',
                  command=lambda : clearC(calc, calcHistory))
    return button


# Создание кнопки очистки поля ввода Del
def makeClearButtonDel(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#333333',
                  activeforeground='#EEEEEE',
                  command=lambda : clearDel(calc))
    return button


# Добавление цифры в поле ввода
def addDigit(calc, digit):
    global block
    if (block != True):
        value = calc.get()

        # Условие для того, чтобы по-умолчанию в меню ввода появлялся ноль
        if value[0] == '0' and len(value) == 1:
            value = value[1:]
        # Условие для того, чтобы в меню ввода нельзя было поставить несколько нолей перед числом
        elif len(value) > 1:
            if value[-2] in '–+÷×' and value[-1] in '0':
                value = value[:-1]

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
        if '+' in value or '-' in value or '/' in value or '*' in value:
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
            valueHistory +=  '  ' + value + '=' + str(eval(value))
            valueHistory = replaceSymbolReturn(valueHistory)
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


# Замена обычных знаков в строке на декоративных
def replaceSymbolReturn(value):
    if '-' in value:
        value = value.replace('-', '–')
    elif '*' in value:
        value = value.replace('*', '×')
    elif '/' in value:
        value = value.replace('/', '÷')
    return value


# Очистка поля ввода по кнопке CE
def clearCE(calc):
    global block
    if (block != True):
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, 0)
        calc['state'] = DISABLED


# Очистка поля ввода по кнопке C
def clearC(calc, calcHistory):
    global block
    block = False

    setDefaultSettings(calc)
    calcHistory['state'] = NORMAL
    calcHistory.delete(0, END)
    calcHistory.insert(0, '')
    calcHistory['state'] = DISABLED

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, 0)
    calc['state'] = DISABLED


# Очистка поля ввода по кнопке Del
def clearDel(calc):
    global block
    if (block != True):
        value = calc.get()
        calc['state'] = NORMAL

        calc.delete(len(value) - 1, END)
        if not len(value) - 1:
            calc.insert(0, 0)

        calc['state'] = DISABLED


# Ограничение ввода с клавиатуры. Только цифры и знаки операций
def pressKey(calc, calcHistory, event):

    print(event.char)
    if event.char.isdigit():
        addDigit(calc, event.char)
    elif event.char in '+-/*':
        addOperation(calc, calcHistory, event.char)
    elif event.char == '\r':
        calculate(calc, calcHistory)
    elif event.char == '\b':
        clearDel(calc)


# Перевод из десятичной в двоичную систему счисления
def decToBin(calc):
    value = float(calc.get())
    valueInt = int(value)
    valueFloat = value - int(value)

    if valueInt == 0:
        return '0'

    result = ''
    while valueInt > 0:
        result = str(valueInt % 2) + result
        valueInt //= 2

    if valueFloat:
        result += '.'
    else:
        result += ''

    iter = 0
    while valueFloat > 1e-5 and iter < 5:
        valueFloat = valueFloat * 2
        number = (int)(valueFloat)
        result += str(number)
        valueFloat -= int(valueFloat)
        iter += 1

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, result)
    calc['state'] = DISABLED


# Перевод из десятичной в восьмеричную систему счисления
def decToOct(calc):
    value = float(calc.get())
    valueInt = int(value)
    valueFloat = value - int(value)

    if valueInt == 0:
        return '0'

    result = ''
    while valueInt > 0:
        result = str(valueInt % 8) + result
        valueInt //= 8

    if valueFloat:
        result += '.'
    else:
        result += ''

    iter = 0
    while valueFloat > 1e-5 and iter < 5:
        valueFloat = valueFloat * 8
        number = (int)(valueFloat)
        result += str(number)
        valueFloat -= int(valueFloat)
        iter += 1

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, result)
    calc['state'] = DISABLED


# Перевод из десятичной в десятичную систему счисления
def decToDec(calc):
    value = int(calc.get())

    if value == 0:
        return '0'

    result = ''
    while value > 0:
        result = str(value % 2) + result
        value //= 2

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, result)
    calc['state'] = DISABLED


# Перевод из десятичной в шестнадцатиричную систему счисления
def decToHex(calc):
    value = float(calc.get())
    valueInt = int(value)
    valueFloat = value - int(value)

    if valueInt == 0:
        return '0'

    result = ''
    while valueInt > 0:
        result = str(digit(valueInt % 16)) + result
        valueInt //= 16

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, result)
    calc['state'] = DISABLED


# Установка настроек по-умолчанию
# Необходима после вывода сообщений об ошибках
def setDefaultSettings(calc):
    calc['font'] = ('Roboto', 32)
    calc['width'] = 15


# Выход из приложения
def exitApp(root):
    root.destroy()

# Для кнопок с цифрами
# Подсвечивает кнопку цветом при наведении мыши
def on_enter_digit(button, event):
    button['background'] = '#111111'

# Возвращает цвет кнопки на цвет по-умолчанию
def on_leave_digit(button, event):
    button['background'] = '#000000'


# Для кнопок с операциями
# Подсвечивает кнопку цветом при наведении мыши
def on_enter_operation(button, event):
    button['background'] = '#333333'

# Возвращает цвет кнопки на цвет по-умолчанию
def on_leave_operation(button, event):
    button['background'] = '#222222'


# Для кнопки calculate
# Подсвечивает кнопку цветом при наведении мыши
def on_enter_calculate(button, event):
    button['background'] = '#0C4487'

# Возвращает цвет кнопки на цвет по-умолчанию
def on_leave_calculate(button, event):
    button['background'] = '#04346C'


def main():

    # Создание переменной, содержащей полный путь до файла
    currentDir = dirname(__file__)
    filePath = join(currentDir, "./Pictures/Calculator icon 9.png")

    root = Tk() # Объявление переменной Tk (окно в котором будем работать)

    width = 364
    height = 496

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
    root.bind('<Key>', lambda event : pressKey(calc, calcHistory, event))

    # Создание кнопок
    button1 = makeDigitButton(calc, '1')
    button1.grid(row=7,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button1.bind("<Enter>", lambda event : on_enter_digit(button1, event))
    button1.bind("<Leave>", lambda event : on_leave_digit(button1, event))

    button2 = makeDigitButton(calc, '2')
    button2.grid(row=7,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button2.bind("<Enter>", lambda event : on_enter_digit(button2, event))
    button2.bind("<Leave>", lambda event : on_leave_digit(button2, event))

    button3 = makeDigitButton(calc, '3')
    button3.grid(row=7,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button3.bind("<Enter>", lambda event : on_enter_digit(button3, event))
    button3.bind("<Leave>", lambda event : on_leave_digit(button3, event))

    button4 = makeDigitButton(calc, '4')
    button4.grid(row=6,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button4.bind("<Enter>", lambda event : on_enter_digit(button4, event))
    button4.bind("<Leave>", lambda event : on_leave_digit(button4, event))

    button5 = makeDigitButton(calc, '5')
    button5.grid(row=6,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button5.bind("<Enter>", lambda event : on_enter_digit(button5, event))
    button5.bind("<Leave>", lambda event : on_leave_digit(button5, event))

    button6 = makeDigitButton(calc, '6')
    button6.grid(row=6,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button6.bind("<Enter>", lambda event : on_enter_digit(button6, event))
    button6.bind("<Leave>", lambda event : on_leave_digit(button6, event))

    button7 = makeDigitButton(calc, '7')
    button7.grid(row=5,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button7.bind("<Enter>", lambda event : on_enter_digit(button7, event))
    button7.bind("<Leave>", lambda event : on_leave_digit(button7, event))

    button8 = makeDigitButton(calc, '8')
    button8.grid(row=5,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button8.bind("<Enter>", lambda event : on_enter_digit(button8, event))
    button8.bind("<Leave>", lambda event : on_leave_digit(button8, event))

    button9 = makeDigitButton(calc, '9')
    button9.grid(row=5,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button9.bind("<Enter>", lambda event : on_enter_digit(button9, event))
    button9.bind("<Leave>", lambda event : on_leave_digit(button9, event))

    button0 = makeDigitButton(calc, '0')
    button0.grid(row=8,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button0.bind("<Enter>", lambda event : on_enter_digit(button0, event))
    button0.bind("<Leave>", lambda event : on_leave_digit(button0, event))

    opButton = makeOperationButton(calc, calcHistory, '±')
    opButton.grid(row=8,
                  column=0,
                  stick='wens',
                  padx=1,
                  pady=1)
    opButton.bind("<Enter>", lambda event : on_enter_operation(opButton, event))
    opButton.bind("<Leave>", lambda event : on_leave_operation(opButton, event))

    opButton0 = makeOperationButton(calc, calcHistory, '.')
    opButton0.grid(row=8,
                   column=2,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton0.bind("<Enter>", lambda event : on_enter_operation(opButton0, event))
    opButton0.bind("<Leave>", lambda event : on_leave_operation(opButton0, event))

    opButton8 = makeOperationButton(calc, calcHistory, '÷')
    opButton8.grid(row=4,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton8.bind("<Enter>", lambda event : on_enter_operation(opButton8, event))
    opButton8.bind("<Leave>", lambda event : on_leave_operation(opButton8, event))

    opButton9 = makeOperationButton(calc, calcHistory, '×')
    opButton9.grid(row=5,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton9.bind("<Enter>", lambda event : on_enter_operation(opButton9, event))
    opButton9.bind("<Leave>", lambda event : on_leave_operation(opButton9, event))

    opButton10 = makeOperationButton(calc, calcHistory, '–')
    opButton10.grid(row=6,
                    column=3,
                    stick='wens',
                    padx=1,
                    pady=1)
    opButton10.bind("<Enter>", lambda event : on_enter_operation(opButton10, event))
    opButton10.bind("<Leave>", lambda event : on_leave_operation(opButton10, event))

    opButton11 = makeOperationButton(calc, calcHistory, '+')
    opButton11.grid(row=7,
                    column=3,
                    stick='wens',
                    padx=1,
                    pady=1)
    opButton11.bind("<Enter>", lambda event : on_enter_operation(opButton11, event))
    opButton11.bind("<Leave>", lambda event : on_leave_operation(opButton11, event))

    opButton12 = makeCalculateButton(calc, calcHistory, '=')
    opButton12.grid(row=8,
                    column=3,
                    stick='wens',
                    padx=1,
                    pady=1)
    opButton12.bind("<Enter>", lambda event : on_enter_calculate(opButton12, event))
    opButton12.bind("<Leave>", lambda event : on_leave_calculate(opButton12, event))

    opButton5 = makeClearButtonCE(calc, 'CE')
    opButton5.grid(row=4,
                   column=0,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton5.bind("<Enter>", lambda event : on_enter_operation(opButton5, event))
    opButton5.bind("<Leave>", lambda event : on_leave_operation(opButton5, event))

    opButton6 = makeClearButtonC(calc, calcHistory, 'C')
    opButton6.grid(row=4,
                   column=1,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton6.bind("<Enter>", lambda event : on_enter_operation(opButton6, event))
    opButton6.bind("<Leave>", lambda event : on_leave_operation(opButton6, event))

    opButton7 = makeClearButtonDel(calc, 'Del')
    opButton7.grid(row=4,
                   column=2,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton7.bind("<Enter>", lambda event : on_enter_operation(opButton7, event))
    opButton7.bind("<Leave>", lambda event : on_leave_operation(opButton7, event))

    opButton1 = makeNumSystemBinButton(calc, 'Bin')
    opButton1.grid(row=3,
                   column=0,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton1.bind("<Enter>", lambda event : on_enter_operation(opButton1, event))
    opButton1.bind("<Leave>", lambda event : on_leave_operation(opButton1, event))

    opButton2 = makeNumSystemOctButton(calc, 'Oct')
    opButton2.grid(row=3,
                   column=1,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton2.bind("<Enter>", lambda event : on_enter_operation(opButton2, event))
    opButton2.bind("<Leave>", lambda event : on_leave_operation(opButton2, event))

    opButton3 = makeNumSystemDecButton(calc, 'Dec')
    opButton3.grid(row=3,
                   column=2,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton3.bind("<Enter>", lambda event : on_enter_operation(opButton3, event))
    opButton3.bind("<Leave>", lambda event : on_leave_operation(opButton3, event))

    opButton4 = makeNumSystemHexButton(calc, 'Hex')
    opButton4.grid(row=3,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton4.bind("<Enter>", lambda event : on_enter_operation(opButton4, event))
    opButton4.bind("<Leave>", lambda event : on_leave_operation(opButton4, event))

    # Установка минимальных размеров кнопок
    root.grid_columnconfigure(0, minsize=50)
    root.grid_columnconfigure(1, minsize=50)
    root.grid_columnconfigure(2, minsize=50)
    root.grid_columnconfigure(3, minsize=50)

    root.grid_rowconfigure(0, minsize=10)
    root.grid_rowconfigure(1, minsize=60)
    root.grid_rowconfigure(2, minsize=60)
    root.grid_rowconfigure(3, minsize=40)
    root.grid_rowconfigure(4, minsize=60)
    root.grid_rowconfigure(5, minsize=60)
    root.grid_rowconfigure(6, minsize=60)
    root.grid_rowconfigure(7, minsize=60)
    root.grid_rowconfigure(8, minsize=60)

    root.mainloop()


if __name__ == "__main__":
    main()