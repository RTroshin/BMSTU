from collections import deque


def main():
    graph = readGraph()
    print(graph)
    start = 0
    finish = len(graph) - 1
    shortestDistance = dijkstra(graph, start)
    shortestPath = displayShortestPath(graph, start, finish, shortestDistance)

    goal = finish
    visited = displayShortestPath(graph, start, finish, shortestDistance)

    v = goal
    print(f'\npath from {goal} ro {start}: \n {goal} ', end = '')
    while v != start:
        v = visited[v]
        print(f'---> {v} ', end = '')

    return shortestPath

# def dijkstra(graph, start, finish):
#     queue = deque()
#     queue.append(start)
#     S = {}
#     S[start] = 0
#     v = start
#     while v is not finish:
#         v = queue.popleft()
#         for u in graph[v]:
#             if u not in S or S[v] + graph[v][u] < S[u]:
#                 S[u] = S[v] + graph[v][u]
#                 queue.append(u)
#     return S

def dijkstra(graph, start):
    queue = deque()
    S = {}
    S[start] = 0
    queue.append(start)
    while queue:
        v = queue.popleft()
        if v == len(graph):
            continue
        for u in graph[v]:
            if u not in S or S[v] + graph[v][u] < S[u]:
                S[u] = S[v] + graph[v][u]
                queue.append(u)
    print('S = ',  S)
    return S

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
    # distance = [0.0, 102.0, 220.0, 256.3, 275.0, 277.6, 381.8, 475.6, 501.8, 554.4, 605.7, 675.1, 708.8, 800.0]
    # cost = [1498, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 99.9, 132.9, 147.9, 102.9, 112.9, 100.9, 0.0]

    for i in range(amountStations + 2):
        currentAutoMiles = maxAutoMiles # Условие №2. На каждой бензоколонке водитель всегда заполняет бензобак полностью.
        for j in range(i + 1, amountStations + 2):
            # dist, cost = map(int, input().split())
            # distance.append(dist)
            if distance[j] < maxAutoMiles + distance[i]:
                # currentAutoMiles -= (dist - distance[j - 1])
                currentAutoMiles -= (distance[j] - distance[j - 1])
                currentFuelTank = currentAutoMiles / fuelConsumption
                if j != amountStations + 1:
                    weight = round(((fuelTank - currentFuelTank) * cost[j] + 200)) / 100
                else:
                    weight = round(((fuelTank - currentFuelTank) * cost[j])) / 100
                addEdge(graph, i, j, weight)
    return graph

def addEdge(graph, a, b, weight):
    if a not in graph:
        graph[a] = {b: weight}
    else:
        graph[a][b] = weight

# def displayShortestPath(graph, start, finish, S):
#     queue = deque()
#     v = finish
#     queue.append(finish)
#     while v is not start:
#         for u in range(len(S) - 1 , 0, -1):
#             print('S[u] = ', S[u])
#             print('graph[v][u]) = ', graph[v][u])
#             print(S[v], '==', S[u] + graph[v][u])
#             if S[v] == S[u] + graph[v][u]:
#                 queue.appendleft(v)
#         v -= 1
#     print(queue)
#     print(S)
#     return queue

def displayShortestPath(graph, start, finish, S):
    queue = deque()
    visited = {start: None}

    v = start
    queue.append(start)
    
    while queue:
        v = queue.popleft()
        if v == finish:
            break

        U = graph[v]
        for u in U:
            # print('S[u] = ', S[u])
            # print('graph[v][u]) = ', graph[v][u])
            # print(S[v], '==', S[u] + graph[v][u])
            if u not in visited:
                queue.appendleft(u)
                visited[u] = v
    print(queue)
    print(visited)
    return queue


if __name__ == "__main__":
    main()