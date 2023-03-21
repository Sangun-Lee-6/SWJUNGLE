from collections import deque
import sys
input=sys.stdin.readline
R,C=map(int,input().split())
arr=[list(input().strip()) for _ in range(R)]



dx=[1,-1,0,0]
dy=[0,0,1,-1]

def escape():
    queue=deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j]=='D':   #도착지 좌표기록 후 루프 탈출 조건에 사용
                D=[i,j]
            elif arr[i][j]=='*':    #물 위치 기록 후 큐에 먼저 넣는다.
                queue.append([i,j,'*'])
            elif arr[i][j]=='S':
                arr[i][j]=0
                S=[i,j,0]
    queue.append(S)            #물이 모두 큐에 들어간 이후에 고슴도치를 넣는다.

    while queue:
        x,y,z=queue.popleft()
        if x==D[0] and y==D[1]:
            print(z)
            break
        else:
            for i in range(4):  #물과 고슴도치의 인접영역으로 이동 가능 여부 확인 후 이동
                nx=x+dx[i]
                ny=y+dy[i]
                if z=='*' and 0<=nx<R and 0<=ny<C and arr[nx][ny]!='X' and arr[nx][ny]!='D' and arr[nx][ny]!='*':
                    arr[nx][ny]='*'
                    queue.append([nx,ny,'*'])
                elif type(z)==int and 0<=nx<R and 0<=ny<C and (arr[nx][ny]=='.' or arr[nx][ny]=='D'):
                    arr[nx][ny]=z+1
                    queue.append([nx,ny,z+1])
        if len(queue)==0:
            print('KAKTUS')
            break

escape()
