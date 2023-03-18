# x 의 위치를 찾아주는 함수

def Find_x_location(S, low, high):
    
    # S 는 리스트 / low, high 는 인덱스

    if (low>high):      # 절반씩 줄여나갈 때 mid 값을 수정하므로 값을 찾지 못한다면 index 가 뒤집힘 → 그 때는 검색을 종료해주는 코드
        
        return 0
    
    else :
        
        mid = (low + high) //2 

        # 만약 x == S[mid] 라면 그 값을 찾은 것
        if (x == S[mid]):
            return mid        # mid 는 인덱스이므로 x 의 위치를 반환
        
        elif (x<S[mid]) :     # x 가 S[mid] 보다 앞에 있다면
            return Find_x_location(S, low, mid-1)       # mid 이상은 버리고 다시 찾기
        
        elif (x > S[mid]):
            return Find_x_location(S, mid+1, high)      # mid 이하는 버리고 다시 찾기

import sys

print('Enter x :', end='')
x = int(sys.stdin.readline())

print('Enter S :', end='')
S = list(map(int, sys.stdin.readline().split()))

print('x의 index :', Find_x_location(S, 0, len(S)-1))