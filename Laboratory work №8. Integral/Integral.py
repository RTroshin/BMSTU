# Программа "Integral"
# Сравнить два метода (метод левых прямоугольников и метод Симпсона)
# для вычисления определённого интеграла.
# Для метода с наименьшей точностью задать степень точности ε и
# выяснить количество N (количество подынтервалов), обеспечивающих
# установленную точность для вычисления интеграла
# 

# Функции, которые также должны работать в программе

#   f(x) = sin(x) * sin(x)
#   f1(x)= (1 / 2) * x - (1 / 4) * sin(2 * x)

#   f(x) = x
#   f1(x)= (x**2) / 2

#   f(x) = sin(3 * x) * cos(2 * x)
#   f1(x)= -(cos(5 * x) / 10 - (cos(x) / 2

#   f(x) = e**x * sin(x)
#   f1(x)= e**x * (sin(x) - cos(x)) / 2

#   f(x) = 1 / (1 + x**2)
#   f1(x)= 1 / 2 * log1p(x**2 / (1 + x**2))

#   f(x) = log1p(x)
#   f1(x)= x * log1p(x) - x


# Функция №1
# def function(x):
#     return sin(x) * sin(x)

# def primFunction(x):
#     return (1 / 2) * x - (1 / 4)*sin(2 * x)

# Функция №2
# def function(x):
#     return x

# def primFunction(x):
#     return (x**2) / 2

# Функция №3
# def function(x):
#     return sin(3 * x) * cos(2 * x)

# def primFunction(x):
#     return -(cos(5 * x) / 10) - cos(x) / 2

# Функция №4
# def function(x):
#     return e**x * sin(x)

# def primFunction(x):
#     return e**x * (sin(x) - cos(x)) / 2

# Функция №5
# def function(x):
#     return 1 / (1 + x**2)

# def primFunction(x):
#     return 1 / 2 * log1p(x**2 / (1 + x**2))

# Функция №6
# def function(x):
#     try:
#         return log1p(x)
#     except ValueError:
#         return None

# def primFunction(x):
#     try:
#         return x * log1p(x) - x
#     except ValueError:
#         return None
#

from math import e, exp, log1p, sin, cos

def main():
    while True:
        print()
        values = []
        # СДЕЛАТЬ ФУНКЦИЮ ВВОДА!
        while True:
            try:
                a, b = map(int,\
                    input('Введите пределы интегрирования a и b: ').split())
                # eps = float(input\
                # ('Введите значение точности для вычисления: '))
                # N1 = int(input\
                # ('Введите количество подынтервалов N1: '))
                # N2 = int(input\
                # ('\nВведите количество подынтервалов N2: '))
                break
            except ValueError:
                print('Некорректный ввод!\nПопробуйте ещё раз!')
        eps = 0.0001
        N1 = 10
        N2 = 100

        z1LRR = leftRectRule(a, b, N1)
        z2LRR = leftRectRule(a, b, N2)
        z1SR = SimpsonRule(a, b, N1)
        z2SR = SimpsonRule(a, b, N2)
        z0 = exValueIntegral(a, b)

        # Проверка на правильность заданных пределов интегрирования №1
        if z1LRR is None or z2LRR is None or\
             z1SR is None or z2SR is None:
            print('Функция не может быть задана в данном диапазоне!\n\
Введите другие пределы интегрирования a и b')

        # Проверка на переполнение
        elif z1LRR > 10**5 or z2LRR > 10**5 or\
            z1SR > 10**5 or z2SR > 10**5:
            print('Переполнение!\n\
В результате вычислений получились слишком большие значения!')
            print('Введите другие значения')

        # Проверка на правильность заданных пределов интегрирования №2
        elif z1LRR < 0 or z2LRR < 0 or\
             z1SR < 0 or z2SR < 0 or z0 <= 0:
            print('Функция не может быть задана в данном диапазоне!\n\
Введите другие пределы интегрирования a и b')

        else:
            break
    values.append(N1)
    values.append(N2)
    values.append(z1LRR)
    values.append(z2LRR)
    values.append(z1SR)
    values.append(z2SR)
    printValues(values)

    # Подсчет необходимого количества подынтервалов N
    # для менее точного метода (метода левых прямоугольников)

    Sum = 0
    z = 1
    previous = 0
    N = 1
    dx = (b - a) / N
    x = a + dx / 2
    while abs(z - previous) > eps:
        previous = z
        z += function(x)
        Sum += z
        N *= 2
        dx = (b - a) / N
        x = a + dx / 2
    # z *= dx
    print('dx = ', Sum * dx)
    print('dx = ', z * dx)

    print('Точное значение интеграла равно z0 = {:.5f}'.format(z0))
    print('\nВычисление приближенного значения для менее\n\
точного метода (метода левых прямоугольников)')
    print('─' * 59)
    print('При точности ε = {:.5g}'.format(eps) + ' значение интеграла равно \
z = {:.5f}'.format(Sum) + '\nи достигнуто на N = {:d}'.format(N) + ' отрезках')
    print()

    print('\nПогрешности метода левых прямоугольников')
    print('─' * 59)
    printObservationalError(z1LRR, z0, N1)
    printObservationalError(z2LRR, z0, N2)
    print()
    print('Погрешности метода Симпсона')
    print('─' * 59)
    printObservationalError(z1SR, z0, N1)
    printObservationalError(z2SR, z0, N2)

