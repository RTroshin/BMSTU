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


from tkinter import Tk, PhotoImage, Entry, Button
from tkinter import messagebox
from tkinter.constants import RIGHT, END, NORMAL, DISABLED

from os.path import dirname, join


def addDigit(calculate, digit):
    value =calculate.get() + str(digit)
    calculate.delete(0, END)
    calculate.insert(0, value)


def main():

    # Создание переменной, содержащей полный путь до файла
    currentDir = dirname(__file__)
    filePath = join(currentDir, "./Pictures/Calculator icon 9.png")

    root = Tk() # Объявление переменной Tk (окно в котором будем работать)

    width = 450
    height = 600

    # Установка иконки приложения
    photo = PhotoImage(file=filePath)
    root.iconphoto(False, photo)

    root.title("Калькулятор") # Изменение заголовка приложения
    root.config(bg='#222222') # Установить фон
    root.geometry(f"{width}x{height}+100+200") # Установка размеров окна приложения
    root.resizable(False, False) # Блокировка возможности изменения размеров окна

    # Создание окна ввода
    # calculate = Entry(root, justify=RIGHT, font=('Arial', 32))
    calculate = Entry(root, justify=RIGHT, font=('Roboto', 32), width=15)
    # calculate = Entry(root, justify=RIGHT, font=('Roboto Black', 32), width=15)
    # calculate = Entry(root, justify=RIGHT, font=('Monserat ExtraBold', 32), width=15)
    # calculate = Entry(root, justify=RIGHT, font=('Play', 32))
    calculate.grid(row=0, column=0, columnspan=4, stick='we')

    # Создание кнопок
    Button(text='1', font=('Roboto', 14), command=lambda : addDigit(calculate, 1)).grid(row=2, column=0, stick='wens', padx=1, pady=1)
    Button(text='2', font=('Roboto', 14), command=lambda : addDigit(calculate, 2)).grid(row=2, column=1, stick='wens', padx=1, pady=1)
    Button(text='3', font=('Roboto', 14), command=lambda : addDigit(calculate, 3)).grid(row=2, column=2, stick='wens', padx=1, pady=1)
    Button(text='4', font=('Roboto', 14), command=lambda : addDigit(calculate, 4)).grid(row=3, column=0, stick='wens', padx=1, pady=1)
    Button(text='5', font=('Roboto', 14), command=lambda : addDigit(calculate, 5)).grid(row=3, column=1, stick='wens', padx=1, pady=1)
    Button(text='6', font=('Roboto', 14), command=lambda : addDigit(calculate, 6)).grid(row=3, column=2, stick='wens', padx=1, pady=1)
    Button(text='7', font=('Roboto', 14), command=lambda : addDigit(calculate, 7)).grid(row=4, column=0, stick='wens', padx=1, pady=1)
    Button(text='8', font=('Roboto', 14), command=lambda : addDigit(calculate, 8)).grid(row=4, column=1, stick='wens', padx=1, pady=1)
    Button(text='9', font=('Roboto', 14), command=lambda : addDigit(calculate, 9)).grid(row=4, column=2, stick='wens', padx=1, pady=1)
    Button(text='0', font=('Roboto', 14), command=lambda : addDigit(calculate, 0)).grid(row=5, column=0, stick='wens', padx=1, pady=1, columnspan=2)

    # Button(text='CE', command= ).grid(row=1, column=0, stick='wens', padx=1, pady=1)
    # Button(text='C', command= ).grid(row=1, column=1, stick='wens', padx=1, pady=1)
    # Button(text='<=', command= ).grid(row=1, column=2, stick='wens', padx=1, pady=1)

    # Button(text=',', command= ).grid(row=5, column=2, stick='wens', padx=1, pady=1)
    # Button(text='/', command= ).grid(row=1, column=3, stick='wens', padx=1, pady=1)
    # Button(text='X', command= ).grid(row=2, column=3, stick='wens', padx=1, pady=1)
    # Button(text='-', command= ).grid(row=3, column=3, stick='wens', padx=1, pady=1)
    # Button(text='+', command= ).grid(row=4, column=3, stick='wens', padx=1, pady=1)
    # Button(text='=', command= ).grid(row=5, column=3, stick='wens', padx=1, pady=1)

    # Установка минимальных размеров кнопок
    root.grid_columnconfigure(0, minsize=100)
    root.grid_columnconfigure(1, minsize=100)
    root.grid_columnconfigure(2, minsize=100)
    root.grid_columnconfigure(3, minsize=100)

    root.grid_rowconfigure(1, minsize=80)
    root.grid_rowconfigure(2, minsize=80)
    root.grid_rowconfigure(3, minsize=80)
    root.grid_rowconfigure(4, minsize=80)
    root.grid_rowconfigure(5, minsize=80)

    root.mainloop()


if __name__ == "__main__":
    main()