# Вычисление минимальной стоимости поездки ИСПРАВИТЬ КОММЕНТАРИЙ

def сostTravel(gallonsSize, currentGallonsSize, cost):
    return round(((gallonsSize - currentGallonsSize) * cost + 200)) / 100


# Название города отправления и пункта назначения


# Общая стоимость поездки

# overallCost = costPatrol


# Конец данных (можно ввести любое отрицательное число или только -1?)

end = -1


# Временный модуль
print('Введите длину пути: ')
# lengthWay = float(input('Введите длину пути: '))
lengthWay1 = 475.6
lengthWay2 = 516.3
lengthWay3 = 800.0

print('Введите вместимость автомобильного бака (в галонах): ')
# gallonsSize = float(input('Введите вместимость автомобильного бака (в галонах): '))
gallonsSize1 = 11.9
gallonsSize2 = 15.7
gallonsSize3 = 11.9

print('Введите число миль, которое может проехать автомобиль: ')
# spendGallon = float(input('Введите число миль, которое может проехать автомобиль: '))
spendGallon1 = 27.4
spendGallon2 = 22.1
spendGallon3 = 27.4

print('Введите стоимость бензина: ')
# costPatrol = float(input('Введите стоимость бензина: '))
costPatrol1 = 14.98
costPatrol2 = 20.87
costPatrol3 = 14.98

print('Введите число бензоколонок (не более 51): ')
# amountPatrolStation = int(input('Введите число бензоколонок (не более 51): '))
amountPatrolStation1 = 6
amountPatrolStation2 = 3
amountPatrolStation3 = 12

# distanceFromCityToPatrolStation = int(input('Введите расстояние от города отправления до бензоколонки: '))
distance1 = [102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6] # + Финальное расстояние как последняя точка
distance2 = [125.4, 297.9, 345.2, 516.3]
distance3 = [102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6, 501.8, 554.4, 605.7, 675,1, 708.8, 800.0,]

# costPatrolForOneGallon = int(input('Введите цену (в центах одного галлона бензина): '))
cost1 = [99.9, 132.9, 147.9, 102.9, 112.9, 100.9]
cost2 = [125.9, 112.9, 99.9]
cost3 = [99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9,]

# Данные № 1

lengthWay = lengthWay1
gallonsSize = gallonsSize1
spendGallon = spendGallon1
costPatrol = costPatrol1
amountPatrolStation = amountPatrolStation1
distance = distance1
cost = cost1

# Данные № 2

# lengthWay = lengthWay2
# gallonsSize = gallonsSize2
# spendGallon = spendGallon2
# costPatrol = costPatrol2
# amountPatrolStation = amountPatrolStation2
# distance = distance2
# cost = cost2

# Данные № 3

# lengthWay = lengthWay3
# gallonsSize = gallonsSize3
# spendGallon = spendGallon3
# costPatrol = costPatrol3
# amountPatrolStation = amountPatrolStation3
# distance = distance3
# cost = cost3

print(lengthWay)
print(gallonsSize, spendGallon, costPatrol, amountPatrolStation)
print(distance, cost)

# Сколько всего миль может проехать автомобиль с учётом вместимости своего бака

currentGallonsSize = gallonsSize
maxAutoMiles = autoMiles = gallonsSize * spendGallon # Максимальное количество миль, которое может пройти автомобиль на полном баке
print('Максимальное количество миль, которое может пройти автомобиль maxAutoMiles = ', maxAutoMiles)

currentMiles = 0
minCostTravel = costPatrol # Минимальная стоимость поездки начинается с первоначально введенной стоимости

# Список минимальных стоимостей за поездку

minCostList = []
currentCostTravel = []

for i in range(amountPatrolStation):
    print('_' * 59)
    print()
    print('ДАННЫЕ №', i)

    print('\nВведите расстояние от города отправления до бензоколонки: ')

    # while True:
    #     if distance[i] > autoMiles:
    #         print('Бензоколонка слишком далеко! Автомобиль не доедет!\nВведите расстояние поменьше')
    #         print('\nВведите расстояние от города отправления до бензоколонки: ')
    #     else:
    #         data.append(distance[i])
    #         break

    # while True:
    #     if distance[i] > lengthWay:
    #         print('Бензоколонка за пукнтом назначения!\nВведите расстояние поменьше')
    #         print('\nВведите расстояние от пункта отправления до бензоколонки: ')
    #     else:
    #         break

    print('Введите цену (в центах одного галлона бензина): ')

    # Проверка

    print()
    print('minCostTravel = ', minCostTravel)
    print('currentGallonsSize = ', currentGallonsSize)
    print()

    if i == 0:
        autoMiles -= distance[i]
    else:
        autoMiles -= (distance[i] - distance[i - 1])
    currentGallonsSize = (autoMiles / spendGallon)

    currentLengthWay = lengthWay - distance[i]
    currentMiles = distance[i + 1] - distance[i]

    print('autoMiles and maxAutoMiles / 2  ', autoMiles, maxAutoMiles / 2)
    print('currentLengthWay = ', currentLengthWay, ' осталось проехать')
    print('currentMiles = ', currentMiles, ' ехать до следующей заправки')
    print('autoMiles = ', autoMiles, ' автомобиль может ещё проехать')
    print('currentGallonsSize = ', currentGallonsSize)
    print()

    # Сначала найдём нужные бензоколонки
    if maxAutoMiles >= currentLengthWay and currentGallonsSize <= gallonsSize / 2:
        currentCostTravel.append(сostTravel(gallonsSize, currentGallonsSize, cost[i]) + costPatrol)

    # А теперь ту бензоколонку, до которой водитель сможет доехать по условию
    if autoMiles <= maxAutoMiles / 2 and autoMiles <= currentMiles:
        currentGallonsSize = gallonsSize
        autoMiles = maxAutoMiles

    # Проверка

    # print('maxAutoMiles and currentLengthWay', maxAutoMiles, currentLengthWay)
    print('autoMiles and maxAutoMiles / 2  ', autoMiles, maxAutoMiles / 2)
    print('currentLengthWay = ', currentLengthWay, ' осталось проехать')
    print('currentMiles = ', currentMiles, ' ехать до следующей заправки')
    print('autoMiles = ', autoMiles, ' автомобиль может ещё проехать')
    print('currentGallonsSize = ', currentGallonsSize)

print('_' * 59)

minCostTravel = round(min(currentCostTravel), 2)

print()
print('Набор данных #1')
print(currentCostTravel)
print('Минимальная стоимость = $', minCostTravel)