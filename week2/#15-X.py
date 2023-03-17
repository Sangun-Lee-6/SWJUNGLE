import sys

bracket = sys.stdin.readline().rstrip()
length = len(bracket)       # 괄호의 개수
stack = []
tmp = 1
res = 0

for i in range(length):
    b = bracket[i]   
    if b == '(':
        tmp *= 2
        stack.append(b)
    elif b == '[':
        tmp *= 3
        stack.append(b)

    elif b == ')':
        if len(stack)==0 or stack[-1] == '[':
            res = 0
            break
        if bracket[i-1] == '(':
            res += tmp
        tmp //= 2
        stack.pop()  
    elif b ==']':
        if len(stack)==0 or stack[-1] == '(':       # 이러면 (] 가 되니까 Error
            res = 0
            break
    # [()]의 경우 ] 직전 문자가 )이므로 더하지 않고 넘어감
    # 단, 이 경우는 오류는 아님 >> 지금까지 계산한거 한번만 해주면 되기 때문에...
        if bracket[i-1] == '[':
            res += tmp
        tmp = tmp // 3
        stack.pop() 

if not len(stack)==0:           # if stack 에 뭐가 들어있으면 res = 0 으로 초기화(문제 조건에서 잘못된 괄호열은 0으로 출력하라고 명시됨)
    res = 0
print(res)