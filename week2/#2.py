def Cut_trees(list, low, high):
    
    if low > high :
        
        return 0
    
    else : 
        
        mid = (low+high)//2

        sum_branches = 0
        for tree in trees_list:

          if (tree - list[mid]) > 0:
              sum_branches += (tree - list[mid])
        
        if sum_branches == M:
            return list[mid]
        
        elif sum_branches < M :
            
            Cut_trees(list, low, mid-1)
        
        elif sum_branches > M:
            Cut_trees(list, mid+1, high)


import sys


N, M = map(int, sys.stdin.readline().split())

trees_list = list(map(int, sys.stdin.readline().split()))

max_tree = max(trees_list)    # 가장 큰 나무
lst = list(range(1, max_tree+1))      # 1 ~ 가장 큰 나무의 길이까지 list

print(Cut_trees(lst, 0, len(lst)))