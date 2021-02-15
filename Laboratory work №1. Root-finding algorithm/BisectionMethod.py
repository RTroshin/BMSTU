# Программа "Bisection method"
#

from math import sqrt, sin

# N = 50
# XL, XR, eps = map(float, input('Введите XL, XR и eps: ').split())

# if (3 * pow(XL, 3) - 5 * sqrt(XL) + XL + 0.4) * (3 * pow(XR, 3) - 5 * sqrt(XR) + XR + 0.4) > 0:
#     print('Не выполнено условие применимости метода половинного деления!')
# else:
#     YL = 3 * pow(XL, 3)- 5 * sqrt(XL) + XL + 0.4
#     i = 0
#     while abs(XR - XL) > eps:
#         X = (XL + XR) / 2
#         Y = 3 * pow(X, 3)- 5 * sqrt(X) + X + 0.4
#         if Y * YL > 0:
#             XL = X
#         else:
#             XR = X
#         i += 1
#     if abs(XR - XL) < eps:
#         print('Корень уравнения ', X, ' найден за ', i, ' шагов, Y(X) = ', Y)
#     else:
#         print('Корень уравнения не найден')

N = 50
# XL, XR, eps = map(float, input('Введите XL, XR и eps: ').split())
XL = 1
XR = 5
eps = 0.0005

if sin(XL) > 0:
    print('Не выполнено условие применимости метода половинного деления!')
else:
    YL = sin(XL)
    i = 0
    while abs(XR - XL) > eps:
        X = (XL + XR) / 2
        Y = sin(XL)
        if Y * YL > 0:
            XL = X
        else:
            XR = X
        i += 1
    if abs(XR - XL) < eps:
        print('Корень уравнения ', X, ' найден за ', i, ' шагов, Y(X) = ', Y)
    else:
        print('Корень уравнения не найден')