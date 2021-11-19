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

# TODO
# СДЕЛАТЬ EXE ФАЙЛ


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
# 28. СДЕЛАТЬ ВЫВОД В ИСТОРИИ 55 + 5 = 60 ТАКОЙ ВОТ
# 29. ПОСЛЕ ЗНАКА ОПЕРАЦИИ НЕЛЬЗЯ ВВОДИТЬ НОЛЬ!
# 30. ПЕРЕД ЗНАКОМ ОПЕРАЦИИ НЕЛЬЗЯ СТАВИТЬ ТОЧКУ
# 31. Если число отрицательно, то можно с помощью Del оставить один МИНУС и будет ошибка

# ОСТАЛОСЬ СДЕЛАТЬ
# 1. Меню (ДОбавить дублирующие кнопки для операций и переводов в системы счисления)
# 2. Выездающий справа журнал/история операций
# 3. Кнопка +/-
# 4. Перевод дробной части числа обратно в десятичную
# 5. Сложение чисел в разных системах счисления
# 6. Блокировка заданной системы счисления
# 7. Ограничить окна Entry 32 символами
# 8. Поработать над дизайном


from tkinter import Tk, Menu, OptionMenu, PhotoImage, Entry, Toplevel
from tkinter import messagebox
from tkinter.constants import RIGHT, END, NORMAL, DISABLED
# from tkinter.ttk import * # Улучшенный tkinter

from os.path import dirname, join

