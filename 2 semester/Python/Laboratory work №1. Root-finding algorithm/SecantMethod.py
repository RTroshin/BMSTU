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
#     return x * x

# def secantMethod(function, a, b, values):
#     answer = {'x': 'value', 'y': 'value', 'errno': 'value'}
#     x = a
#     xPrevious = a + 2 * values['eps']
#     errno = i = 0
#     while abs(x - xPrevious) >= values['eps'] and i <= values['N']:
#         x, xPrevious = x - function(x) / (function(x) - function(xPrevious)) * (x - xPrevious), x
#         i += 1
#     y = function(x)
#     print('Значение функции в найденном корне (метод Хорд):\nf({:.5g}) = {:.5g}'.format(x, y), sep='', end='\n\n')
#     answer['x'] = x
#     answer['y'] = y
#     answer['errno'] = errno
#     return answer

def secantMethod(function, a, b, values):
    answer = {'method': 'Secant', '': 'value', 'x': 'value', 'y': 'value', 'a': 'value', 'b': 'value', 'errno': 'value'}
    answer['a'] = a
    answer['b'] = b
    errno = i = 0
    while abs(b - a) >= values['eps']:
        if function(a) * function(b) >= 0:
            # print('f(a) и f(b) должны иметь противоположные знаки')
            # errno = '1'
            errno = 1
            break
        elif i >= values['N']:
            # print('Превышено максимальное количество итераций ', values['N'], sep='')
            errno = 2
            break
        elif abs(function(a)) > 10**9 or abs(function(a)) > 10**9:
            # print('Результат функции превышает допустимое значение')
            errno = 3
            break
        else:
            a = b - (b - a) * function(b) / (function(b) - function(a)) # НЕМНОГО ПЕРЕДЕЛАТЬ В СООТВЕТСТВИИ С ВИКИПЕДИЕЙ!
            x = b = a - (a - b) * function(a) / (function(a) - function(b))
            i += 1
    if not errno:
        y = function(x)
        # print('Корень = ', x, sep='')
        # print('Значение функции в найденном корне (метод Хорд):\nf({:.5f}) = {:.5g}'.format(x, y), sep='', end='\n\n')
        answer['x'] = x
        answer['y'] = y
    answer['errno'] = errno
    return answer

def BrentsMethod(function, a, b, values):
    answer = {'method': 'Brent', '': 'value', 'x': 'value', 'y': 'value', 'a': 'value', 'b': 'value', 'errno': 'value'}
    answer['a'] = a
    answer['b'] = b
    try:
        # r = _zeros._brentq(f, a, b, xtol, rtol, maxiter, args, full_output, disp)
        # root = brentq(function, values['a'], values['b'], xtol=values['eps'], rtol=values['eps'], maxiter=values['N'])
        x = brentq(function, a, b, xtol=values['eps'], rtol=values['eps'], maxiter=values['N'])
        y = function(x)
        answer['x'] = x
        answer['y'] = y
        # print('Корень = ', x, sep='')
        # print('Значение функции в найденном корне (метод Брента):\nf({:.5f}) = {:.5g}'.format(x, y), sep='', end='\n\n')
    except ValueError:
        # print('f(a) и f(b) должны иметь противоположные знаки')
        # errno = '1'
        errno = 1
    except RuntimeError:
        # print('Превышено максимальное количество итераций ', values['N'], sep='')
        errno = 2
    except OverflowError:
        # print('Результат функции превышает допустимое значение')
        errno = 3
    else:
        errno = 0
    answer['errno'] = errno
    return answer

# Вывод таблицы значений на экран
def printValues(answers):
    print(answers)
    if answers[0]['method'] == 'Secant':
        print('\nМетод хорд')
    elif answers[0]['method'] == 'Brent':
        print('\nМетод Бранта')
    print('┌', '─' * 9, '┬', '─' * 12, '┬', '─' * 22, '┬', '─' * 22, '┬', '─' * 12, '┐', sep = '')
    print('│ № корня │ Промежуток │  Значение корня (x)  │ Значение функции (y) │ Код ошибки │')
    print('├', '─' * 9, '┼', '─' * 12, '┼', '─' * 22, '┼', '─' * 22, '┼', '─' * 12, '┤', sep = '', end='\n')
    lenAnswers = len(answers)
    for i in range(len(answers)):
        if answers[i]['errno'] == 1:
            pass
        # answer = {'method': 'Secant', '': 'value', 'x': 'value', 'y': 'value', 'a': 'value', 'b': 'value', 'errno': 'value'}
        elif not answers[i]['x'] == 'value' or not answers[i]['y'] == 'value':
            print('│   {:^3d}   │  [{:3},{:3}] │ {:20.8g} │ {:20.8g} │ {:^10d} │'\
            .format(i + 1, answers[i]['a'], answers[i]['b'], answers[i]['x'], answers[i]['y'], answers[i]['errno']))
        elif i < lenAnswers - 1 and answers[i]['errno'] == 1:
            print('├', '─' * 9, '┼', '─' * 12, '┼', '─' * 22, '┼', '─' * 22, '┼', '─' * 12, '┤', sep = '', end='\n')
        else:
            print('│   {:^3d}   │  [{:3},{:3}] │ Не удалось уточнить корень │                │ {:^10d} │'\
            .format(i + 1, answers[i]['a'], answers[i]['b'], answers[i]['errno']))
    print('└', '─' * 9, '┴', '─' * 12, '┴', '─' * 22, '┴', '─' * 22, '┴', '─' * 12, '┘', sep = '', end='\n')


if __name__ == "__main__":
    main()