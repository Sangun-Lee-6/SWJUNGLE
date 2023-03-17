import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

result = A*B*C

result = str(result)



for i in range(10):
    i = str(i)
    print(result.count(i))
