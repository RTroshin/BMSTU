# Программа "Quadratic Equation"
# Условие задания:
# Составить программу для решения квадратного уравнения
# Составить функциональную схему к данной программе
#

from math import sqrt

print('\nДано квадратное уравнение вида ax^2 + bx + c = 0')

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

if a == 0:
	if b == 0:
		if c == 0:
			print('\nБесконечно много решений\n')
		else:
			print('\nКорней нет\n')
	else:
		x = -c / b
		print('\nКорень x: {:.2f}\n'.format(x))
else:
	D = b * b - 4 * a * c
	if D >= 0:
		if D == 0:
			x = (-b + sqrt(D)) / 2 * a
			print('\nДва равных корня:\nx1,2 = {:.2f}\n'.format(x))
		else:
			sqD =sqrt(D)
			x1 = (-b + sqD) / 2 * a
			x2 = (-b - sqD) / 2 * a
			print('\nКорень x1 и x2:\nx1 = {:.2f}  x2 = {:.2f}\n'.format(x1, x2))
	else:
		print('\nКорни мнимые\n')