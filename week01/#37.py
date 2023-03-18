import sys
from itertools import permutations

N = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))



p_result = list(permutations(input_list, N))

result_list = []

for p in p_result:
    
    result = 0

    for i in range(len(p)):
        
        if i == len(p) - 1:
            break
        
        cha = abs(p[i] - p[i+1])
        result += cha
    
    result_list.append(result)

print(max(result_list))

