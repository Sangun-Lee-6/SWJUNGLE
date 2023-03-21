import sys
input = sys.stdin.readline
from collections import deque


V, E = map(int, input().split())
indegree = [0] * (V+1)

graph = [[] for _ in range(V+1)]
output = [[] for _ in range(V+1)]

for _ in range(E):
    a,b = map(int, input().split() )
    graph[a].append(b)
    # a → b
    indegree[b] += 1

def topology_sort():
    
    q = deque()

    for i in range(1, V+1):    
        if indegree[i] == 0:
            q.append(i)
            output[i] = 1
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            indegree[i] -= 1
            output[i] = output[now] + 1

            if indegree[i] ==0:
                q.append(i)
    

topology_sort()
print(*output[1:])