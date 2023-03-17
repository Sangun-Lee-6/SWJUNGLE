# GPT 가 고쳐준 코드

# 이 코드의 시간 복잡도는 O(N^2)입니다. 이는 Histogram_area 함수 내부의 for 루프에서 N에서 1까지 역순으로 반복하며, 각 반복마다 h_stack의 최솟값을 찾고 리스트에 추가하므로 O(N^2)입니다.

# 시간 복잡도를 줄이려면, h_stack에서 최솟값을 찾을 때마다 모든 요소를 검색하지 말고, 스택에서 빼낸 요소와 새로운 요소를 비교하여 스택에서 빼낸 요소보다 작은 경우에만 새로운 요소를 넣으면 됩니다. 또한, 입력 리스트를 역순으로 바꾸는 대신에 스택을 이용하여 바로 뒤에 있는 요소와 비교하면서 반복하면 더욱 빠른 시간에 해결할 수 있습니다.

import sys
import copy
from collections import deque

def Histogram_area(N, input_list) :
    sz_list = []
    h_stack = []

    for i in range(N):
        while h_stack and input_list[h_stack[-1]] > input_list[i]:
            j = h_stack.pop()
            if h_stack:
                sz = (i - h_stack[-1] - 1) * input_list[j]
            else:
                sz = i * input_list[j]
            sz_list.append(sz)
        h_stack.append(i)

    while h_stack:
        j = h_stack.pop()
        if h_stack:
            sz = (N - h_stack[-1] - 1) * input_list[j]
        else:
            sz = N * input_list[j]
        sz_list.append(sz)

    return max(sz_list)

while True:
    input_list = list(map(int, sys.stdin.readline().split()))

    N = input_list[0]
    input_list = input_list[1:]

    if N == 0:
        exit(0)

    print(Histogram_area(N, input_list))
