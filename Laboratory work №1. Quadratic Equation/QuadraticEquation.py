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
		print('{}{:.2f}{}'.format('\nКорень x: ', x, '\n'))
else:
	D = b * b - 4 * a * c
	if D >= 0:
		if D == 0:
			x = (-b + sqrt(D)) / 2 * a
			print('{}{:.2f}{}'.format('\nДва равных корня:\nx1,2 = ', x, '\n'))
		else:
			sqD =sqrt(D)
			x1 = (-b + sqD) / 2 * a
			x2 = (-b - sqD) / 2 * a
			print('{}{}{:.2f}{}{:.2f}{}'.format('\nКорень x1 и x2:', '\nx1 = ', x1, '  x2 = ', x2, '\n'))
	else:
		print('\nКорни мнимые\n')