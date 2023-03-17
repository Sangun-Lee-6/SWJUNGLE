import sys

def Stack_order(order):

    if order == 'pop':

        if len(stack) ==0:
            print(-1)
        else :
            data = stack.pop()
            print(data)
    
    elif order =='size':

        print(len(stack))
    
    elif order =='empty':

        if len(stack) ==0:
            print(1)
        else :
            print(0)
    
    elif order =='top':
        
        if len(stack)==0:
            print(-1)
        else :
            print(stack[-1])







N = int(sys.stdin.readline())

stack = []
for i in range(N):
    
    input_list = list(sys.stdin.readline().split())

    if len(input_list) == 2:

        x = input_list[1]
        stack.append(x)

    else :

        order = input_list[0]
        Stack_order(order)




