import matplotlib.pyplot as plt
import numpy as np
# from scipy.optimize import bisect
from math import pi, sin, cos, exp, sqrt

def f1(t):
    # return exp(-0.5 * t) * cos(2 * pi * t)
    return -2 * pi * exp(-0.5 * t) * sin(2 *  pi * t) - 0.5 * exp(-0.5 * t) * cos(2 * pi * t)

def f2(x):
    return (-5 / 2) * sin(x) * cos((5 / 2) * cos(x))

def secondDerivative_f2(x):
    return -(25 * (sin(x))**2 * sin(5 * cos(x) / 2) / 4) - (5 * cos(x) * cos(5 * cos(x) / 2) / 2)

def f3(x):
    return -sqrt(x**2) * sin(x) + sqrt(x**2) * cos(x) / x

def secondDerivative_f3(x):
    return -sqrt(x**2) * cos(x) - 2 * sqrt(x**2) * sin(x) / x

def secondDerivative_f1(x):
    return abs(2 * x) * (-3 * sqrt(33) / 112 + 1 /16) + ((3 - x) / sqrt(abs(1 - (abs(x) - 3))**2)) + 1 / 2

figure = plt.gcf()
figure.canvas.set_window_title('Исследование графиков функций')

# Изменить цвет графика
# plt.plot(x, y, 'red')
# plt.plot(x, y, 'r')
# plt.show()
# plt.plot(x, y, ':')
# plt.show()
# plt.plot(x, y, '*')
# plt.show()
# plt.plot(x, y, '<')
# plt.show()

# plt.plot(x, y, 'red', linewidth=3)                # Ширина линии графика
# plt.title('График', fontsize=16, loc='left')      # Обозначение титульного (над рамкой графика)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

# Гармоническая функция

t = np.linspace(0, 5, 100000) # Равномерное распределение точек на промежутке

plt.subplot(221) # Размещение на поле нескольких графиков
plt.title('Уравнение свободных затухающий колебаний', fontsize=12)
plt.xlabel('t')
plt.ylabel('x')

# graph = plt.plot(t, np.exp(-0.5 * t) * np.cos(2 * pi * t), 'r', label=r'$x$', linewidth=3)
# plt.plot(t, np.exp(-0.5 * t), '--', 'b', label=r'$x$', linewidth=2)
# plt.plot(t, -np.exp(-0.5 * t), '--', 'b', label=r'$A0e^bt$', linewidth=2)

plt.plot(t, np.exp(-0.5 * t) * np.cos(2 * pi * t),
         'r',
         label = r'$x = A_0e^{-βt}cos(ω_0t)$',
         linewidth=3)
plt.plot(t, np.exp(-0.5 * t),
         '--',
         color='b',
         label = r'$y = A_0e^{-βt}$',
         linewidth=2)
plt.gca().set_prop_cycle(None)
plt.plot(t, -np.exp(-0.5 * t),
         '--',
         color='b',
         linewidth=2)

# for value in t:
#     xt = x(value)
#     if xt > x(value - 0.1) and xt > x(value + 0.1) or\
#        xt < x(value - 0.1) and xt < x(value + 0.1):
#         plt.scatter(value, xt,
#                     color='r',
#                     marker='D',
#                     label='Точки')

data_t = data_x = np.array([])
for value in t:
    xt = f1(value)
    if xt > -1e-3 and xt < 1e-3:
        data_t = np.append(data_t, value)
        data_x = np.append(data_x, exp(-0.5 * value) * cos(2 * pi * value))

plt.scatter(data_t, data_x,
            color='r',
            marker='D', label='Экстремумы функции x')

# lab1 = r'$x = A_0e^{-βt}cos(ω_0t)$' # Использование стиля LaTeX для оформления математических записей
# lab2 = r'$x = A_0e^{-βt}$'
# lab3 = 'Экстремумы функции x'
# plt.legend((lab1, lab2, lab3), loc='best', fontsize=10)
plt.legend(loc='upper right', fontsize=10)
plt.grid()

# Периодическая функция

x = np.linspace(-10, 10, 100000) # Равномерное распределение точек на промежутке

plt.subplot(222)
plt.title('Периодическая функция', fontsize=12)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-10, 10, -2, 2])

plt.plot(x, np.sin((5 / 2) * np.cos(x)), 'g', label=r'$y = sin(5/2cos(x)$', linewidth=3)
plt.plot(x, x - x + 1,
         '--',
         color='b',
         label = r'$y_{1,2} = ±1$',
         linewidth=2)
