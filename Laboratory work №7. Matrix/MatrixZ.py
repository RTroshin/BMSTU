# Программа "Matrix Z"
# В матрицe Z(10x12) найти произведение положительных элементов каждой
# строки. Строку с максимальным значением произведения поменять местами с
# последней строкой. Затем вычеркнуть строку с минимальным произведением
# элементов. Напечатать исходную и сформированную матрицы в виде матриц.
# Примечание. Дополнительных массивов не использовать. Получаемый после
# вычеркивания массив расположить на месте старого.
#

from random import randint

N = 10
M = 12
Z = [[0] * M for i in range(N)]

# Заполнение матрицы случайными значениями
print()
for i in range(N):
    rowMult = 1
    for j in range(M):
        Z[i][j] = randint(-9, 9)
        while Z[i][j] == 0:
            Z[i][j] = randint(-9, 9)

# Вычисление произведений элементов в каждой строке
# Поиск максимального произведения
print('Исходная матрица:\n')

maxi = mini = 0
maxMult = 0
for i in range(N):
    rowMult = 1
    for j in range(M):
        print('{:4}'.format(Z[i][j]), end = '')
        if Z[i][j] > 0:
            rowMult *= Z[i][j]
    if maxMult < rowMult:
        maxMult = rowMult
        maxi = i
    print('    # ∏(row) = ', rowMult)
    print()

print('* ∏(row) - произведение положительных элементов в строке\n')

print('Максимальное произведение = ', maxMult,\
      '\nНомер строки = ', maxi + 1, end = '\n')

# Поиск минимального произведения
minMult = maxMult
for i in range(N):
    rowMult = 1
    for j in range(M):
        if Z[i][j] > 0:
            rowMult *= Z[i][j]
    if minMult > rowMult:
        minMult = rowMult
        mini = i

print('Минимальное произведение = ', minMult,\
      '\nНомер строки = ', mini + 1, end = '\n')
print()

# Преобразование матрицы
print('Преобразованная матрица:\n')

for j in range(M):
    Z[maxi][j] = Z[9][j]

for i in range(N):
    if i != mini:
        for j in range(M):
            print('{:4}'.format(Z[i][j]), end = '')
        if i == maxi:
            print('    # Заменённая строка')
        else:
            print()
        print()
print()
for i in range(N):
    if i == mini:
        for j in range(M):
            print('{:4}'.format(Z[i][j]), end = '')
        print('    # Удалённая строка')
        print()