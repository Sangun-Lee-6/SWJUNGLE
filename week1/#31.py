import sys

N = int(sys.stdin.readline())

input_list = []
for i in range(N):
    
    num = int(sys.stdin.readline())
    input_list.append(num)

input_list.sort()

print(*input_list, sep='\n')