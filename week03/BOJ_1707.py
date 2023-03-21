def dfs(V, group):
    
    global error

    if error :    
        return
    
    visited_dfs[V] = group    # 방문한 V 를 group 등록

    # visited_dfs 리스트는 False 값으로 초기화
    # 거기서 group 등록이 되었다면 False 가 group 값으로 바뀜

    for i in graph[V]:              # graph[V] 와 연결된 node 번호가 들어있음
        
        if not visited_dfs[i]:      # 연결된 노드의 값이 False 라면(= 방문하지 않았다면)
            dfs(i, -group)          # 해당 노드를 방문해서 다른 group 으로 등록
        
        elif visited_dfs[V] == visited_dfs[i]: # 인접한 노드끼리 group 값이 같다면 이분 그래프가 아님
            error = True
            return

import sys
sys.setrecursionlimit(10**6)

T = int(sys.stdin.readline())

for _ in range(T):
    
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited_dfs = [False]*(V+1)
    error = False

    for _ in range(E):
        
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    # print(graph)
    
    for i in range(1, V+1):
        if not visited_dfs[i]:
            dfs(i, 1)
            if error:
                break
    
    if error:
        print('NO')
    else :
        print('YES')



    

