def dfs(V):             # 탐색을 시작할 노드의 번호 V  
    global count
    visited[V] = True  # 해당 V값 방문처리
    count += 1
    for i in range(1, N + 1):
        if not visited[i] and graph[V][i]:  # 만약 i값을 방문하지 않았고 V와 연결이 되어 있다면
            dfs(i)  # 해당 i 값으로 dfs를 돈다.(더 깊이 탐색)

##
from collections import deque
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# 2차원 리스트를 False 로 초기화
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = True
    graph[b][a] = True
    # a ↔ b 가 서로 연결되어 있음

visited = [False] * (N + 1)  # dfs의 방문기록

count = -1    # 1번 노드는 count 에서 제외
dfs(1)
print(count)
