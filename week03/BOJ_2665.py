import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
maze = [list(input().rstrip()) for _ in range(N)]



dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if (r, c) == (N-1, N-1):
            print(visited[N-1][N-1])
            return
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc] == -1:
                if maze[nr][nc] == '1':
                    visited[nr][nc] = visited[r][c]
                    q.appendleft((nr, nc))
                elif maze[nr][nc] == '0':
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))


bfs()