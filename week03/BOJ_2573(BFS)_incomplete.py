import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

R, C = map(int, input().split())

graph = []
ice_map = []
ice = []

for i in range(R):
    
    ice_input = list(map(int, input().split()))

    for j in range(len(ice_input)):
      if ice_input[j] > 0:
          ice.append((i,j))

    graph.append(ice_input)
    ice_map = deepcopy(graph)

# print(ice)

year = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melt(arr):   # 빙산의 좌표값을 배열로 넣어주면 빙산을 녹임
    
    global ice_map
        
    q = deque()
    
    for x,y in arr:
        q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < R and 0 <= ny < C and ice_map[nx][ny] == 0:
                
                if graph[x][y] == 0:
                  continue                 
                graph[x][y] -= 1
    ice_map = deepcopy(graph)



def ice_location():   # 빙산의 좌표 update
  ice = []
  sum = 0
  for i in graph:
    for j in range(len(i)):
        if i[j] > 0:
          ice.append((i,j))
        
        sum += i[j]
  if sum ==0:
      print(0)
      exit(0)

def check_ice(arr):
    
    global ice_map
        
    q = deque()
    cx = arr[0][0]
    cy = arr[0][1]

    q.append((cx, cy))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < R and 0 <= ny < C and ice_map[nx][ny] > 0:
               
               ice_map[nx][ny] = 0
               q.append((nx,ny))
    
    sum_ice = 0
    for i in ice_map:
       sum_ice += sum(i)
    
    if sum_ice != 0:
       print(year)
       exit(0)


while True:   
  melt(ice)
  ice_location()
  year += 1
  check_ice(ice)




