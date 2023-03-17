# V = 올라간 높이
# A = 낮에 올라간 높이
# B = 밤에 미끄러진 높이
# day = 올라가는데 걸린 일 수

# V = (A-B) * day + A

# V-A = (A-B)*day
# day = V-A / A-B

import sys

A, B, V = map(int, sys.stdin.readline().split())
day = int((V-A) / (A-B)) +1

print(day)

