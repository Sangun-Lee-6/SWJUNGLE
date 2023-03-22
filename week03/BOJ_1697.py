import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
MAX = 100001
array = [0] * MAX
q = deque()

def bfs(N):
    
    q.append(N)

    while q:
        N = q.popleft()

        if N ==K :
            return array[N]
        
        for next_N in (N-1, N+1, N*2):
            
            if 0<= next_N < MAX and not array[next_N]:
                q.append(next_N)
                array[next_N] = array[N] + 1

print(bfs(N))