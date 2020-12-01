# z1 = x^3 - 6,5x^2 - 31,3x + 2,32
# z2 = x^3 - sin(Pix)
# z3 = z1^2 - z2^2
#
# x = 0 (0,05) 1
#
# Оператор "while"
# Определить минимальное значение z1 и максимальное z2
#

from math import pi, sin

print()
while True:
    x1 = float(input('Введите начальное значение аргумента x\
в диапазоне (-1000...1000): '))
    while abs(x1) > 1000:
        x1 = float(input('Аргумент x должен быть в диапазоне\
 (-1000...1000)\nВведите x: '))
    x2 = float(input('Введите конечное значение аргумента x\
 в диапазоне (-1000...1000): '))
    while (abs(x2) > 1000) or (x2 <= x1):
        if x2 < x1:
            x2 = float(input('Аргумент x должен быть меньше\
 x1\nВведите x: '))
        else:
            x2 = float(input('Аргумент x должен быть в диапазоне\
 (-1000...1000)\nВведите x: '))
    minZ1 = x1
    maxZ2 = x1

    z1 = x1**3 - 6.5 * x1**2 - 31.3 * x1 + 2.32
    z2 = x1**3 - sin(pi * x1)
    z3 = z1**2 - z2**2

    step = 0.05
    number = 1

    print('─' * 58)
    print('{:^5s}| {:^10s} | {:^10s} | {:^10s} | {:^10s} |'\
    .format('№', 'Аргумент', 'Ф1', 'Ф2', 'Ф3'))
    # print(' ' * 43, '|',' ' * 10, '| ')
    print(' ' * 6,' ' * 36,'│',' ' * 10,'│ ')
    while x1 <= x2 and number <= 100:
        z1 = x1**3 - 6.5 * x1**2 - 31.3 * x1 + 2.32
        z2 = x1**3 - sin(pi * x1)
        z3 = z1**2 - z2**2

        if minZ1 > z1:
            minZ1 = z1
        if maxZ2 < z2:
            maxZ2 = z2

        if number % 2 != 0:
            elem = '|'
        else:
            elem = ' '
        if z1 > 10 and z2 > 10 and z3 > 10:
            print('{1:^5d}{0} {2: 10.4f} {0} {3: 10.4f} {0}\
 {4: 10.4f} | {5: 10.4f} |'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) > 10 and abs(z2) < 10 and abs(z3) < 10:
            print('{1:^5d}{0} {2: 10.4f} {0} {3: 10.2e} {0}\
 {4: 10.4f} | {5: 10.4f} |'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) < 10 and abs(z2) > 10 and abs(z3) < 10:
            print('{1:^5d}{0} {2: 10.4f} {0} {3: 10.4f} {0}\
 {4: 10.2e} | {5: 10.4f} |'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) < 10 and abs(z2) < 10 and abs(z3) > 10:
            print('{1:^5d}{0} {2: 10.4f} {0} {3: 10.4f} {0}\
 {4: 10.4f} | {5: 10.2e} |'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) > 10 and abs(z2) > 10 and abs(z3) > 10:
            print('{1:^5d}{0} {2: 10.4f} {0} {3: 10.2e} {0}\
 {4: 10.2e} | {5: 10.2e} |'.format(elem, number, x1, z1, z2, z3))
        x1 += step
        number += 1
    print('─' * 58,'\n')
    print('Минимальное значение функции z1: {: .4g}\n\
Максимальное значение функции z2: {: .4g}\n'.format(minZ1, maxZ2))