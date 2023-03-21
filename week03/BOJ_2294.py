from collections import deque
import sys
intput = sys.stdin.readline

n,k = map(int, input().split())
coins = set(int(input()) for _ in range(n))
check = [0 for _ in range(k+1)]

q = deque()

for coin in coins:
    if coin > k:
        continue
    q.append([coin, 1])
    check[coin] = 1

print(q)

flag = True
while q:
    val, cnt = q.popleft()
    if val == k:
        print(cnt)
        flag = False
        break
    
    for coin in coins:
        if val + coin > k:
            continue
        if check[val + coin] ==0:
            check[val+coin] = 1
            q.append([val+coin, cnt+1])

if flag :
    print(-1)