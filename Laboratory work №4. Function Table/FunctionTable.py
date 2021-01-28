# Программа "Function table"
# Условие задания:
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
print('Программа "Function table":')
while True:
    print()
    print('Функции по условию задачи:')
    print('1) z1 = x^3 - 6,5x^2 - 31,3x + 2,32')
    print('2) z2 = x^3 - sin(Pix)')
    print('3) z3 = z1^2 - z2^2')
    print()
    x = x1 = float(input('Введите начальное значение аргумента x \
в диапазоне [-1000...1000]: '))
    while abs(x1) > 1000:
        x = x1 = float(input('Аргумент x должен быть в диапазоне \
[-1000...1000]\nВведите x: '))
    x2 = float(input('Введите конечное значение аргумента x \
в диапазоне [-1000...1000]: '))
    while abs(x2) > 1000:
        x2 = float(input('Аргумент x должен быть в диапазоне \
[-1000...1000]\nВведите x: '))

    if x1 > x2:
        x1, x2 = x2, x1
        x = x1

    step = float(input('Введите значение шага: '))
    while step <= 0:
        step = float(input('Значение шага должно быть положительной величиной!\
\nВведите значение шага: '))

    z1 = minY1 = maxY1 = x1**3 - 6.5 * x1**2 - 31.3 * x1 + 2.32
    z2 = minY2 = maxY2 = x1**3 - sin(pi * x1)
    z3 = minY3 = maxY3 = z1**2 - z2**2

    number = 1

############################## ВЫВОД ТАБЛИЦЫ ##################################

    print()
    print('┌', '─' * 5, '┬', '─' * 12, '┬', '─' * 12, '┬',
'─' * 12, '┬', '─' * 12, '┐', sep = '')
    print('│{:^5s}│ {:^10s} │ {:^10s} │ {:^10s} │ {:^10s} │'\
.format('№', 'Аргумент', 'Ф1', 'Ф2', 'Ф3'))
    print('│',' ' * 42,'│',' ' * 10,'│')
    while x1 <= x2 + 0.05 and number <= 100:

        if minY1 > z1:
            minY1 = z1
        if maxY2 < z2:
            maxY2 = z2

        if number % 2 != 0:
            elem = '│'
        else:
            elem = ' '

        if abs(z1) < 10**5 and abs(z2) < 10**5 and abs(z3) < 10**5:
            print('│{1:^5d}{0} {2: 10.3f} {0} {3: 10.3f} {0} \
{4: 10.3f} │ {5: 10.3f} │'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) > 10**5 and abs(z2) < 10**5 and abs(z3) < 10**5:
            print('│{1:^5d}{0} {2: 10.3f} {0} {3: 10.2e} {0} \
{4: 10.3f} │ {5: 10.3f} │'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) < 10**5 and abs(z2) > 10**5 and abs(z3) < 10**5:
            print('│{1:^5d}{0} {2: 10.3f} {0} {3: 10.3f} {0} \
{4: 10.2e} │ {5: 10.3f} │'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) < 10**5 and abs(z2) < 10**5 and abs(z3) > 10**5:
            print('│{1:^5d}{0} {2: 10.3f} {0} {3: 10.3f} {0} \
{4: 10.3f} │ {5: 10.2e} │'.format(elem, number, x1, z1, z2, z3))
        elif abs(z1) > 10**5 and abs(z2) > 10**5 and abs(z3) > 10**5:
            print('│{1:^5d}{0} {2: 10.3f} {0} {3: 10.2e} {0} \
{4: 10.2e} │ {5: 10.2e} │'.format(elem, number, x1, z1, z2, z3))
        else:
            print('│{1:^5d}{0} {2: 10.3f} {0} {3: 10.2e} {0} \
{4: 10.2e} │ {5: 10.2e} │'.format(elem, number, x1, z1, z2, z3))

        x1 += step
        number += 1

        z1 = x1**3 - 6.5 * x1**2 - 31.3 * x1 + 2.32
        z2 = x1**3 - sin(pi * x1)
        z3 = z1**2 - z2**2

    print('└', '─' * 5, '┴', '─' * 12, '┴', '─' * 12, '┴',
'─' * 12, '┴', '─' * 12, '┘', sep = '')
    print('Минимальное значение функции z1: {: .4g}\n\
Максимальное значение функции z2: {: .4g}\n'.format(minY1, maxY2))