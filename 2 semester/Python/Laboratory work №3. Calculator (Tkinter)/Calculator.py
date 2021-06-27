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
# 11. Реализовать ввод числа в степени e
# 12. 
# 13. 
# 14. 
# 15. 


from tkinter import Tk, Toplevel, Menu, PhotoImage, Entry, Button
from tkinter import messagebox
from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from os.path import dirname, join


# Создание кнопок с 0 по 9
def makeDigitButton(calc, digit):
    return Button(bg='#000000',
                  text=digit,
                  font=('Roboto', 14),
                  fg='#EEEEEE',
                  activebackground='#111111',
                  activeforeground="#EEEEEE",
                  command=lambda : addDigit(calc, digit))


# Создание кнопок с операциями
def makeOperationButton(calc, operation):
    return Button(bg='#222222',
                  text=operation,
                  font=('Roboto', 14),
                  fg='#EEEEEE',
                  activebackground='#333333',
                  activeforeground='#EEEEEE',
                  command=lambda : addOperation(calc, operation))


# Создание кнопок для взаимодействия с полем ввода
def makeCalculateButton(calc, operation):
    return Button(bg='#666666',
                  text=operation,
                  font=('Roboto', 14),
                  fg='#EEEEEE',
                  activebackground='#777777',
                  activeforeground='#EEEEEE',
                  command=lambda : calculate(calc))


# Создание кнопки очистки поля ввода
def makeClearButton(calc, operation):
    return Button(bg='#666666',
                  text=operation,
                  font=('Roboto', 14),
                  fg='#EEEEEE',
                  activebackground='#777777',
                  activeforeground='#EEEEEE',
                  command=lambda : clear(calc))


# Добавление цифры в поле ввода
def addDigit(calc, digit):
    value =calc.get()

    # Условие для того, чтобы по-умолчанию в меню ввода появлялся ноль
    if value[0] == '0' and len(value) == 1:
        value = value[1:]

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value + digit)
    calc['state'] = DISABLED


# Добавление знака операции в поле ввода
def addOperation(calc, operation):
    value =calc.get()

    # Условие для того, чтобы операции отображались как в калькуляторе Windows
    if value[-1] in '-+/*':
        value = value[:-1]
    # Условие для того, чтобы выполнялось предварительное вычисление
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate(calc)
        value = calc.get()

    calc['state'] = NORMAL
    calc.delete(0, END)
    calc.insert(0, value + operation)
    calc['state'] = DISABLED


# Вычисление выражения в поле ввода
def calculate(calc):
    value =calc.get()

    # Если последним знаком стоит операция, то она выполняется 
    if value[-1] in '+-/*':
        value = value + value[:-1]

    calc['state'] = NORMAL
    calc.delete(0, END)

    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание!',
                            'Нужно вводить только цифры! Вы ввели другие символы!')
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание!', 'Деление на ноль недопустимо!')
        calc.insert(0, 0)

    calc['state'] = DISABLED


# Очистка поля ввода
def clear(calc):
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


# Выход из приложения
def exitApp(root):
    root.destroy()


