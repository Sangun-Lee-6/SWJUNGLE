#import sys
from collections import deque
#input = sys.stdin.readline

N = int(input()) ## 보드 크기
K = int(input()) ## 사과 개수


## NxN의 board를 만든다.
board_array = [[1]*(N+2)] + [[1]+[0]*N+[1] for _ in range(N)] + [[1]*(N+2)]


for i in range(K):
    a,b = map(int, input().split()) ## a,b:사과 위치
    board_array[a][b] = 2 ## 사과는 숫자 2로 표현

    
L = int(input()) ## 뱀의 방향 변환 횟수
## 뱀의 방향 변환 정보
L_array = list(map(lambda x:[int(x[0]), x[1]], [input().split() for _ in range(L)]))

time = 0 ## 첫 시작은 일단 0초부터
x,y = 1,1 ## 뱀의 첫 위치
direction = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} ## 0:북 1:동 2:남 3:서
d = 1 ## 현재 방향은 오른쪽 (동쪽)
snake_array = deque([[1,1]]) ## 뱀의 위치를 큐로 나타낸다.

## board_array -> 0:빈공간, 1:벽, 2:사과, 3:뱀
board_array[1][1] = 3 ## 처음 뱀이 (1,1)에 존재하므로

## 이동한 후에 뱀 머리의 위치가 벽이거나, 자신의 몸일 경우 stop
while(1):
    ## 일단 뱀의 머리를 이동시킨다. 바라보고 있는 방향으로.
    x = x + direction[d][0]
    y = y + direction[d][1]
    
    ## 이동한 곳에 사과가 있다.
    if board_array[x][y] == 2:
        board_array[x][y] = 3 ## 이제는 사과 대신 뱀의 머리가 위치한다.
        snake_array.append([x, y]) ## snake_array의 맨 오른쪽 원소가 머리, 왼쪽이 꼬리부분이다.
        time = time + 1
    ## 이동한 곳엔 사과가 없고, 그냥 빈 공간이다.
    elif board_array[x][y] == 0:
        board_array[x][y] = 3
        snake_array.append([x,y])
        del_x, del_y = snake_array.popleft() ## 뱀의 전체 길이는 변하지 않아야 하기 때문에 꼬리를 제거
        board_array[del_x][del_y] = 0
        time = time + 1
    ## 나머지는 이동한 위치가 벽(=1)이거나 자신의 몸(=3)이므로 stop
    else:
        time = time + 1
        break
    ## 뱀의 방향 전환 정보
    if len(L_array) != 0:
        if L_array[0][0] == time:
            if L_array[0][1] == 'L': ## 왼쪽으로 90도 회전
                d = (d-1)%4
            elif L_array[0][1] =='D': ## 오른쪽으로 90도 회전
                d = (d+1)%4
            del L_array[0] ## 방향 전환했으므로 제거

print(time)