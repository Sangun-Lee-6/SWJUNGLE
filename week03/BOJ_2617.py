import sys

N, M = map(int, sys.stdin.readline().split())

heavy_list = [[] for _ in range(N + 1)]
light_list = [[] for _ in range(N + 1)]

for _ in range(M):
    heavy, light = map(int, sys.stdin.readline().split())
    heavy_list[light].append(heavy)
    light_list[heavy].append(light)


def dfs(V, lst):
    
    global check
    
    visited[V] = True
    for i in lst[V]:
        if not visited[i]:
            check += 1
            dfs(i, lst)

count = 0
md = (N + 1) / 2
for i in range(1, N + 1):
    visited = [False] * (N + 1)

    check = 0
    dfs(i, heavy_list)
    if (check >= md):
        count += 1

    check = 0
    dfs(i, light_list)
    if check >= md:
        count += 1


print(count)