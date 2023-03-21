import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())    # R 행 C 열

graph = []
House = []
Water = []
Rabbit = []

for i in range(R):
    
    temp = input().rstrip()
    temp_list = []
    for c in temp:
        temp_list.append(c)
    
    for j in range(len(temp_list)):
        if temp_list[j] == 'D':
            House.append((i,j))
        elif temp_list[j] == '*':
            temp_list[j] = 0
            Water.append((i,j))
        elif temp_list[j] == 'S':
            Rabbit.append((i,j))
    graph.append(temp_list)
        

# print(House)
# print(Water)
# print(Rabbit)
# print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs_Water(arr):
        
    q = deque()
    for x,y in arr:
        q.append((x,y))

    while q:
        x,y = q.popleft()

        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 'X' and graph[nx][ny] != 'D':

                if type(graph[nx][ny]) == str:                                    
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
                else :
                    continue

                # 이러면 물 지도 그리기 완료

bfs_Water(Water)
# print(graph)



def bfs_Rabbit(x,y):

    graph[x][y] = 0

    global time
        
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        if graph[x][y] < time:
            continue

        time +=1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= R or nx < 0 or ny >= C or ny < 0:
                continue

            if graph[nx][ny] == '. ':
                graph[nx][ny] = time
                q.append((nx, ny))
                continue

            if graph[nx][ny] == 'D':
                print(time)
                exit(0)        

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != 'X' and (graph[nx][ny] - time) >=1: 
                graph[nx][ny] = time
                q.append((nx, ny))

    print('KAKTUS')
    exit(0)

time = 0
bfs_Rabbit(Rabbit[0][0], Rabbit[0][1])

# 토끼 지도를 따로 그려보기
# 물 지도의 값을 변화시켜서 문제가 발생할 수도 있음
# 