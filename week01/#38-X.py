import sys
from itertools import permutations

N = int(sys.stdin.readline())

W = []
for i in range(N):
    
    lst = list(map(int, sys.stdin.readline().split()))
    W.append(lst)

city_list = list(range(N))


p_list = list(permutations(city_list, N))

cost_list = []

for path in p_list:
    
    cost = 0
    

    for i in range(len(path)):
        
        if path[i] == path[-1]:
            if W[i][0] ==0:
                break
            else :
                cost += W[i][0]
                break
            
        elif W[i][i+1] ==0:
            break
        
        cost += W[i][i+1]

    cost_list.append(cost)
    
print(min(cost_list))

  


