import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
v = [[0]*(N+1) for _ in range(N+1)]
# 부품 개수를 저장하는 리스트 v


for _ in range(M):
    a,b,c = map(int, input().split())
    graph[b].append((a,c))
    indegree[a] += 1

q = deque()

for i in range(N+1):
    if indegree[i] ==0:
        q.append(i)
        v[i][i] = 1    # 기본 부품만 1 로 설정

while q:
    now = q.popleft()
    for node in graph[now]:         # node 는 (다음 부품 번호, 그걸 만드는데 필요한 개수)
        
        for i in range(1, N+1):
            # 다음 부품을 만드는데 필요한 부품 계산, 현재 부품 만드는데 드는 개수에 다음 부품 만들때 필요한 부품 곱해줌
            next_part = node[0]
            count = node[1]

            v[next_part][i] += count*v[now][i]
            
        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            q.append(next_part)

for i in range(1, N+1):
    if v[N][i]:  
        print(f"{i} {v[N][i]}")