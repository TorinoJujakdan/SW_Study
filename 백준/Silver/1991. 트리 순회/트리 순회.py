class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(node):
    if node:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data, end="")
        inorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end="")

n = int(input())

tree = {}

for i in range(n):
    data, left, right = input().split()
    
    if data not in tree:
        tree[data] = Node(data)
    
    # 왼쪽 자식이 있다면
    if left != '.':
        tree[left] = Node(left)
        tree[data].left = tree[left]
    
    # 오른쪽 자식이 있다면
    if right != '.':
        tree[right] = Node(right)
        tree[data].right = tree[right]

root = tree['A']
preorder(root)
print()
inorder(root)
print()
postorder(root)
