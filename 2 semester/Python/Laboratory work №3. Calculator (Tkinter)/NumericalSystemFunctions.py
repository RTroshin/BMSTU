from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from Calculator import *
from Functions import *
from Buttons import *


BLOCK = False # Глобальная переменная
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
def returnToDec(calc):
    value = float(calc.get())
    valueInt = int(value)
    valueFloat = value - int(value)

    if valueInt == 0:
        return '0'

    resultInt = 0
    i = 0
    while valueInt > 0:
        resultInt += pow(2 * valueInt % 10, i)
        valueInt = int(valueInt / 10)
        i += 1

    resultInt = str(resultInt)
    if valueFloat:
        resultInt += '.'
    # else:
    #     result += ''

    # resultFloat = 0
    # valueFloat = str(valueFloat)
    # print("valueFloat = ", valueFloat)
    # j = 1
    # for i in range(len(valueFloat)):
    #     print("valueFloat[i] = ", valueFloat[i])
    #     if i > 1:
    #         resultFloat +=  int(valueFloat[i]) * pow(2, -j)
    #         print("resultFloat = ", resultFloat)
    #         print("j = ", j)
    #         j += 1
        
    # resultFloat = float('0.' + str(resultFloat))

    # resultFloat = 0
    # print(valueFloat)
    # valueFloat *= 1e+5
    # valueFloat = int(valueFloat)
    # print(valueFloat)
    # i = len(str(valueFloat))
    # while valueFloat > 0:
    #     resultFloat += pow(2 * valueFloat % 10, -i)
    #     valueFloat = int(valueFloat / 10)
    #     i -= 1

    # print(resultFloat)

    calc['state'] = NORMAL
    calc.delete(0, END)
    # calc.insert(0, str(float(resultInt) + resultFloat))
    calc.insert(0, str(resultInt))
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

    if valueFloat:
        result += '.'
    else:
        result += ''

    iter = 0
    while valueFloat > 1e-5 and iter < 5:
        valueFloat = valueFloat * 16
        number = (int)(valueFloat)
        result += str(digit(number))
        valueFloat -= int(valueFloat)
        iter += 1

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, result)
    calc['state'] = DISABLED


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