import sys

N = int(sys.stdin.readline())

input_list = list(map(int, sys.stdin.readline().split()))

top_stack = []
max_top_stack = []
output = []

for top in input_list:
    
    if len(top_stack) ==0:
        output.append(0)
        top_stack.append(top)
        max_top_stack.append(top)
        continue
    
    while True:
        
        if len(max_top_stack) ==0:
            output.append(0)
            max_top_stack.append(top)
            top_stack.append(top)
            break
        
        if top_stack[-1] < top:
            if max_top_stack[-1] < top:
                max_top_stack.pop()
            elif max_top_stack[-1] > top:
                received_top = max_top_stack[-1]
                output.append(top_stack.index(received_top)+1)
                top_stack.append(top)
                max_top_stack.append(top)
                break
                
        elif top_stack[-1] > top:
            received_top = top_stack[-1]
            output.append(top_stack.index(received_top)+1)
            top_stack.append(top)
            break

print(*output)