# Подынтегральная функция
def function(x):
    return (-2) * exp(x) * sin(x)

# Первообразная (примитивная функция)
def primFunction(x):
    return exp(x) * (cos(x) - sin(x))

# Точное значение интеграла
def exValueIntegral(a, b):
    try:
        z0 = primFunction(b) - primFunction(a)
        return z0
    except TypeError:
        return None

# Метод левых прямоугольников
def leftRectRule(a, b, N):
    try:
        z = 0
        dx = (b - a) / N
        x = a + dx / 2
        for i in range(N):
            if z > 10**5:
                break
            z += function(x)
            x += dx
        return z * dx
    except TypeError:
        return None

# Метод Симпсона (метод парабол)
def SimpsonRule(a, b, N):
    try:
        dx = (b - a) / N
        dx2 = dx / 2
        z = (function(a) + function(b)) / 2 + 2 * function(b - dx2)
        # z = function(a) + function(b) + 4 * function(a + dx2)
        x = a + dx
        for i in range(1, N):
            if z > 10**5:
                break
            z += function(x) + 2 * function(x - dx2)
            # z += 2 * function(a + (2 * i) * dx2) + 4 * function(a + (2 * i + 1) * dx2)
            x += dx
        return z * dx / 3
    except TypeError:
        return None

# Вывод таблицы значений на экран
def printValues(values):
    print('Таблица приближённых значений z')
    print('┌', '─' * 29, '┬', '─' * 13, '┬', '─' * 13, '┐', sep = '')
    print('│       Название метода       │   N1 = {:^3d}'.format(values[0]) +
          '  │   N2 = {:^3d}  │'.format(values[1]))
    print('├', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
    print('│ Метод левых прямоугольников │ {:11.3f} │ {:11.3f} │'\
            .format(values[2], values[3]))
    print('├', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
    print('│ Метод Симпсона              │ {:11.3f} │ {:11.3f} │'\
            .format(values[4], values[5]))
    print('└', '─' * 29, '┴', '─' * 13, '┴', '─' * 13, '┘', sep = '')
    print()

# Вывод значений погрешностей на экран
def printObservationalError(z, z0, N):
    print('При N = {:d}'.format(N))
    print('Aбсолютная ошибка ΔX = {:.5g}'.format(abs(z0 - z)))
    print('Относительная ошибка δX = {:.5g}'.format(abs((z0 - z) / z0)))
    print()


if __name__ == "__main__":
    main()