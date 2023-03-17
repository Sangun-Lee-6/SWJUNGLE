import sys

a_list = [int(sys.stdin.readline()) for _ in range(9)] 

max = max(a_list)

print(max)
print(a_list.index(max)+1)



