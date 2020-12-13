# Название города отправления и пункта назначения




# Одно действительное число - длина пути

# lengthWay = float(input('Введите длину пути: '))
lengthWay1 = 475.6
lengthWay2 = 516.3


# Первое действительное число - вместимость автомобильного бака в галлонах

# gallonsSize = float(input('Введите вместимость автомобильного бака (в галонах): '))
gallonsSize1 = 11.9
gallonsSize2 = 15.7


# Второе число - число миль, которое может проехать автомобиль, используя один галлон бензина

# spendGallon = float(input('Введите число миль, которое может проехать автомобиль: '))
spendGallon1 = 27.9
spendGallon2 = 22.1


# Третье число - стоимость заправки автомобиля (в долларах) в пункте отправления

# costPatrol = float(input('Введите стоимость бензина: '))
costPatrol1 = 14.98
costPatrol2 = 20.87


# Целое число (меньше 51) - число бензоколонок на пути следования

# amountPatrolStation = int(input('Введите число бензоколонок (не более 51): '))
amountPatrolStation1 = 6
amountPatrolStation2 = 3


# Первое число - расстояние от города отправления до бензоколонки

# distanceFromCityToPatrolStation = int(input('Введите расстояние от города отправления до бензоколонки: '))
distance1 = [102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6]
distance2 = [125.4, 297.9, 345.2, 516.3]


# Второе число - цена (в центах) одного галлона бензина на бензоколонке

# costPatrolForOneGallon = int(input('Введите цену (в центах одного галлона бензина): '))
cost1 = []
cost2 = [125.9, 112.9, 99.9]


# Общая стоимость поездки

# overallCost = costPatrol

# Конец данных (можно ввести любое отрицательное число или только -1?)

end = -1


# Временный модуль
print('Введите длину пути: ')
print()
print('Введите вместимость автомобильного бака (в галонах): ')
print('Введите число миль, которое может проехать автомобиль: ')
print('Введите стоимость бензина: ')
print('Введите число бензоколонок (не более 51): ')

print(lengthWay2)
print(gallonsSize2, spendGallon2, costPatrol2, amountPatrolStation2)
print(distance2, cost2)

# НЕОБЯЗАТЕЛЬНО
costPatrol2 *= 100 # Переводим доллары в центы

# Сколько всего миль может проехать автомобиль с учётом вместимости своего бака

currentGallonsSize = gallonsSize2

maxAutoMiles = autoMiles = gallonsSize2 * spendGallon2 # Максимальное количество миль, которое может пройти автомобиль на полном баке

currentMiles = 0
minCostTravel = costPatrol2 # Минимальная стоимость поездки начинается с первоначально введенной стоимости


for i in range(amountPatrolStation2):
    data = []

    print('_' * 59)
    print()
    print('ДАННЫЕ №', i)

    print('\nВведите расстояние от города отправления до бензоколонки: ')

    # while True:
    #     if distance2[i] > autoMiles:
    #         print('Бензоколонка слишком далеко! Автомобиль не доедет!\nВведите расстояние поменьше')
    #         print('\nВведите расстояние от города отправления до бензоколонки: ')
    #     else:
    #         data.append(distance2[i])
    #         break

    # while True:
    #     if distance2[i] > lengthWay2:
    #         print('Бензоколонка за пукнтом назначения!\nВведите расстояние поменьше')
    #         print('\nВведите расстояние от пункта отправления до бензоколонки: ')
    #     else:
    #         break

    data.append(distance2[i])

    print('Введите цену (в центах одного галлона бензина): ')
    data.append(cost2[i])
    print('data = ', data)

    # Проверка

    print()
    print('minCostTravel = ', minCostTravel)
    print('currentGallonsSize = ', currentGallonsSize)
    print()

    if i == 0:
        autoMiles -= distance2[i]
    else:
        autoMiles -= (distance2[i] - distance2[i - 1])
    currentGallonsSize = (autoMiles / spendGallon2)

    currentLengthWay2 = lengthWay2 - distance2[i]
    currentMiles = distance2[i + 1] - distance2[i]

    print('autoMiles and maxAutoMiles / 2  ', autoMiles, maxAutoMiles / 2)
    print('autoMiles and currentMiles  ', autoMiles, currentMiles)
    if autoMiles <= maxAutoMiles / 2 and autoMiles <= currentMiles:
        minCostTravel += round((gallonsSize2 - currentGallonsSize) * cost2[i] + 200, 2)
        currentGallonsSize = gallonsSize2

    # Проверка

    print('currentLengthWay2 = ', currentLengthWay2, ' осталось проехать')
    print('currentMiles = ', currentMiles, ' ехать до следующей заправки')
    print('autoMiles = ', autoMiles, ' автомобиль может ещё проехать')
    print('minCostTravel = ', minCostTravel)
    print('currentGallonsSize = ', currentGallonsSize)

print('_' * 59)

print()
print('Набор данных #1')
# print('Минимальная стоимость = $27.31')
print('Минимальная стоимость = $', round((minCostTravel / 100), 2))