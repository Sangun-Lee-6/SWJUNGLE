import sys

N = int(sys.stdin.readline())

input_list = list(map(int, sys.stdin.readline().split()))

top_stack = []
output = [0]*N

for n in range(N):
    
    top = input_list[n]
    while top_stack:
        
        if top_stack[-1][1] > top:
            output[n] = top_stack[-1][0] + 1
            break
        top_stack.pop()
    
    top_stack.append((n, top))

            
top_stack.append((n, top))
print(*output)
    
    