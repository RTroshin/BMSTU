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
# 2. Сделать итоговые данные (самое быстрое время и самое медленное)


from BubbleSort import *
from CocktailShakerSort import *
import numpy as np
from random import sample
# from time import time
from timeit import default_timer as timer # Данная функция считает время
# точнее чем функия time()

def main():
    sortNames = ["Пузырьковая сортировка",\
                 "Шейкерная сортировка",\
                 "Быстрая сортировка (numpy)",\
                 "Cортировка слиянием (numpy)",\
                 "Сортировка кучей (numpy)"]
    lenSortNames = len(sortNames)
    arraySizes = list()
    timeList = list()

    for i in range(lenSortNames):
        arraySizes.append(inputArray(sortNames[i]))
        arrayList = arrayCreating(arraySizes[i])
        times = []
        for arr in arrayList:
            if i == 0:
        #         start = time()
                start = timer()
                bubbleSort(arr)
        #         end = time()
                end = timer()
            elif i == 1:
                start = timer()
                cocktailShakerSort(arr)
                end = timer()
            elif i == 2:
                start = timer()
                np.sort(arr) # Быстрая сортировка (quicksort) по-умолчанию
                end = timer()
            elif i == 3:
                start = timer()
                np.sort(arr, kind="mergesort")
                end = timer()
            elif i == 4:
                start = timer()
                np.sort(arr, kind="heapsort")
                end = timer()
            times.append(end - start)
        timeList.append(times)

    for i in range(lenSortNames):
        printData(i, sortNames, arraySizes[i], timeList[i])

# Ввод трёх размеров для массивов
def inputArray(sortName):
    print('\n', sortName, sep = '', end='\n')
    while True:
        try:
            arraySizes = list(map(int,\
            input('Введите три размера для массива: ').split()))
            if len(arraySizes) != 3:
                print('Некорректный ввод!\nПопробуйте ещё раз')
            else:
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
def printData(i, sortNames, arraySizes, timeList):
    if i == 0:
        print()
        print('┌', '─' * 29, '┬', '─' * 16, '┬', '─' * 59, '┐', sep = '')
        print('│', ' ' * 29, '│', ' ' * 16, '│', ' ' * 19,\
              'Время выполнения, сек.', ' ' * 18, '│', sep = '', end='\n')
        print('│       Вид сортировки        │ Размер массива ├', '─' * 19,\
            '┬', '─' * 19, '┬', '─' * 19, '┤', sep = '', end='\n')
        print('│', ' ' * 29, '│', ' ' * 16,\
            '│ Массив упорядочен │ Массив упорядочен │ Массив упорядочен │',\
            sep = '', end='\n')
        print('│', ' ' * 29, '│', ' ' * 16,\
            '│   по возрастанию  │    по убыванию    │ случайным образом │',\
            sep = '', end='\n')
        print('├', '─' * 29, '┼', '─' * 16, '┼', '─' * 19, '┼', '─' * 19,\
            '┼', '─' * 19, '┤', sep = '', end='\n')
    n = 0
    for j in range(len(arraySizes)):
        if j == 1:
            print('│ {:^27} │ {:14d} │ {:17.6f} │ {:17.6f} │ {:17.6f} │'\
            .format(sortNames[i], arraySizes[j], timeList[n],\
                    timeList[n + 1], timeList[n + 2]))
            if j != len(arraySizes) - 1:
                print('│', ' ' * 29, '├', '─' * 16, '┼', '─' * 19,\
                      '┼', '─' * 19, '┼', '─' * 19, '┤', sep = '', end='\n')
        else:
            print('│ {:^27} │ {:14d} │ {:17.6f} │ {:17.6f} │ {:17.6f} │'\
            .format('', arraySizes[j], timeList[n],\
                    timeList[n + 1], timeList[n + 2]))
            if j != len(arraySizes) - 1:
                print('│', ' ' * 29, '├', '─' * 16, '┼', '─' * 19,\
                      '┼', '─' * 19, '┼', '─' * 19, '┤', sep = '', end='\n')
            elif i == len(sortNames) - 1:
                print('└', '─' * 29, '┴', '─' * 16, '┴', '─' * 19,\
                      '┴', '─' * 19, '┴', '─' * 19, '┘', sep = '', end='\n')
            elif j == len(arraySizes) - 1:
                print('├', '─' * 29, '┴', '─' * 16, '┴', '─' * 19,\
                      '┴', '─' * 19, '┴', '─' * 19, '┤', sep = '', end='\n')
                print('├', '─' * 29, '┬', '─' * 16, '┬', '─' * 19,\
                      '┬', '─' * 19, '┬', '─' * 19, '┤', sep = '', end='\n')
        n += 3


if __name__ == "__main__":
    main()