plt.gca().set_prop_cycle(None)
plt.plot(x, x - x - 1,
         '--',
         color='b',
         linewidth=2)

data_x = data_y = np.array([])
for value in x:
    xt = f2(value)
    if xt > -1e-3 and xt < 1e-3:
        data_x = np.append(data_x, value)
        data_y = np.append(data_y, sin((5 / 2) * cos(value)))

plt.scatter(data_x, data_y,
            color='g',
            marker='o', label='Экстремумы функции y')

data_x = data_y = np.array([])
for value in x:
    xt = secondDerivative_f2(value)
    if xt > -1e-2 and xt < 1e-2:
        data_x = np.append(data_x, value)
        data_y = np.append(data_y, sin((5 / 2) * cos(value)))

plt.scatter(data_x, data_y,
            color='g',
            marker='s', label='Точки перегиба функции y')

plt.legend(loc='upper right', fontsize=10)
plt.grid()

# Непериодическая функция

# x = np.linspace(0, 15.707963, 100000) # Равномерное распределение точек на промежутке

# plt.subplot(223)
# plt.title('Непериодическая функция', fontsize=12)
# plt.xlabel('x')
# plt.ylabel('y')

# plt.plot(x, x * np.cos(x), 'm', label=r'$y = x * cos(x)$', linewidth=3)

# data_x = data_y = np.array([])
# for value in x:
#     xt = f3(value)
#     if xt > -1e-3 and xt < 1e-3:
#         data_x = np.append(data_x, value)
#         data_y = np.append(data_y, value * np.cos(value))

# plt.scatter(data_x, data_y,
#             color='m',
#             marker='D', label='Экстремумы функции y')

# plt.legend(loc='upper right', fontsize=10)
# plt.grid()

# Полином

x = np.linspace(0, 10, 100000) # Равномерное распределение точек на промежутке

plt.subplot(223)
plt.title('Полином второй степени', fontsize=12)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x, np.sqrt(x**2) * np.cos(x), 'm', label=r'$y = \sqrt{x^2} * cos(x)$', linewidth=3)
plt.plot(x, x - x,
         '--',
         color='b',
         label = r'$y_1 = 0$',
         linewidth=2)

data_x = data_y = np.array([])
for value in x:
    xt = f3(value)
    if xt > -1e-3 and xt < 1e-3:
        data_x = np.append(data_x, value)
        data_y = np.append(data_y, sqrt(value**2) * cos(value))

plt.scatter(data_x, data_y,
            color='m',
            marker='>', label='Экстремумы функции y')

data_x = data_y = np.array([])
for value in x:
    xt = secondDerivative_f3(value)
    if xt > -1e-2 and xt < 1e-2:
        data_x = np.append(data_x, value)
        data_y = np.append(data_y, sqrt(value**2) * cos(value))

plt.scatter(data_x, data_y,
            color='m',
            marker='s', label='Точки перегиба функции y')

plt.legend(loc='lower left', fontsize=10)
plt.grid()

# Спираль

# t = np.linspace(0, 15.707963, 100000) # Равномерное распределение точек на промежутке

# plt.subplot(223)
# plt.title('Спираль', fontsize=12)
# plt.xlabel('x')
# plt.ylabel('y')

# plt.plot(t * np.sin(t), t * np.cos(t), 'm', label=r'$y = sin(5/2cos(x)$', linewidth=3)

# data_x = data_y = np.array([])
# for value in t:
#     xt = f3(value)
#     if xt > -1e-3 and xt < 1e-3:
#         data_x = np.append(data_x, value)
#         data_y = np.append(data_y, value * np.sin(value))

# plt.scatter(data_x, data_y,
#             color='m',
#             marker='D', label='Экстремумы функции x')

# data_x = data_y = np.array([])
# for value in t:
#     yt = f4(value)
#     if yt > -1e-3 and yt < 1e-3:
#         data_x = np.append(data_x, value)
#         data_y = np.append(data_y, value * np.cos(value))

# plt.scatter(data_x, data_y,
#             color='m',
#             marker='D', label='Экстремумы функции y')

# plt.legend(loc='upper right', fontsize=10)
# plt.grid()

# Функция Бэтмена (бэтфункция)
# TODO Оформить код правильно

x = np.linspace(-10, 10, 100000) # Равномерное распределение точек на промежутке
f = np.linspace(-10, 10, 100000)

plt.subplot(224)
plt.title('Функция Бэтмена', fontsize=12)
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,
         np.abs(x / 2) - ((3 * np.sqrt(33) - 7) / 112) * x**2 - 3 + np.sqrt(1 - (np.abs(np.abs(x) - 2) - 1)**2),
         color='black',
         label=r'$y1 = sin(5/2cos(x)$',
         linewidth=3)
