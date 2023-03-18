import sys

N = int(sys.stdin.readline())

tree = {}
for i in range(N):
    
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

def preorder(root):
    
    if root != '.':

    # 만약 root 가 비어 있지 않다면 if 문 실행
    # root 가 비어있다면 root 로 '.' 이 들어와도 아무것도 실행되지 않음

    # 전위 순회는 root 노드를 먼저 방문
    # ∴ print 뒤에 함수 2개가 연속으로 나오는 것
        
        print(root, end='')
        preorder(tree[root][0])   # left
        preorder(tree[root][1])   # right

def inorder(root):
    
    if root != '.':
        
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    
    if root != '.':
        
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')