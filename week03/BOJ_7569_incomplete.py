import sys
from collections import deque
input = sys.stdin.readline


num_col, num_row, num_height = map(int, input().split())

graph = []

tomato = []

for k in range(num_height):

    graph_xy = []

    for i in range(num_row):
        
        box_input_xy = list(map(int, input().split()))
        for j in range(len(box_input_xy)):
            if box_input_xy[j] ==1:
                tomato.append((i,j,k))

        graph_xy.append(box_input_xy)
    graph.append(graph_xy)
            

# print(tomato)
# print(graph)
# print(graph[1][2][1])

day = [1]
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(arr):
        
    q = deque()
    for x,y,z in arr:
        q.append((x,y,z))

    while q:
        x,y,z = q.popleft()

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]    

            if 0 <= nx < num_row and 0 <= ny < num_col and 0 <= nz < num_height:
                if graph[nz][nx][ny] == 0:
                
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append((nx, ny, nz))

                    # 이러면 주변 감염 완료

                    if graph[nz][nx][ny] > day[-1]:
                        day.append(graph[nz][nx][ny])

bfs(tomato)


newlist=[(i,j,k) for k in range(num_height) for i in range(num_row) for j in range(num_col) if graph[k][i][j]==0]

if newlist:
    print(-1)
else :
    print(max(day)-1)



