def solution(start, end):
    
    if start > end:
        return
    div = end+1

    for i in range(start + 1, end + 1):  # list 의 두번째 원소부터 끝까지
        if tree[start] < tree[i]:       # tree[start] 는 루트노드 ∴ 루트 노드보다 큰 원소값이 있다면 if 문 실행
            
            div = i
            break
            # 루트 노드보다 큰 값을 찾으면 break
            # 루트 노드보다 큰 값은 오른쪽 서브 트리의 루트 노드
    solution(start +1, div -1)    # 왼쪽 서브 트리를 solution 함수에 넣기
    solution(div, end)      # 오른쪽 서브 트리를 solution 함수에 넣기
    print(tree[start])
    
    # solution 함수 2개 밑에 print(루트노드)
    # → ∵ 후위 순회값을 출력해야하므로
            


import sys
sys.setrecursionlimit(10**9)

tree = []
count = 0
while count <= 10000:
    
    try:
        temp = int(sys.stdin.readline())
    except :
        break
    
    tree.append(temp)
    count += 1

solution(0, len(tree)-1)
