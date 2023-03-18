import sys

N = int(sys.stdin.readline())

stack = []

for i in range(N):
    
    bar = int(sys.stdin.readline())
    
    while True:
        
        if len(stack) ==0:
          stack.append(bar)
          break
        
        if bar >= stack[-1]:
            stack.pop()
        else :
            stack.append(bar)
            break

print(len(stack))

