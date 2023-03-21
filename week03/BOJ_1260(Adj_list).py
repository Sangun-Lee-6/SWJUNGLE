from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:          # graph 에는 연결되어 있는 노드만 추가되어 있음
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:

        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
# 문제 조건 : 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문
# 따라서 정렬하는 것, 꼭 모든 문제에서 정렬할 필요는 없다
for i in graph:
    i.sort()



# dfs
visited = [False] * (N + 1)
dfs(V)
print()

# bfs
visited = [False] * (N + 1)
bfs(V)