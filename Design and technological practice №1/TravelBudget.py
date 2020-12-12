# Название города отправления и пункта назначения




# Одно действительное число - длина пути

# lengthWay = float(input('Введите длину пути: '))
lengthWay = 475.6




# Первое действительное число - вместимость автомобильного бака в галлонах

# gallonsSize = float(input('Введите вместимость автомобильного бака (в галонах): '))
gallonsSize = 11.9

# Второе число - число миль, которое может проехать автомобиль, используя один галлон бензина

# spendGallon = float(input('Введите число миль, которое может проехать автомобиль: '))
spendGallon = 27.9

# Третье число - стоимость заправки автомобиля (в долларах) в пункте отправления

# costPatrol = float(input('Введите стоимость бензина: '))
costPatrol = 14.98

# Целое число (меньше 51) - число бензоколонок на пути следования

# amountPatrolStation = int(input('Введите число бензоколонок (не более 51): '))
amountPatrolStation = 6




# Первое число - расстояние от города отправления до бензоколонки

# distanceFromCityToPatrolStation = int(input('Введите расстояние от города отправления до бензоколонки: '))
distanceFromCityToPatrolStation1 = 102.0
distanceFromCityToPatrolStation2 = 220.0
distanceFromCityToPatrolStation3 = 256.3
distanceFromCityToPatrolStation4 = 275.0
distanceFromCityToPatrolStation5 = 277.6
distanceFromCityToPatrolStation6 = 381.8

# Второе число - цена (в центах) одного галлона бензина на бензоколонке

# costPatrolForOneGallon = int(input('Введите цену (в центах одного галлона бензина): '))
costPatrolForOneGallon1 = 99.9
costPatrolForOneGallon2 = 132.9
costPatrolForOneGallon3 = 147.9
costPatrolForOneGallon4 = 102.9
costPatrolForOneGallon5 = 112.9
costPatrolForOneGallon6 = 100.9




# Общая стоимость поездки

overallCost = costPatrol # Должно получиться $27.31

# Конец данных (можно ввести любое отрицательное число или только -1?)

end = -1

# Временный модуль
print('Введите длину пути: ')
print()
print('Введите вместимость автомобильного бака (в галонах): ')
print('Введите число миль, которое может проехать автомобиль: ')
print('Введите стоимость бензина: ')
print('Введите число бензоколонок (не более 51): ')

print(lengthWay)
print(gallonsSize, spendGallon, costPatrol, amountPatrolStation)
print(distanceFromCityToPatrolStation1, costPatrolForOneGallon1)

costPatrol *= 100 # Переводим доллары в центы

# Сколько всего миль может проехать автомобиль с учётом вместимости своего бака

gallonsSize = 11.9
spendGallon = 27.9

MinCostTravel = 0

MaxMiles = gallonsSize * spendGallon

data = []
amountPatrolStation = 1
for i in range(amountPatrolStation):
    print('\nВведите расстояние от города отправления до бензоколонки: ')

    while True:
        if distanceFromCityToPatrolStation1 > MaxMiles:
            print('Бензоколонка слишком далеко! Автомобиль не доедет!\nВведите расстояние поменьше')
            print('\nВведите расстояние от города отправления до бензоколонки: ')
        else:
            data.append(distanceFromCityToPatrolStation1)
            break

    while True:
        if distanceFromCityToPatrolStation1 > lengthWay:
            print('Бензоколонка за пукнтом назначения!\nВведите расстояние поменьше')
            print('\nВведите расстояние от пункта отправления до бензоколонки: ')
        else:
            break
    print('Введите цену (в центах одного галлона бензина): ')
    data.append(costPatrolForOneGallon1)
    MinCostTravel += (costPatrol + 200)

    lengthWay -= distanceFromCityToPatrolStation1

print()
print('MaxMiles = ', MaxMiles)
print('lengthWay= ', lengthWay)
print(data)
print()
print('Набор данных #1')
print('Минимальная стоимость = $27.31')
print('Минимальная стоимость = $', round((MinCostTravel / 100), 2))

