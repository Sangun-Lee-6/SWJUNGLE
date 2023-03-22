import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
q = deque()

N = int(input())
graph = [list(map(str, input().rstrip())) for _ in range(N)]
JJJ_graph = deepcopy(graph)

dr = [-1,0,1,0]
dc = [0,-1,0,1]

def bfs(r,c,A):
    
    q.append((r,c))
    
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < N and 0<= nc < N and graph[nr][nc] == A:
                graph[nr][nc] = 0
                q.append((nr,nc))
    return A

def JJJ_bfs(r,c):
    
    q.append((r,c))
    
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < N and 0<= nc < N and (JJJ_graph[nr][nc] == 'R' or JJJ_graph[nr][nc] == 'G') :
                JJJ_graph[nr][nc] = 0
                q.append((nr,nc))
    return 'R'

def JJJ_bfs_blue(r,c):
    
    q.append((r,c))
    
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < N and 0<= nc < N and JJJ_graph[nr][nc] == 'B' :
                JJJ_graph[nr][nc] = 0
                q.append((nr,nc))
    return 'B'

result = []
JJJ_result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            result.append(bfs(i,j,'R'))
        elif graph[i][j] == 'G':
            result.append(bfs(i,j,'G'))
        elif graph[i][j] == 'B':
            result.append(bfs(i,j,'B'))
            

for i in range(N):
    for j in range(N):
        if JJJ_graph[i][j] == 'R':
            JJJ_result.append(JJJ_bfs(i,j))
        elif JJJ_graph[i][j] == 'G':
            JJJ_result.append(JJJ_bfs(i,j))
        elif JJJ_graph[i][j] == 'B':
            JJJ_result.append(JJJ_bfs_blue(i,j))


print(len(result), end= ' ')
print(len(JJJ_result), end= ' ')






