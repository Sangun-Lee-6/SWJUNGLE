def dfs(V, cnt):      # V : node 번호, cnt : 실외와 연결된 실내 node 개수
    
    visited_dfs[V] = True

    for i in graph[V]:      # V(node)와 연결된 인접 node 를 하나씩 불러옴
        
        if location[i] == 1:      # i(node) 가 실내(1)이라면
            cnt +=1               # 실내 개수에 +1
        
        elif not visited_dfs[i] and location[i] == 0:
            # i 를 방문하지 않았고 i 가 실외라면
            cnt = dfs(i, cnt)     # 해당 실외를 기준으로 dfs
    
    return cnt

#---Main code----

import sys
sys.setrecursionlimit(10**6)

ans = 0
N = int(sys.stdin.readline())

location = [0]+list(map(int, sys.stdin.readline().rstrip()))

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

    if location[a] ==1 and location[b] ==1:     # 둘 다 실내라면 → 경로 개수에 2개 추가
        ans += 2

sum = 0
visited_dfs = [False]*(N+1)
for i in range(1, N+1):
    if not visited_dfs[i] and location[i] ==0:
        x = dfs(i, 0)           # x 에는 실내 node 개수
        sum += x*(x-1)

print(sum + ans)