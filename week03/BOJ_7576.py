import sys
from collections import deque
input = sys.stdin.readline


num_col, num_row = map(int, input().split())

graph = []
tomato = []

for i in range(num_row):
    
    box_input = list(map(int, input().split()))
    for j in range(len(box_input)):
        if box_input[j] ==1:
            tomato.append((i,j))

    graph.append(box_input)
            
            
# print(tomato)
# print(graph)

day = [1]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(arr):
        
    q = deque()
    for x,y in arr:
        q.append((x,y))

    while q:
        x,y = q.popleft()

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < num_row and 0 <= ny < num_col and graph[nx][ny] == 0:
                
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))

                # 이러면 주변 감염 완료

                if graph[nx][ny] > day[-1]:
                    day.append(graph[nx][ny])

bfs(tomato)


newlist=[(i,j) for i in range(num_row) for j in range(num_col) if graph[i][j]==0]

if newlist:
    print(-1)
else :
    print(max(day)-1)



