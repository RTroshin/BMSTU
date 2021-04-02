# Программа "Sorting algorithms comparison"
# Исследовать временную сложность заданного алгоритма сортировки.
# Требуется составить таблицу в которой указать время работы
# алгоритма в зависимости от размерности массива (3 разных значения)
# и его упорядоченности (по возрастанию, по убыванию, случайным образом).
# Также это сделать для стандартного метода или функции, или библиотечной
# функции.
# Ввести 3 размерности 2 раза (первый раз для самописной сортировки, второй
# раз для встроенной)
#
# Сортировки:
# 1) Сортировка перемешиванием (Шейкерная сортировка)
# 2) Метод sort() (Быстрая сортировка)
#
# TODO
# 1. Сделать массив через numpy


from BubbleSort import *
from CocktailShakerSort import *
import numpy as np
from random import sample
# from time import time
from timeit import default_timer as timer # Данная функция считает время
# точнее чем функия time()

def main():
    arraySizes = inputArray()
    arrayList = arrayCreating(arraySizes)
    timeList = []
    for arr in arrayList:
#         start = time()
        start = timer()
        bubbleSort(arr)
#         end = time()
        end = timer()
        timeList.append(end - start)
    printData("Пузырьковая сортировка", arraySizes, timeList)

    arraySizes = inputArray()
    arrayList = arrayCreating(arraySizes)
    timeList = []
    for arr in arrayList:
        start = timer()
        cocktailShakerSort(arr)
        end = timer()
        timeList.append(end - start)
    printData("Шейкерная сортировка", arraySizes, timeList)

    arraySizes = inputArray()
    arrayList = arrayCreating(arraySizes)
    timeList = []
    for arr in arrayList:
        start = timer()
        np.sort(arr)
        end = timer()
        timeList.append(end - start)
    printData("Метод sort()", arraySizes, timeList)

# Ввод трёх размеров для массивов
def inputArray():
    print()
    while True:
        try:
            arraySizes = list(map(int,\
            input('Введите три размера для массива: ').split()))
            break
        except ValueError:
            print('Некорректный ввод!\nПопробуйте ещё раз')
    return arraySizes

# Создание трёх массивов заданных размерностей в трёх разных состояниях
# (в порядках по возрастанию, по убыванию и случайным образом)
def arrayCreating(arraySizes):
    arrList = []
    for size in arraySizes:
        arr = list(range(size))
        arrList.append(arr)
        arrList.append(arr[::-1])
        arrList.append(sample(arr, size))

        # TODO
        # Так не работает!
        # arr.reverse()
        # arrList.append(arr)
        # r.shuffle(arr)
        # arrList.append(arr)
    return arrList

# Вывод таблицы значений на экран
def printData(sortName, arraySizes, timeList):
    print('┌', '─' * 26, '┬', '─' * 16, '┬', '─' * 59, '┐', sep = '')
    print('│', ' ' * 26, '│', ' ' * 16, '│', ' ' * 22,\
          'Время выполнения', ' ' * 21, '│', sep = '', end='\n')
    print('│      Вид сортировки      │ Размер массива ├', '─' * 19,\
          '┬', '─' * 19, '┬', '─' * 19, '┤', sep = '', end='\n')
    print('│', ' ' * 26, '│', ' ' * 16,\
          '│ Массив упорядочен │ Массив упорядочен │ Массив упорядочен │',\
          sep = '', end='\n')
    print('│', ' ' * 26, '│', ' ' * 16,\
          '│   по возрастанию  │    по убыванию    │ случайным образом │',\
          sep = '', end='\n')
    print('├', '─' * 26, '┼', '─' * 16, '┼', '─' * 19, '┼', '─' * 19,\
          '┼', '─' * 19, '┤', sep = '', end='\n')
    n = 0
    for i in range(len(arraySizes)):
        if i == 1:
            print('│ {:^24} │ {:14d} │ {:17.6f} │ {:17.6f} │ {:17.6f} │'\
            .format(sortName, arraySizes[i], timeList[n],\
                    timeList[n + 1], timeList[n + 2]))
            if i != len(arraySizes) - 1:
                print('│', ' ' * 26, '├', '─' * 16, '┼', '─' * 19,\
                      '┼', '─' * 19, '┼', '─' * 19, '┤', sep = '', end='\n')
            else:
                print('└', '─' * 26, '┴', '─' * 16, '┴', '─' * 19,\
                      '┴', '─' * 19, '┴', '─' * 19, '┘', sep = '', end='\n')
        else:
            print('│ {:^24} │ {:14d} │ {:17.6f} │ {:17.6f} │ {:17.6f} │'\
            .format('', arraySizes[i], timeList[n],\
                    timeList[n + 1], timeList[n + 2]))
            if i != len(arraySizes) - 1:
                print('│', ' ' * 26, '├', '─' * 16, '┼', '─' * 19,\
                      '┼', '─' * 19, '┼', '─' * 19, '┤', sep = '', end='\n')
            else:
                print('└', '─' * 26, '┴', '─' * 16, '┴', '─' * 19,\
                      '┴', '─' * 19, '┴', '─' * 19, '┘', sep = '', end='\n')
        n += 3


if __name__ == "__main__":
    main()