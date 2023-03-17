import sys

N = int(sys.stdin.readline())

input_list = []

for i in range(N):
    
    word = sys.stdin.readline().rstrip()
    input_list.append(word)


input_list = list(set(input_list))
input_list.sort()
input_list.sort(key=len)

print(*input_list, sep='\n')


# sort 를 하면 일단 사전순으로 나열되고
# 그 다음 sort(key = len) 으로 하면 나열됨
