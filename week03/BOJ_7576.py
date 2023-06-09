import sys
input = sys.stdin.readline
from collections import deque
q = deque()

C, R = map(int, input().split())

graph = []
tomato = []
for i in range(R):
    
    row_input = list(map(int, input().split()))
    for j in range(len(row_input)):
        if row_input[j] == 1:
            tomato.append((i,j))
    
    graph.append(row_input)


dr = [-1,0,1,0]
dc = [0,-1,0,1]

def bfs(arr):
    global answer    

    for r,c in arr:
        q.append((r,c))
    
    while q:
        r,c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0<= nr < R and 0<=nc<C and graph[nr][nc] == 0:
                
                graph[nr][nc] = graph[r][c] + 1
                q.append((nr,nc))
                answer = max(graph[nr][nc]-1, answer)
    

answer = 0
bfs(tomato)
if any(0 in l for l in graph):
    print(-1)
else :
    print(answer)
      
            