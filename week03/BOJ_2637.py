import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
v = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    graph[b].append((a,c))
    indegree[a] += 1

q = deque()

for i in range(N+1):
    if indegree[i] ==0:
        q.append(i)
        v[i][i] = 1   

while q:
    now = q.popleft()
    for node in graph[now]:                 
        for i in range(1, N+1):
            next_part = node[0]
            count = node[1]

            v[next_part][i] += count*v[now][i]
            
        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            q.append(next_part)

for i in range(1, N+1):
    if v[N][i]:  
        print(f"{i} {v[N][i]}")