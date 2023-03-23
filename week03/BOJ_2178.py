import sys
input = sys.stdin.readline
from collections import deque
q = deque()

R, C = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(R)]


dr = [-1,0,1,0]
dc = [0,-1,0,1]

def bfs(r,c):
    
    q.append((r,c))

    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < R and 0<= nc < C and graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr,nc))
    return graph[R-1][C-1]

print(bfs(0,0))