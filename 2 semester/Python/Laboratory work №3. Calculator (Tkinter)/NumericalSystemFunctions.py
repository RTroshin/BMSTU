from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from Calculator import *
from Functions import *
from Buttons import *

# Глобальные переменные
BLOCK = False
SYSNUMBER = 10

# Перевод из десятичной в двоичную систему счисления
def decToBin(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 2
        else:
            returnToDec(calc)
            SYSNUMBER = 2
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 2
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в троичную систему счисления
def decToThird(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 3
        else:
            returnToDec(calc)
            SYSNUMBER = 3
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 3
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в четверичную систему счисления
def decToFour(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 4
        else:
            returnToDec(calc)
            SYSNUMBER = 4
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 4
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в пятеричную систему счисления
def decToFifth(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 5
        else:
            returnToDec(calc)
            SYSNUMBER = 5
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 5
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в шестеричную систему счисления
def decToSix(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 6
        else:
            returnToDec(calc)
            SYSNUMBER = 6
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 6
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в семеричную систему счисления
def decToSeven(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 7
        else:
            returnToDec(calc)
            SYSNUMBER = 7
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 7
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в восьмеричную систему счисления
def decToOct(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 8
        else:
            returnToDec(calc)
            SYSNUMBER = 8
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 8
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в девятеричную систему счисления
def decToNine(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 9
        else:
            returnToDec(calc)
            SYSNUMBER = 9
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(valueInt % SYSNUMBER) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(number)
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 9
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Перевод из десятичной в десятичную систему счисления
def returnToDec(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            return '0'
        value = calc.get()
        if value == 'Деление на ноль невозможно':
            return '0'

        if value == '0':
            return '0'

        if '.' in value:
            valueInt, valueFloat = map(str, value.split('.'))
        else:
            valueInt = value
            valueFloat = '0'

        resultInt = 0
        iter = len(valueInt) - 1
        for digit in valueInt:
            resultInt += int(digitReturn(digit)) * pow(SYSNUMBER, iter)
            iter -= 1

        resultFloat = 0
        iter = 1
        for digit in valueFloat:
            if digit != '0':
                resultFloat += int(digitReturn(digit)) * pow(SYSNUMBER, -iter)
            iter += 1

        SYSNUMBER = 10
        calc['state'] = NORMAL
        calc.delete(0, END)
        if resultFloat:
            calc.insert(0, str(float(resultInt) + resultFloat))
        else:
            calc.insert(0, str(resultInt))
        calc['state'] = DISABLED

# Перевод из десятичной в шестнадцатиричную систему счисления
def decToHex(calc):
    global BLOCK
    global SYSNUMBER
    if (BLOCK != True):
        if SYSNUMBER == 10:
            SYSNUMBER = 16
        else:
            returnToDec(calc)
            SYSNUMBER = 16
        try:
            value = float(calc.get())
        except ValueError:
            return '0'
        valueInt = int(value)
        valueFloat = value - int(value)

        if valueInt == 0:
            return '0'

        result = ''
        while valueInt > 0:
            result = str(digit(valueInt % SYSNUMBER)) + result
            valueInt //= SYSNUMBER

        if valueFloat:
            result += '.'
        else:
            result += ''

        iter = 0
        while valueFloat > 1e-5 and iter < 5:
            valueFloat = valueFloat * SYSNUMBER
            number = (int)(valueFloat)
            result += str(digit(number))
            valueFloat -= int(valueFloat)
            iter += 1

        SYSNUMBER = 16
        calc['state'] = NORMAL
        calc.delete(0, END)
        calc.insert(0, result)
        calc['state'] = DISABLED

# Возвращает в переменную номер системы счисления
def returnNumericalSystemNumber():
    if SYSNUMBER == 2:
        return 2
    elif SYSNUMBER == 3:
        return 3
    elif SYSNUMBER == 4:
        return 5
    elif SYSNUMBER == 5:
        return 5
    elif SYSNUMBER == 6:
        return 6
    elif SYSNUMBER == 7:
        return 7
    elif SYSNUMBER == 8:
        return 8
    elif SYSNUMBER == 9:
        return 9
    elif SYSNUMBER == 10:
        return 10
    elif SYSNUMBER == 11:
        return 11
    elif SYSNUMBER == 12:
        return 12
    elif SYSNUMBER == 13:
        return 13
    elif SYSNUMBER == 14:
        return 14
    elif SYSNUMBER == 15:
        return 15
    elif SYSNUMBER == 16:
        return 16

# Преобразование десятичных чисел в шестнадцатиричные
def digit(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'

# Преобразование шестнадцатиричных чисел в десятичные
def digitReturn(num):
    if num == '0':
        return '0'
    elif num == '1':
        return '1'
    elif num == '2':
        return '2'
    elif num == '3':
        return '3'
    elif num == '4':
        return '4'
    elif num == '5':
        return '5'
    elif num == '6':
        return '6'
    elif num == '7':
        return '7'
    elif num == '8':
        return '8'
    elif num == '9':
        return '9'
    elif num == 'A':
        return '10'
    elif num == 'B':
        return '11'
    elif num == 'C':
        return '12'
    elif num == 'D':
        return '13'
    elif num == 'E':
        return '14'
    elif num == 'F':
        return '15'