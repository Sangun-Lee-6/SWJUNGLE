### 입력 받기, 변수 초기화

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

distance = [INF] *(N+1)

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

### dijkstra 함수

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

print(distance[end])
