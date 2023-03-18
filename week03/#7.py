import sys

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]

while True:

    try :
        a,b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    except :
        break

# 문제에서 작은 번호의 노드부터 방문해야하는 조건은 없지만 편의상 정렬
for i in graph:
    i.sort()


visited_dfs = [False]*(N+1)
dict = dict()

def dfs(V):

    visited_dfs[V] = True
    # print(V, end=' ')

    for i in graph[V]:
        if not visited_dfs[i]:
            dict[i] = V
            dfs(i)

dfs(1)
# print(dict)

sort_dict = sorted( dict.items() )          # dict 의 key 값 기준으로 정렬 ∵ 출력 조건이 낮은 노드부터 출력

for i in sort_dict:
    print(i[1])
