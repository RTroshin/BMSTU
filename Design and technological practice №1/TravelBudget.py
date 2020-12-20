# Вычисление минимальной стоимости поездки

# def сostComputation(gallonsSize, currentGallonsSize, cost):
#     return round(((gallonsSize - currentGallonsSize) * cost + 200)) / 100

def maxSteps(amountPatrolStation, maxAutoMiles, distance):
    step = 1
    for n in range(amountPatrolStation + 1):
        if maxAutoMiles >= distance[n]:
            step += 1
    return step

def kuznechik(steps, temp):
    C = [0] * (steps)
    print(C)
    count = 0
    for i in range(steps - 1):
        C[i] = min(C[i - count], C[i - count - 1]) + temp[i]
        if count < steps - 1:
            count += 1
    return C[i]

    
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
distance3 = [102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6, 501.8, 554.4, 605.7, 675,1, 708.8, 800.0]

# costPatrolForOneGallon = int(input('Введите цену (в центах одного галлона бензина): '))
cost1 = [99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 0.0]
cost2 = [125.9, 112.9, 99.9, 0.0] # + Финальная стоимость бензина равна 0
cost3 = [99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 0.0]

# Данные № 1

# lengthWay = lengthWay1
# gallonsSize = gallonsSize1
# spendGallon = spendGallon1
# costPatrol = costPatrol1
# amountPatrolStation = amountPatrolStation1
# distance = distance1
# cost = cost1

# Данные № 2

lengthWay = lengthWay2
gallonsSize = gallonsSize2
spendGallon = spendGallon2
costPatrol = costPatrol2
amountPatrolStation = amountPatrolStation2
distance = distance2
cost = cost2

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
print('Максимальное количество миль, которое может пройти автомобиль: ', maxAutoMiles)

currentMiles = 0
minCostTravel = costPatrol # Минимальная стоимость поездки начинается с первоначально введенной стоимости

# Список минимальных стоимостей за поездку

minCostList = []
currentCostTravel = []


# print('\nНачало динамического программирования\n')
# C = []
# C = [0] * (amountPatrolStation + 1)


# print('\nНачало динамического программирования\n')
# C = []
# C = [0] * (amountPatrolStation + 1)
# print(distance)

# for i in range(amountPatrolStation + 1):
# 	C[i] = min(C[i - 1], C[i - 2]) + distance[i]
# print('Ответ: ', C[amountPatrolStation])


# Заменил на for!
# i = 0
# while distance[i] < maxAutoMiles:
#     if i == 0:
#         autoMiles -= distance[i]
#     else:
#         autoMiles -= (distance[i] - distance[i - 1])
#     currentGallonsSize = (autoMiles / spendGallon)
#     minCostList.append(round(((gallonsSize - currentGallonsSize) * cost[i] + 200)) / 100)
#     i += 1
# print('minCostList = ', minCostList)
# print('autoMiles = ', autoMiles)


# minCostList.append(0.0) # Цена бензина в пункте назначения (там автомобиль не заправляется)

# print('minCostList = ', minCostList)
# count = 0
# for i in range(amountPatrolStation + 1):
#     # N1 = C[i - count]
#     # M1 = C[i - count - 1]    
#     # N = C[i - 1]
#     # M = C[i - 2]
#     # print(N1, M1)
#     # print(N, M)
#     C[i] = min(C[i - count], C[i - count - 1]) + minCostList[i]
#     # C[i] = min(C[i - 1], C[i - 2]) + distance[i]
#     if count < n - 2:
#         count += 1


# print()
# print('Набор данных #1')
# print('Минимальная стоимость = $', C[amountPatrolStation] + costPatrol)


costList = []
costStep = []

print('steps = ', maxSteps(amountPatrolStation, maxAutoMiles, distance))
steps = maxSteps(amountPatrolStation, maxAutoMiles, distance)


print(distance)
print(cost)
for s in range(steps):
    costStep = []
    autoMiles = maxAutoMiles
    for i in range(s, amountPatrolStation + 1):
        if s == 0:
            d = 0
        else:
            d = distance[s - 1]
        if distance[i] < maxAutoMiles + d:
            if i == 0:
                autoMiles -= distance[i]
            else:
                autoMiles -= (distance[i] - distance[i - 1])
            currentGallonsSize = (autoMiles / spendGallon)
            costStep.append(round(((gallonsSize - currentGallonsSize) * cost[i] + 200)) / 100)
    costList.append(costStep)
print('costList = ', costList)
print('autoMiles = ', autoMiles)

print()

temp = [0] * steps
for s in range(steps):
    for i in range(len(costList[s])):
        temp[s + i] = costList[s][i]
    print(temp)
    result = kuznechik(steps, temp)
    print(result)

#     print('currentLengthWay = ', currentLengthWay, ' осталось проехать')
#     print('currentMiles = ', currentMiles, ' ехать до следующей заправки')
#     print('autoMiles = ', autoMiles, ' автомобиль может ещё проехать')
#     print('currentGallonsSize = ', currentGallonsSize)