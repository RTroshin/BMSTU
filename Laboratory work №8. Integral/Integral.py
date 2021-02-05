# Программа "Integral"
# Сравнить два метода (метод левых прямоугольников и метод Симпсона)
# для вычисления определённого интеграла.
# Для метода с наименьшей точностью задать степень точности ε и
# выяснить количество N (количество подынтервалов), обеспечивающих
# установленную точность для вычисления интеграла
#

from math import exp, sin, cos

def function(x):
    f = (-2) * exp(x) * sin(x)
    return f

def primFunction(x):
    F = exp(x) * (cos(x) - sin(x))
    return F

def exValueIntegral(a, b):
    z0 = primFunction(b) - primFunction(a)
    return z0

def leftRectRule(a, b, N):
    z = 0
    dx = (b - a) / N
    x = a + dx / 2
    for i in range(N):
        if z > 10**5:
            break
        z += function(x)
        x += dx
    return z * dx

def SimpsonRule(a, b, N):
    dx = (b - a) / N
    dx2 = dx / 2
    x = a + dx
    z = (function(a) + function(b)) / 2 + 2 * function(x - dx2)
    for i in range(1, N):
        if z > 10**5:
            break
        z += function(x) + 2 * function(x - dx2)
        x += dx
    return z * dx / 3

def output(values):
    print('Таблица точных значений z')
    print('┌', '─' * 29, '┬', '─' * 13, '┬', '─' * 13, '┐', sep = '')
    print('│       Название метода       │   N1 = {0:^3d}  │   N2 = {1:^3d}  │'\
    .format(values[0], values[3]))
    print('├', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
    print('│ Метод левых прямоугольников │ {:11.3f} │ {:11.3f} │'\
    .format(values[1], values[4]))
    print('├', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
    print('│ Метод Симпсона              │ {:11.3f} │ {:11.3f} │'\
    .format(values[2], values[5]))
    print('└', '─' * 29, '┴', '─' * 13, '┴', '─' * 13, '┘', sep = '')
    print()

values = []
while True:
    end = 0
    while True:
        print()
        if end == 2:
            break

        if end == 0:
            a, b = map(int, input('Введите пределы интегрирования a и b: ')\
            .split())
            N = N1 = int(input('Введите количество подынтервалов N1: '))
            values.append(N1)
        else:
            N = N2 = int(input('\nВведите количество подынтервалов N2: '))
            values.append(N2)


        # Метод левых прямоугольников

        print('\nМетод левых прямоугольников при N = ', N)
        z1 = leftRectRule(a, b, N)

        if z1 > 10**5: # Проверка на переполнение
            break

        values.append(z1)
        print('Приближённое значение интеграла z = {:.5f}'.format(z1))
        z10 = exValueIntegral(a, b)
        print('Точное значение интеграла z0 = {:.5f}\n'.format(z10))
        print('Aбсолютная ошибка ΔX = {:.5g}'.format(abs(z10 - z1)))
        print('Относительная ошибка δX = {:.5g}\n'.format(abs((z10 - z1) /z10)))


        # Метод Симпсона (метод парабол)

        print('\nМетод Симпсона (метод парабол) при N = ', N)
        z2 = SimpsonRule(a, b, N)    

        if z2 > 10**5: # Проверка на переполнение
            break

        values.append(z2)
        print('Приближённое значение интеграла z = {:.5f}'.format(z2))
        z20 = exValueIntegral(a, b)
        print('Точное значение интеграла z0 = {:.5f}\n'.format(z20))
        print('Aбсолютная ошибка ΔX = {:.5g}'.format(abs(z20 - z2)))
        print('Относительная ошибка δX = {:.5g}'.format(abs((z20 - z2) /z20)))

        end += 1

    if z1 < 10**5 and z2 < 10**5:
        output(values)
    else:
        print('Переполнение!')

    # Подсчет необходимого количества подынтервалов N
    # для менее точного метода (метода левых прямоугольников)

#     eps = 10**(-5)
#     z1 = 0
#     N = 1
#     dx = (b - a) / N
#     x = a + dx / 2
#     while abs(z10 - z1) > eps:
#         z1 += function(x)
#         if z1 > z10:
#             z1 = 0
#             N *= 2
#             dx = (b - a) / N
#             x = a + dx / 2
#         x += dx
#         # print(abs(z10 - z1))
#     print('Минимальное количество подынтервалов N \
# для точного вычисления интеграла\nметодом левых прямоугольников:')
#     print('N = {:d} при точности ε = {:.5g}'. format(N, eps))

#     z1 = leftRectRule(a, b, N)
#     print('Приближённое значение интеграла z = {:.5f}'.format(z1))
#     print()
    print('─' * 59)