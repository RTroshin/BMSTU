# Программа "Integral"
# Сравнить два метода (метод левых прямоугольников и метод Симпсона)
# для вычисления определённого интеграла.
# Для метода с наименьшей точностью задать степень точности ε и
# выяснить количество N (количество подынтервалов), обеспечивающих
# установленную точность для вычисления интеграла
# 

# Функции, которые также должны работать в программе

#   f(x) = sin(x)*sin(x)
#   f1(x)= (1/2)*x - (1/4)*sin(2*x)

#   f(x) = x
#   f1(x)= (x**2)/2

#   f(x) = sin(3*x)*cos(2*x)
#   f1(x)= -(cos(5*x)/10 - (cos(x)/2

#   f(x) = e**x * sin(x)
#   f1(x)= e**x * (sin(x)-cos(x))/2

#   f(x) = 1/(1+x**2)
#   f1(x)= 1/2*log1p(x**2/(1+x**2))

#   f(x) = log1p(x)
#   f1(x)= x*log1p(x) - x
#

from math import exp, sin, cos


def main():
    values = []
    # СДЕЛАТЬ ФУНКЦИЮ ВВОДА!
    # a, b = map(int, input('Введите пределы интегрирования a и b: ')\
    # .split())
    # eps = float(input('Введите значение точности для вычисления: '))
    # N = N1 = int(input('Введите количество подынтервалов N1: '))
    # values.append(N1)
    # N = N2 = int(input('\nВведите количество подынтервалов N2: '))
    # values.append(N2)
    a = 0
    b = 10
    eps = 0.001
    N1 = 10
    N2 = 100
    values.append(N1)
    values.append(N2)

    z1LRR = leftRectRule(a, b, N1)
    z2LRR = leftRectRule(a, b, N2)
    values.append(z1LRR)
    values.append(z2LRR)
    z1SR = SimpsonRule(a, b, N1)
    z2SR = SimpsonRule(a, b, N2)
    values.append(z1SR)
    values.append(z2SR)

    z0 = exValueIntegral(a, b)

    # Проверка на переполнение
    if z1LRR < 10**5 or z2LRR < 10**5 or\
       z1SR < 10**5 or z2SR < 10**5:
        printValues(values)
    else:
        print('Переполнение!\n\
В результате вычислений получились слишком большие значения!')

    # Подсчет необходимого количества подынтервалов N
    # для менее точного метода (метода левых прямоугольников)

    N = 1
    z = leftRectRule(a, b, N)
    while abs(z - z0) > eps:
        N *= 2
        z = leftRectRule(a, b, N)
        # print(abs(k - m))
    print(N)

    # z1 = 0
    # N = 1
    # dx = (b - a) / N
    # x = a + dx / 2
    # while abs(z0 - z1) > eps:
    #     z1 += function(x)
    #     if z1 > z0:
    #         z1 = 0
    #         N *= 2
    #         dx = (b - a) / N
    #         x = a + dx / 2
    #     x += dx
    #     # print(abs(z0 - z1))
    print('Минимальное количество подынтервалов N \
для точного вычисления интеграла\nметодом левых прямоугольников:')
    print('N = {:d} при точности ε = {:.5g}'. format(N, eps))
    print('\nТочное значение интеграла z0 = {:.5f}'.format(z0))

    # print('При точности = ',e,' значение интеграла равно ', end ='')
    # print( '{:10.7f}'.format(k),' и достигнуто на ', n , 'отрезках')

    print('\nПогрешности метода левых прямоугольников')
    print('─' * 59)
    printObservationalError(z1LRR, z0, N1)
    printObservationalError(z2LRR, z0, N2)

    print('Погрешности метода Симпсона')
    print('─' * 59)
    printObservationalError(z1SR, z0, N1)
    printObservationalError(z2SR, z0, N2)

# Подынтегральная функция
# def function(x):
#     f = (-2) * exp(x) * sin(x)
#     return f

# Первообразная (примитивная функция)
# def primFunction(x):
#     F = exp(x) * (cos(x) - sin(x))
#     return F

# Подынтегральная функция
def function(x):
    f = x
    return f

# Первообразная (примитивная функция)
def primFunction(x):
    F = (x**2)/2
    return F

# Точное значение интеграла
def exValueIntegral(a, b):
    z0 = primFunction(b) - primFunction(a)
    return z0

# Метод левых прямоугольников
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

# Метод Симпсона (метод парабол)
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

# Вывод таблицы значений на экран
def printValues(values):
    print('Таблица точных значений z')
    print('┌', '─' * 29, '┬', '─' * 13, '┬', '─' * 13, '┐', sep = '')
    print('│       Название метода       │   N1 = {:^3d}'.format(values[0]) +
          '  │   N2 = {:^3d}  │'.format(values[1]))
    print('├', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
    print('│ Метод левых прямоугольников │ {:11.3f} │ {:11.3f} │'\
            .format(values[2], values[4]))
    print('├', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
    print('│ Метод Симпсона              │ {:11.3f} │ {:11.3f} │'\
            .format(values[3], values[5]))
    print('└', '─' * 29, '┴', '─' * 13, '┴', '─' * 13, '┘', sep = '')
    print()

# Вывод значений погрешностей на экран
def printObservationalError(z, z0, N):
    print('Приближённое значение интеграла z = {:.5f}'.format(z))
    print('Aбсолютная ошибка ΔX = {:.5g}'.format(abs(z0 - z)))
    print('Относительная ошибка δX = {:.5g}'.format(abs((z0 - z) /z0)))
    print()


if __name__ == "__main__":
    main()