def main():

    # Создание переменной, содержащей полный путь до файла
    currentDir = dirname(__file__)
    filePath = join(currentDir, "./Pictures/Calculator icon 9.png")

    root = Tk() # Объявление переменной Tk (окно в котором будем работать)

    width = 400
    height = 600

    # Установка иконки приложения
    photo = PhotoImage(file=filePath)
    root.iconphoto(False, photo)

    root.title("Калькулятор") # Изменение заголовка приложения
    root.config(bg='#222222') # Установить фон
    root.geometry(f"{width}x{height}+100+200") # Установка размеров окна приложения
    root.resizable(False, False) # Блокировка возможности изменения размеров окна

    # Создание меню
    mainMenu = Menu(root)
    root.config(menu=mainMenu)

    firstItem = Menu(mainMenu,
                     tearoff=0,
                     bg='#222222',
                     fg='#EEEEEE',
                     activebackground='#444444')

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
                      activebackground='#444444')

    mainMenu.add_cascade(label='Справка', menu=secondItem)
    secondItem.add_command(label='О программе')


    # Создание окна ввода
    calc = Entry(root,
                 disabledbackground='#666666',
                 disabledforeground='#EEEEEE',
                 justify=RIGHT,
                 font=('Roboto', 32),
                 width=15)

    calc.grid(row=1,
              column=0,
              columnspan=4,
              stick='we',
              padx=1)

    calc['state'] = DISABLED

    # calc = Entry(root, justify=RIGHT, font=('Arial', 32))
    calc = Entry(root,
                 disabledbackground='#666666',
                 disabledforeground='#EEEEEE',
                 justify=RIGHT,
                 font=('Roboto', 32),
                 width=15)

    # calc = Entry(root, justify=RIGHT, font=('Roboto Black', 32), width=15)
    # calc = Entry(root, justify=RIGHT, font=('Monserat ExtraBold', 32), width=15)
    # calc = Entry(root, justify=RIGHT, font=('Play', 32))
    calc.insert(0, 0)
    calc.grid(row=2,
              column=0,
              columnspan=4,
              stick='we',
              padx=1,
              pady=1)

    calc['state'] = DISABLED

    # Обработка событий
    root.bind('<Key>', lambda event : pressKey(calc, event))

    # Создание кнопок
    makeDigitButton(calc, '1').grid(row=4,
                                    column=0,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '2').grid(row=4,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '3').grid(row=4,
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

    makeDigitButton(calc, '7').grid(row=6,
                                    column=0,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '8').grid(row=6,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '9').grid(row=6,
                                    column=2,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeDigitButton(calc, '0').grid(row=7,
                                    column=0,
                                    stick='wens',
                                    padx=1,
                                    pady=1, columnspan=2)

    makeOperationButton(calc, ',').grid(row=7,
                                        column=2,
                                        stick='wens',
                                        padx=1,
                                        pady=1)

    makeOperationButton(calc, '/').grid(row=3,
                                        column=3,
                                        stick='wens',
                                        padx=1,
                                        pady=1)

    makeOperationButton(calc, '*').grid(row=4,
                                        column=3,
                                        stick='wens',
                                        padx=1,
                                        pady=1)

    makeOperationButton(calc, '-').grid(row=5,
                                        column=3,
                                        stick='wens',
                                        padx=1,
                                        pady=1)

    makeOperationButton(calc, '+').grid(row=6,
                                        column=3,
                                        stick='wens',
                                        padx=1,
                                        pady=1)

    makeCalculateButton(calc, '=').grid(row=7,
                                        column=3,
                                        stick='wens',
                                        padx=1,
                                        pady=1)

    makeClearButton(calc, 'CE').grid(row=3,
                                     column=0,
                                     stick='wens',
                                     padx=1,
                                     pady=1)

    makeClearButton(calc, 'C').grid(row=3,
                                    column=1,
                                    stick='wens',
                                    padx=1,
                                    pady=1)

    makeClearButton(calc, '<=').grid(row=3,
                                     column=2,
                                     stick='wens',
                                     padx=1,
                                     pady=1)

    # Установка минимальных размеров кнопок
    root.grid_columnconfigure(0, minsize=100)
    root.grid_columnconfigure(1, minsize=100)
    root.grid_columnconfigure(2, minsize=100)
    root.grid_columnconfigure(3, minsize=100)

    root.grid_rowconfigure(0, minsize=40)
    root.grid_rowconfigure(1, minsize=80)
    root.grid_rowconfigure(2, minsize=80)
    root.grid_rowconfigure(3, minsize=80)
    root.grid_rowconfigure(4, minsize=80)
    root.grid_rowconfigure(5, minsize=80)
    root.grid_rowconfigure(6, minsize=80)
    root.grid_rowconfigure(7, minsize=80)

    root.mainloop()


if __name__ == "__main__":
    main()