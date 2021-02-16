# Программа "Secant method"
# Дано уравнение и большой отрезок
# Например y = sin(x) (-10, 0)
# Уточнить все корни на этом отрезке
# Ограничения:
# 1. Уточнить все корни уравнения проходя отрезок с шагом h
# На отрезке с шагом h может быть только один корень
# Задание шага 3 - правильно, 3.5 - неправильно
# Уравнение задается в виде функции
# Функция которая будет производить вычисление
# Давать в комментариях описание метода уточнения (краткое)
# Параметры для задавания
# 1. Левые и правые концы интервала
# 2. Точность eps
# 3. Максимальное количество итераций (переполнение)
# Если переполнение - то нельзя уточнить корень
# 4. Полученный корень действительное число типа float
# 5. Значение функции в точке корня
# 6. Код ошибки
# Например: если уточнить корни нельзя, целая величина 1, 2, 3 с объяснением ошибки 
# 7. Результаты вывести в виде таблицы
#
# 1. Метод хорд
# 2. Метод Брента (brentq)
#

from scipy.optimize import brentq
from math import e, pi, exp, log, log1p, sin, cos, tan


def main():
    values = inputValues()
    values = {'a': 'value', 'b': 'value', 'h': 'value', 'eps': 'value', 'N': 'value'}
    # values['a'] = 1
    # values['b'] = 5
    # values['h'] = 1
    # values['eps'] = 0.0005
    # values['N'] = 10

    answersSecant = []
    answersBrents = []
    a = values['a']
    b = a + values['h']
    while b <= values['b']:
        answersSecant.append(secantMethod(function, a, b, values))
        a += values['h']
        b += values['h']
    a = values['a']
    b = a + values['h']
    while b <= values['b']:
        answersBrents.append(BrentsMethod(function, a, b, values))
        a += values['h']
        b += values['h']
    # print(answersSecant)
    # print(answersBrents)
    printValues(answersSecant)
    printValues(answersBrents)

def inputValues():
    values = {'a': 'value', 'b': 'value', 'h': 'value', 'eps': 'value', 'N': 'value'}
    print()
    while True:
        try:
            values['a'], values['b'] = map(int, input('Введите интервал (a, b): ').split())
            break
        except ValueError:
            print('Некорректный ввод!\nПопробуйте ещё раз')

    # if values['b'] > values['a']:
    #     values['a'], values['b'] = values['b'], values['a']
    # print(values)

    maxStep = abs(values['a']) + abs(values['b'])

    while True:
        try:
            while True:
                print('Введите шаг h для интервала (', values['a'], ', ', values['b'], '): ', sep = '', end='')
                values['h'] = int(input())
                if values['h'] > maxStep:
                    print('Неверное значение шага!\nЗначение шага должно быть меньше или равно ', maxStep, sep = '')
                elif values['h'] <= 0:
                    print('Неверное значение шага!\nЗначение шага должно быть больше нуля')
                else:
                    break
            break
        except ValueError:
            print('Некорректный ввод!\nПопробуйте ещё раз!\n')

#         # Проверка на правильность заданных пределов интегрирования №2
#         elif z1LRR < 0 or z2LRR < 0 or\
#              z1SR < 0 or z2SR < 0 or z0 <= 0:
#             print('Функция не может быть задана в данном диапазоне!\n\
# Введите другие пределы интегрирования a и b')

#         # Проверка на переполнение
#         elif z1LRR > 10**5 or z2LRR > 10**5 or\
#             z1SR > 10**5 or z2SR > 10**5:
#             print('Переполнение!\n\
# В результате вычислений получились слишком большие значения!')
#             print('Введите другие значения')
#         else:
#             break

    while True:
        try:
            while True:
                values['eps'] = float(input\
                ('Введите значение точности eps для вычисления (eps > 0 ): '))
                if values['eps'] <= 0:
                    print('Неверное значение точности!\nЗначение точности должно быть больше нуля')
                else:
                    break
            break
        except ValueError:
            print('Некорректный ввод!\nПопробуйте ещё раз!\n')
    while True:
        try:
            while True:
                values['N'] = int(input\
                ('Введите максимальное количество итераций N (N > 0): '))
                if values['N'] <= 0:
                    print('Неверное значение итераций!\nЗначение итераций должно быть больше нуля')
                else:
                    break
            break
        except ValueError:
            print('Некорректный ввод!\nПопробуйте ещё раз!\n')
    return values

def function(x):
    return sin(x)

# def function(x):
#     return x**9999

# def function(x):
#     return x**2

def BrentsMethod(function, a, b, values):
    answer = {'x': 'value', 'y': 'value', 'errno': 'value'}
    try:
        # r = _zeros._brentq(f, a, b, xtol, rtol, maxiter, args, full_output, disp)
        # root = brentq(function, values['a'], values['b'], xtol=values['eps'], rtol=values['eps'], maxiter=values['N'])
        x = brentq(function, a, b, xtol=values['eps'], rtol=values['eps'], maxiter=values['N'])
        print('Корень = ', x, sep='')
        y = function(x)
        answer['x'] = x
        answer['y'] = y
        print('Значение функции в найденном корне:\nf({:.5f}) = {:.5f}'.format(x, y), sep='', end='\n\n')
    except ValueError:
        print('f(a) и f(b) должны иметь противоположные знаки')
        # errno = '1'
        errno = 1
    except RuntimeError:
        print('Превышено максимальное количество итераций ', values['N'], sep='')
        errno = '2'
    except OverflowError:
        print('Результат функции превышает допустимое значение')
        errno = '3'
    else:
        errno = 0
    answer['errno'] = errno
    return answer

# Вывод таблицы значений на экран
# def printValues(answersSecant, answersBrents):
#     if 
#         print('Метод хорд')
#     else:
#         print('Метод Бранта')
#     print('┌', '─' * 9, '┬', '─' * 29, '┬', '─' * 13, '┬', '─' * 13, '┐', sep = '')
#     print('│ № Корня │    Отрезок       │   Значение корня (x)  │   Значение функции (y) в точке корня  │   Код ошибки  │')
#     print('├', '─' * 9, '┼', '─' * 29, '┼', '─' * 13, '┼', '─' * 13, '┤', sep = '')
#     print('│ № Корня │ Метод левых прямоугольников │ {:11.3f} │ {:11.3f} │'.format(0, 1))
#     print('└', '─' * 9, '─' * 29, '┴', '─' * 13, '┴', '─' * 13, '┘', sep = '', end='\n')


if __name__ == "__main__":
    main()