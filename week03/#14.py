import sys
sys.setrecursionlimit(10**6)
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]


for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    

visited_bfs = [False]*(N+1)

output_list = []

def bfs(V):
    queue = deque([V])
    # visited_bfs[V] = True
    while queue:

        V = queue.popleft()
        
        for i in graph[V]:
            if not visited_bfs[i] and i != 1:
                visited_bfs[i] = visited_bfs[V]+1
                queue.append(i)

                if visited_bfs[i] == K:
                    output_list.append(i)

bfs(X)

if output_list:
    output_list.sort()
    for i in output_list:
        print(i)
else :
    print(-1)