from collections import deque


def displayShortestPath(G, start, finish, S):
    # v = finish # Здесь можно поставить 0
    # queue = deque([finish])
    Q = deque()
    v = finish
    Q.append(v)
    while v is not start:
        for u in G[v]:
            if S[v] == S[u] + G[v][u]:
                Q.appendleft(u)
                v = u
                break
    return Q

def dijkstra(G, start):
    Q = deque()
    S = {}
    S[start] = 0
    Q.append(start)
    while Q:
        v = Q.popleft()
        for u in G[v]:
            if u not in S or S[v] + G[v][u] < S[u]:
                S[u] = S[v] + G[v][u]
                Q.append(u)
        print('S = ', S)
    return Q

def main():
    G = readGraph()
    start = 0
    # start = int(input('Введите начальную вершину: '))
    # while start not in G:
    #     start = int(input('Вершина в графе отсутствует\n' +
    #                   'Введите начальную вершину: ')) 
    shortestDistance = dijkstra(G, start)
    finish = int(input('Введите конечную вершину: '))
    while start not in G:
        finish = int(input('Вершина в графе отсутствует\n' +
                       'Введите конечную вершину: '))
    shortestPath = displayShortestPath(G, start, finish, shortestDistance)
    return shortestPath

def readGraph():
    # M = int(input()) # Количество рёбер, далее - "A, d, вес"
    graph = {}

    # fuelTank = 11.9
    # fuelConsumption = 27.4
    # amountStations = 6 # Количество вершин для бензоколонок
    # startCost = 1498
    # wayLength = 475.6

    fuelTank = 15.7
    fuelConsumption = 22.1
    amountStations = 3 # Количество вершин для бензоколонок
    startCost = 2087
    wayLength = 516.3

    # fuelTank = 11.9
    # fuelConsumption = 30.1
    # amountStations = 12 # Количество вершин для бензоколонок
    # startCost = 1498
    # wayLength = 800.0

    maxAutoMiles = currentAutoMiles = fuelTank * fuelConsumption # Столько миль автомобиль может проехать с полным баком
    # G = {0: {1: wayAndCost}}
    # G = {0: {2: wayAndCost}}
    # G = {0: {3: wayAndCost}}

    startWeight = startCost
    finishWeight = 0

    # distance = [0.0, 102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6]
    # cost = [1498, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 0.0]
    distance = [0, 125.4, 297.9, 345.2, 516.3]
    cost = [2087, 125.9, 112.9, 99.9, 0.0]
    # distance = [0.0, 102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6, 501.8, 554.4, 605.7, 675,1, 708.8, 800.0]
    # cost = [1498, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 0.0]


    for i in range(amountStations + 2):
        currentAutoMiles = maxAutoMiles # Условие №2. На каждой бензоколонке водитель всегда заполняет бензобак полностью.
        for j in range(i + 1, amountStations + 2):
            # dist, cost = map(int, input().split())
            # distance.append(dist)
            if distance[j] < maxAutoMiles + distance[i]:
                # if j == 0:
                #     # currentAutoMiles -= dist
                #     currentAutoMiles -= distance[j]
                #     addEdge(graph, 0, j + 1, startWeight)
                # else:
                # currentAutoMiles -= (dist - distance[j - 1])
                currentAutoMiles -= (distance[j] - distance[j - 1])
                currentFuelTank = currentAutoMiles / fuelConsumption
                weight = round(((fuelTank - currentFuelTank) * cost[j] + 200)) / 100
                addEdge(graph, i, j, weight)

    addEdge(graph, j + 1, amountStations + 1, finishWeight)
    print('graph = ', graph)
    print()
    return graph

def addEdge(graph, a, b, weight):
    if a not in graph:
        graph[a] = {b: weight}
    else:
        graph[a][b] = weight


if __name__ == "__main__":
    main()