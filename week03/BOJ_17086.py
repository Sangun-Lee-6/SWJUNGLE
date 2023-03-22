import sys
input = sys.stdin.readline
from collections import deque
q = deque()

R, C = map(int, input().split())
graph = []
shark = []
for i in range(R):
    row_input = list(map(int, input().split()))
    for j in range(len(row_input)):
        if row_input[j] == 1:
            shark.append((i,j))
    graph.append(row_input)


dr = [-1,0,1,0,-1,1,-1,1]
dc = [0,-1,0,1,-1,-1,1,1] 
ans = 0
def bfs(arr):
    global ans
    
    for r,c in arr:
        q.append((r,c))
    
    while q:
        r,c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < R and 0 <= nc < C and graph[nr][nc] == 0:
                
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr,nc))
                ans = max(ans, graph[nr][nc]-1)

bfs(shark)
print(ans)