from Buttons import *
from Functions import *
from NumericalSystemFunctions import *


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


    # Создание меню
    mainMenu = Menu(root)

    root.config(menu=mainMenu)

    firstItem = Menu(mainMenu,
                     tearoff=0,
                    #  bg='#222222',
                    #  fg='#EEEEEE',
                    #  activebackground='#333333')
                    )

    mainMenu.add_cascade(label='Вид',
                         menu=firstItem)

    # firstItem.add_command(label='Обычный') # command
    # firstItem.add_command(label='Программист')
    firstItem.add_command(label='Выход',
                          command=lambda : exitApp(root))

    secondItem = Menu(mainMenu,
                      tearoff=0,
                    #   bg='#222222',
                    #   fg='#EEEEEE',
                    #   activebackground='#333333')
                     )

    thirdItem = Menu(secondItem,
                      tearoff=0,
                     )

    fourthItem = Menu(secondItem,
                      tearoff=0,
                     )


    mainMenu.add_cascade(label='Правка', menu=fourthItem)
    fourthItem.add_command(label='Очистить',
                             command=lambda : clearC(calc, calcHistory))


    mainMenu.add_cascade(label='Выполнить', menu=secondItem)
    secondItem.add_command(label='Вычислить',
                             command=lambda : calculate(calc, calcHistory))
    secondItem.add_separator()
    secondItem.add_command(label='Перевести в 2-ю систему счисления',
                             command=lambda : decToBin(calc))
    secondItem.add_command(label='Перевести в 3-ю систему счисления',
                               command=lambda : decToThird(calc))
    secondItem.add_command(label='Перевести в 4-ю систему счисления',
                              command=lambda : decToFour(calc))
    secondItem.add_command(label='Перевести в 5-ю систему счисления',
                               command=lambda : decToFifth(calc))
    secondItem.add_command(label='Перевести в 6-ю систему счисления',
                             command=lambda : decToSix(calc))
    secondItem.add_command(label='Перевести в 7-ю систему счисления',
                               command=lambda : decToSeven(calc))
    secondItem.add_command(label='Перевести в 8-ю систему счисления',
                             command=lambda : decToOct(calc))
    secondItem.add_command(label='Перевести в 9-ю систему счисления',
                              command=lambda : decToNine(calc))
    secondItem.add_command(label='Перевести в 10-ю систему счисления',
                                command=lambda : returnToDec(calc))
    secondItem.add_command(label='Перевести в 16-ю систему счисления',
                             command=lambda : decToHex(calc))




    mainMenu.add_cascade(label='Справка', menu=thirdItem)
    thirdItem.add_command(label='О программе')



    # w = OptionMenu(root, mainMenu, "Обычный", "Программист", "Выход")
    # w.config(bg = "#222222", bd=0)
    # w["menu"].config(bg="#222222", bd=0)
    # w.grid(row=0,
    #        column=0,
    #        columnspan=4,
    #        stick='wens')


    # Обработка событий
    root.bind('<Key>', lambda event : pressKey(calc, calcHistory, event))


    # Создание кнопок
    button1 = makeDigitButton(calc, calcHistory, '1')
    button1.grid(row=7,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button1.bind("<Enter>", lambda event : on_enter_digit(button1, event))
    button1.bind("<Leave>", lambda event : on_leave_digit(button1, event))

    button2 = makeDigitButton(calc, calcHistory, '2')
    button2.grid(row=7,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button2.bind("<Enter>", lambda event : on_enter_digit(button2, event))
    button2.bind("<Leave>", lambda event : on_leave_digit(button2, event))

    button3 = makeDigitButton(calc, calcHistory, '3')
    button3.grid(row=7,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button3.bind("<Enter>", lambda event : on_enter_digit(button3, event))
    button3.bind("<Leave>", lambda event : on_leave_digit(button3, event))

    button4 = makeDigitButton(calc, calcHistory, '4')
    button4.grid(row=6,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button4.bind("<Enter>", lambda event : on_enter_digit(button4, event))
    button4.bind("<Leave>", lambda event : on_leave_digit(button4, event))

    button5 = makeDigitButton(calc, calcHistory, '5')
    button5.grid(row=6,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button5.bind("<Enter>", lambda event : on_enter_digit(button5, event))
    button5.bind("<Leave>", lambda event : on_leave_digit(button5, event))

    button6 = makeDigitButton(calc, calcHistory, '6')
    button6.grid(row=6,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button6.bind("<Enter>", lambda event : on_enter_digit(button6, event))
    button6.bind("<Leave>", lambda event : on_leave_digit(button6, event))

    button7 = makeDigitButton(calc, calcHistory, '7')
    button7.grid(row=5,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button7.bind("<Enter>", lambda event : on_enter_digit(button7, event))
    button7.bind("<Leave>", lambda event : on_leave_digit(button7, event))

    button8 = makeDigitButton(calc, calcHistory, '8')
    button8.grid(row=5,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button8.bind("<Enter>", lambda event : on_enter_digit(button8, event))
    button8.bind("<Leave>", lambda event : on_leave_digit(button8, event))

    button9 = makeDigitButton(calc, calcHistory, '9')
    button9.grid(row=5,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button9.bind("<Enter>", lambda event : on_enter_digit(button9, event))
    button9.bind("<Leave>", lambda event : on_leave_digit(button9, event))

    button0 = makeDigitButton(calc, calcHistory, '0')
    button0.grid(row=8,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button0.bind("<Enter>", lambda event : on_enter_digit(button0, event))
    button0.bind("<Leave>", lambda event : on_leave_digit(button0, event))

    opButton = makeSignButton(calc, '±')
    opButton.grid(row=8,
                  column=0,
                  stick='wens',
                  padx=1,
                  pady=1)
    opButton.bind("<Enter>", lambda event : on_enter_operation(opButton, event))
    opButton.bind("<Leave>", lambda event : on_leave_operation(opButton, event))

    opButton0 = makePointButton(calc, '.')
    opButton0.grid(row=8,
                   column=2,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton0.bind("<Enter>", lambda event : on_enter_operation(opButton0, event))
    opButton0.bind("<Leave>", lambda event : on_leave_operation(opButton0, event))

    opButton8 = makeOperationButton(calc, '÷')
    opButton8.grid(row=4,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton8.bind("<Enter>", lambda event : on_enter_operation(opButton8, event))
    opButton8.bind("<Leave>", lambda event : on_leave_operation(opButton8, event))

    opButton9 = makeOperationButton(calc, '×')
    opButton9.grid(row=5,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton9.bind("<Enter>", lambda event : on_enter_operation(opButton9, event))
    opButton9.bind("<Leave>", lambda event : on_leave_operation(opButton9, event))

    opButton10 = makeOperationButton(calc, '–')
    opButton10.grid(row=6,
                    column=3,
                    stick='wens',
                    padx=1,
                    pady=1)
    opButton10.bind("<Enter>", lambda event : on_enter_operation(opButton10, event))
    opButton10.bind("<Leave>", lambda event : on_leave_operation(opButton10, event))

    opButton11 = makeOperationButton(calc, '+')
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
    button1 = makeDigitButton(calc, calcHistory, '1')
    button1.grid(row=7,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button1.bind("<Enter>", lambda event : on_enter_digit(button1, event))
    button1.bind("<Leave>", lambda event : on_leave_digit(button1, event))

    button2 = makeDigitButton(calc, calcHistory, '2')
    button2.grid(row=7,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button2.bind("<Enter>", lambda event : on_enter_digit(button2, event))
    button2.bind("<Leave>", lambda event : on_leave_digit(button2, event))

    button3 = makeDigitButton(calc, calcHistory, '3')
    button3.grid(row=7,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button3.bind("<Enter>", lambda event : on_enter_digit(button3, event))
    button3.bind("<Leave>", lambda event : on_leave_digit(button3, event))

    button4 = makeDigitButton(calc, calcHistory, '4')
    button4.grid(row=6,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button4.bind("<Enter>", lambda event : on_enter_digit(button4, event))
    button4.bind("<Leave>", lambda event : on_leave_digit(button4, event))

    button5 = makeDigitButton(calc, calcHistory, '5')
    button5.grid(row=6,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button5.bind("<Enter>", lambda event : on_enter_digit(button5, event))
    button5.bind("<Leave>", lambda event : on_leave_digit(button5, event))

    button6 = makeDigitButton(calc, calcHistory, '6')
    button6.grid(row=6,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button6.bind("<Enter>", lambda event : on_enter_digit(button6, event))
    button6.bind("<Leave>", lambda event : on_leave_digit(button6, event))

    button7 = makeDigitButton(calc, calcHistory, '7')
    button7.grid(row=5,
                 column=0,
                 stick='wens',
                 padx=1,
                 pady=1)
    button7.bind("<Enter>", lambda event : on_enter_digit(button7, event))
    button7.bind("<Leave>", lambda event : on_leave_digit(button7, event))

    button8 = makeDigitButton(calc, calcHistory, '8')
    button8.grid(row=5,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button8.bind("<Enter>", lambda event : on_enter_digit(button8, event))
    button8.bind("<Leave>", lambda event : on_leave_digit(button8, event))

    button9 = makeDigitButton(calc, calcHistory, '9')
    button9.grid(row=5,
                 column=2,
                 stick='wens',
                 padx=1,
                 pady=1)
    button9.bind("<Enter>", lambda event : on_enter_digit(button9, event))
    button9.bind("<Leave>", lambda event : on_leave_digit(button9, event))

    button0 = makeDigitButton(calc, calcHistory, '0')
    button0.grid(row=8,
                 column=1,
                 stick='wens',
                 padx=1,
                 pady=1)
    button0.bind("<Enter>", lambda event : on_enter_digit(button0, event))
    button0.bind("<Leave>", lambda event : on_leave_digit(button0, event))

    opButton = makeOperationButton(calc, '±')
    opButton.grid(row=8,
                  column=0,
                  stick='wens',
                  padx=1,
                  pady=1)
    opButton.bind("<Enter>", lambda event : on_enter_operation(opButton, event))
    opButton.bind("<Leave>", lambda event : on_leave_operation(opButton, event))

    opButton0 = makePointButton(calc, '.')
    opButton0.grid(row=8,
                   column=2,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton0.bind("<Enter>", lambda event : on_enter_operation(opButton0, event))
    opButton0.bind("<Leave>", lambda event : on_leave_operation(opButton0, event))

    opButton8 = makeOperationButton(calc, '÷')
    opButton8.grid(row=4,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton8.bind("<Enter>", lambda event : on_enter_operation(opButton8, event))
    opButton8.bind("<Leave>", lambda event : on_leave_operation(opButton8, event))

    opButton9 = makeOperationButton(calc, '×')
    opButton9.grid(row=5,
                   column=3,
                   stick='wens',
                   padx=1,
                   pady=1)
    opButton9.bind("<Enter>", lambda event : on_enter_operation(opButton9, event))
    opButton9.bind("<Leave>", lambda event : on_leave_operation(opButton9, event))

    opButton10 = makeOperationButton(calc, '–')
    opButton10.grid(row=6,
                    column=3,
                    stick='wens',
                    padx=1,
                    pady=1)
    opButton10.bind("<Enter>", lambda event : on_enter_operation(opButton10, event))
    opButton10.bind("<Leave>", lambda event : on_leave_operation(opButton10, event))

    opButton11 = makeOperationButton(calc, '+')
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