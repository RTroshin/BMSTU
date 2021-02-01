# Программа "Array W"
# Вычислить и разместить в массиве W:
# 1) если fn = 0 → Wn-1
# 2) если fn ≠ 0 → Wn-1 - fn∑cos^2(xk)
# при n ≤ 35 и k ≤ 15
# 
# Первый элемент массива равен 0,5 т.е. W1 = 0,5.
# Наибольшее значение массива W заменить произведением остальных
# нечётных элементов - элементы с нечётными порядковыми номерами
# (1, 3, 5, ...).
# Напечатать значение Wmax, его порядковый номер и массив W.
# 

from math import cos

print()
W = []
f = []
x = []

while True:
    M = int(input('Введите размер M для массива f (M <= 35): '))
    if M > 35:
        print('Вы ввели слишком большое значение!\nПопробуйте ещё раз')
    else:
        break
print('\nВведите значения в массив f:')
number = 1
for n in range(M):
    print('Значение №', number, ': ', end = '')
    userNumber = float(input())
    f.append(userNumber)
    number += 1
print('\nМассив f: ', end = '')
for n in f:
    print('{:.4f}'.format(n), end = ' ')
print()

while True:
    N = int(input('\nВведите размер N для массива x (N <= 15): '))
    if N > 15:
        print('Вы ввели слишком большое значение!\nПопробуйте ещё раз')
    else:
        break
print('\nВведите значения в массив x:')
number = 1
for k in range(N):
    print('Значение №', number, ': ', end = '')
    userNumber = float(input())
    x.append(userNumber)
    number += 1
print('\nМассив x: ', end = '')
for k in x:
    print('{:.4f}'.format(k), end = ' ')
print()

# Вычисление суммы ∑cos^2(xk)

sumx = 0
for k in x:
    sumx += cos(k)**2
print('Сумма ∑cos^2(xk) = {:.4f}'.format(sumx))
print()

# Формирование массива W

W.append(0.5)

for n in range(len(f)):
    if f[n] == 0:
        W.append(W[n - 1])
    else:
        W.append(W[n - 1] - f[n] * sumx)

print('Массив W:', end = ' ')
for n in W:
    print('{:.4f}'.format(n), end = ' ')
print()

# Поиск максимального значения в массивеW и
# замена этого значения произведением элементов
# с нечётными порядковыми номерами

Wmax = W[0]
maxi = 0
multOdd = 1
for i in range(len(W)):
    if Wmax < W[i]:
        Wmax = W[i]
        maxi = i
    if not (i % 2):
        multOdd *= W[i]
print('\nНаибольшее значение массива (Wmax): ', Wmax, '\n\
Порядковый номер (maxi) данного значения: ', maxi)
print('Произведение элементов \
с нечётными порядковыми номерами = {:.4f}'.format(multOdd))
print()

W[maxi] = multOdd
print('Преобразованный массив W:', end = ' ')
for n in W:
    print('{:.4f}'.format(n), end = ' ')
print()