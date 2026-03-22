class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# 전위 순회
def preorder(node):
    if node:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)

# 중위 순회
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end="")
        inorder(node.right)

# 후위 순회
def postoerder(node):
    if node:
        postoerder(node.left)
        postoerder(node.right)
        print(node.data, end="")

n = int(input())

# 이진 트리 생성
tree = {}

for i in range(n):
    data, left, right = input().split()
    # 트리에 해당 노드가 없으면 추가
    if data not in tree:
        tree[data] = Node(data)
    

    # 왼쪽 자식이 있다면
    if left != ".":
        tree[left] = Node(left)
        tree[data].left = tree[left]
    
    # 오른쪽 자식이 있다면
    if right != ".":
        tree[right] = Node(right)
        tree[data].right = tree[right]

root = tree["A"]
preorder(root)
print()
inorder(root)
print()
postoerder(root)