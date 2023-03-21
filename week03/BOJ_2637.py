import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
connect = [[] for _ in range(n+1)]
need = [[0]*(n+1) for _ in range(n+1)]
indegree = [0]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())  
    connect[b].append((a,c))
    indegree[a] += 1

q = deque()

for i in range(1, n+1):
    if indegree[i] ==0:
        q.append(i)

while q:
    now = q.popleft()
    for part, num_parts in connect[now]:
        if need[now].count(0) == n+1:
            need[part][now] += num_parts
        else :
            for i in range(1, n+1):
                need[part][i] += need[now][i] * num_parts
        indegree[part] -= 1
        if indegree[part] ==0:
            q.append(part)

for x in enumerate(need[n]):
    if x[1] > 0:
        print(*x)
