def Find_M_location(N_list, low, high):
    
    if (low>high):
        
        return 0
    
    else :
        
        mid = (low+high) // 2

        if M == N_list[mid]:
            
            return 1
        
        elif M > N_list[mid]:
            
            return Find_M_location(N_list, mid+1, high)
        
        elif M < N_list[mid]:
            
            return Find_M_location(N_list, low, mid-1)
        








import sys

N = int(sys.stdin.readline())

N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

num_M = int(sys.stdin.readline())

M_list = list(map(int, sys.stdin.readline().split()))

for M in M_list:
    
    print(Find_M_location(N_list, 0, len(N_list)-1))

