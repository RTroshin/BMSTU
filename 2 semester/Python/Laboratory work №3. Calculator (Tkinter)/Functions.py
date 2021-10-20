from tkinter import messagebox
from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from Calculator import *
from Buttons import *


block = False # Глобальная переменная


# Добавление цифры в поле ввода
def addDigit(calc, calcHistory, digit):
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

        # Условие для того, чтобы выполнялось предварительное вычисление
        if len(value) > 1:
            if value[-1] in '–+÷×':
                addHistory(value, calcHistory)
                value = ''
                exit

        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + digit)
        calc['state'] = DISABLED


# Добавление знака операции в поле ввода
def addOperation(calc, operation):
    global block
    if (block != True):
        value = calc.get()
        value = replaceSymbol(value)

        # Условие для того, чтобы операции отображались как в калькуляторе Windows
        if value[-1] in '-+/*':
            value = value[:-1]

        # Условия для того, чтобы после точки ставился ноль, если перед ней знак стоит операции
        if value[-1] == '.':
            value = value[:-1]

        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + operation)
        calc['state'] = DISABLED


# Отделение дробной части точкой!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def addPoint(calc, operation):
    global block
    if (block != True):
        value = calc.get()

        # Условия для того, чтобы нельзя было ввести несколько точек
        if value[-1] == '.':
            value = value[:-1]

        # Условия для того, чтобы в одном числе было не более одной точки!!!!!!!!!!!!!!!!!!!!!!!!
        if '.' in value:
            operation = ''

        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, value + operation)
        calc['state'] = DISABLED


# Добавление значения в историю
def addHistory(value, calcHistory):
    valueHistory = calcHistory.get()

    calcHistory['state'] = NORMAL
    calcHistory.delete(0, END)

    valueHistory = replaceSymbolReturn(valueHistory)
    valueHistory += value
    calcHistory.insert(0, valueHistory)

    calcHistory['state'] = DISABLED

# Вычисление выражения в поле ввода
def calculate(calc, calcHistory):
    global block
    if (block != True):
        valueHistory = calcHistory.get()
        value = calc.get()

        # Если последним знаком стоит операция, то она выполняется 
        if value[-1] in '+-/*':
            value = value + value[:-1]

        calcHistory['state'] = NORMAL
        calc['state'] = NORMAL
        calcHistory.delete(0, END)
        calc.delete(0, END)

        try:
            if valueHistory:
                valueHistory = replaceSymbol(valueHistory)
                value = replaceSymbol(value)

                calc.insert(0, eval(valueHistory + value))

                valueHistory = replaceSymbolReturn(valueHistory)
                value = replaceSymbolReturn(value)

                calcHistory.delete(0, END)
            else:
                calc.insert(0, eval(value))
        except (NameError, SyntaxError):
            # messagebox.showinfo('Внимание!',
            #                     'Нужно вводить только цифры! Вы ввели другие символы!')
            valueHistory = replaceSymbolReturn(valueHistory)
            value = replaceSymbolReturn(value)

            calcHistory.insert(0, valueHistory + value)
            calc['font'] = ('Roboto', 16)
            calc['width'] = 30
            calc.insert(0, 'Нужно вводить только цифры')
            block = True
        except ZeroDivisionError:
            # messagebox.showinfo('Внимание!', 'Деление на ноль невозможно!') # Выводить в самом окне
            valueHistory = replaceSymbolReturn(valueHistory)
            value = replaceSymbolReturn(value)

            calcHistory.insert(0, valueHistory + value)
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
    if '×' in value:
        value = value.replace('×', '*')
    if '÷' in value:
        value = value.replace('÷', '/')
    return value


# Замена обычных знаков в строке на декоративных
def replaceSymbolReturn(value):
    if '-' in value:
        value = value.replace('-', '–')
    if '*' in value:
        value = value.replace('*', '×')
    if '/' in value:
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


# Установка настроек по-умолчанию
# Необходима после вывода сообщений об ошибках
def setDefaultSettings(calc):
    calc['font'] = ('Roboto', 32)
    calc['width'] = 15


# Выход из приложения
def exitApp(root):
    root.destroy()