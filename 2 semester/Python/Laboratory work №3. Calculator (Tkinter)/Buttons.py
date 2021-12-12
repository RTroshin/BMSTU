from tkinter import Button

from Calculator import *


# Создание кнопок с 0 по 9
def makeDigitButton(calc, calcHistory, digit):
    button = Button(bg='#000000',
                      text=digit,
                      font=('Roboto', 16),
                      fg='#EEEEEE',
                      activebackground='#222222',
                      activeforeground="#EEEEEE",
                      command=lambda : addDigit(calc, calcHistory, digit))
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
                  command=lambda : returnToDec(calc))
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
def makeOperationButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : addOperation(calc, operation))
    return button


# Создание кнопки с операцией смены знака
def makeSignButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : changeSign(calc))
    return button


# Создание кнопок с операциями
def makePointButton(calc, operation):
    button =  Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 16),
                  fg='#EEEEEE',
                  activebackground='#444444',
                  activeforeground='#EEEEEE',
                  command=lambda : addPoint(calc, operation))
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