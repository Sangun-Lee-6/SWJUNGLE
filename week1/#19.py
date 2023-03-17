import sys

x, y = map(str,sys.stdin.readline().split())

x = int(x[::-1])
y = int(y[::-1])

if x > y :
    print(x)
else :
    print(y)


