import sys
input = sys.stdin.readline
from collections import deque

R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

dr = [-1,0,1,0]
dc = [0,-1,0,1]

q = deque()
def bfs(r,c):

    graph[r][c] = 0    
    q.append((r,c))
    area = 1
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < R and 0 <= nc < C and graph[nr][nc] ==1:
                
                graph[nr][nc] = 0
                q.append((nr, nc))
                area += 1
    return area


cnt = 0
ans = 0
for i in range(R):
    for j in range(C):
        if graph[i][j] ==1:
            cnt += 1
            ans = max(bfs(i,j), ans)

print(cnt)
print(ans)

