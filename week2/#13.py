import sys

N = int(sys.stdin.readline())

for i in range(N):
    
    stack = []

    input = sys.stdin.readline().rstrip()

    for c in input:
        
        if c == '(':
            stack.append(c)
        
        elif c ==')':
            
            if len(stack) ==0:
                stack.append(c)
                break
            else : 
                stack.pop()
    if len(stack) ==0:
        print('YES')
    else :
        print('NO')
            