plt.plot(x,
         9 * np.sqrt(np.abs((np.abs(x) - 1) * (np.abs(x) - 0.75)) / ((1 - np.abs(x)) * (np.abs(x) - 0.75))) - 8 * np.abs(x),
         color='black',
         label=r'$y2 = sin(5/2cos(x)$',
         linewidth=3)
plt.plot(x,
         2.25 * np.sqrt(np.abs((x - 0.5) * (x + 0.5)) / ((0.5 - x) * (0.5 + x))),
         color='black',
         label=r'$y3 = sin(5/2cos(x)$',
         linewidth=3)
plt.plot(x,
         3 * np.abs(x) + 0.75 * np.sqrt(np.abs((np.abs(x) - 0.75) * (np.abs(x) - 0.5)) / ((0.75 - np.abs(x)) * (np.abs(x) - 0.5))),
         color='black',
         abel=r'$y3 = sin(5/2cos(x)$',
         linewidth=3)
plt.plot(x,
         6 * np.sqrt(10) / 7 + (1.5 - 0.5 * np.abs(x)) * np.sqrt(np.abs(np.abs(x) - 1) / (np.abs(x) - 1)) - 6 * np.sqrt(10) / 14 *np.sqrt(4 - (np.abs(x) - 1)**2),
         color='black',
         label=r'$y3 = sin(5/2cos(x)$',
         linewidth=3)
plt.plot(7 * np.sin(f) * np.sqrt(np.abs(np.abs(7 * np.sin(f)) - 3) / (np.abs(7 * np.sin(f)) - 3)),
         3 * np.cos(f) * np.sqrt(np.abs(3 * np.cos(f) + 3 * np.sqrt(33) / 7) / (3 * np.cos(f) + 3 * np.sqrt(33) / 7)),
         color='black',
         label=r'$y3 = sin(5/2cos(x)$',
         linewidth=3)

data_x = data_y = np.array([])
for value in x:
    xt = secondDerivative_f1(value)
    if xt > -1e-3 and xt < 1e-3:
        data_x = np.append(data_x, value)
        data_y = np.append(data_y, abs(value / 2) - ((3 * sqrt(33) - 7) / 112) * value**2 - 3 + sqrt(1 - (abs(abs(value) - 2) - 1)**2))

plt.scatter(data_x, data_y,
            color='black',
            marker='>', label='Экстремумы функции y')

# plt.plot(x,
#          np.sin((5 / 2) * np.cos(x)), 'g', label=r'$y4 = sin(5/2cos(x)$', linewidth=3)
# plt.plot(x,
#          np.sin((5 / 2) * np.cos(x)), 'g', label=r'$y5 = sin(5/2cos(x)$', linewidth=3)
# plt.plot(x,
#          np.sin((5 / 2) * np.cos(x)), 'g', label=r'$y6 = sin(5/2cos(x)$', linewidth=3)

# data_x = data_y = np.array([])
# for value in x:
#     xt = f2(value)
#     if xt > -1e-3 and xt < 1e-3:
#         data_x = np.append(data_x, value)
#         data_y = np.append(data_y, sin((5 / 2) * cos(value)))

# plt.scatter(data_x, data_y,
#             color='g',
#             marker='D', label='Экстремумы функции y')

# plt.legend(loc='lower left', fontsize=10)
plt.grid()

plt.tight_layout() # Подгонка полей под края графиков
plt.show()

# x = np.linspace(-10, 10, 25)
# plt.plot(x, 'r', label=r'$x$', linewidth=3)
# plt.plot(np.sin(x), 'b', label=r'$sinx$', linewidth=3)
# plt.title('Title', loc='left', fontsize=10)
# plt.legend(loc='best', fontsize=10)

# plt.axis([0, 10, -10, 10])

# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.tight_layout()
# plt.show()

# x1 = np.linspace(-10, 10., 100)
# x4 = np.linspace(-2, 2, 10)
# y1 = np.sin(x1)
# y2 = np.cos(x1)
# y3 = x1**2 * np.exp(-x1**2)
# y4 = abs(x4)

# plt.plot(y1, '--', label='sin(x)')
# plt.plot(y2, label='cos(x)')
# plt.plot(y3, '-.', label='$x1^2 exp(-x2^2)$')
# plt.plot(y4, ':', linewidth=5, label='|x|')
# plt.title('4 graphs')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()