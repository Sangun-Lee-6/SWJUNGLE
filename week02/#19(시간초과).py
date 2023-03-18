import sys
import copy
from collections import deque

def Histogram_area(N, input_list, h_stack) :
    
    if N == 1:
        
        
        # sz = min(h_stack) * N
        sz = input_list[0]
        sz_list.append(sz)
        return
    
    else :
                
        for n in range(N,0,-1):      # N 에서 1까지 역순으로 숫자 생성
            
            sz = min(h_stack) * n
          
            sz_list.append(sz)
            h_stack.pop()


        input_list.pop()
        h_stack = list(reversed(input_list))
        return Histogram_area(N-1, input_list, h_stack)

while True :
    
    input_list = list(map(int, sys.stdin.readline().split()))

    N = input_list[0]
    input_list = input_list[1:]

    if N ==0:
      exit(0)

    sz_list = []
    h_stack = list(reversed(input_list))

    Histogram_area(N, input_list, h_stack)

    print(max(sz_list))