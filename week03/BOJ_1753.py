# Dijkstra

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

start = int(input())

graph = [[] for _ in range(N+1)]

distance = [INF] *(N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))


def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for temp_node, temp_cost in graph[now]:
            
            cost = dist + temp_cost

            if cost < distance[temp_node]:
                distance[temp_node] = cost
                heapq.heappush(q, (cost, temp_node))

dijkstra(start)

for i in range(1, N+1):
    if distance[i] == INF:
        print('INF')
    else :
        print(distance[i])
