import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 전위순회한 값들이 주어짐 (루트 - 좌 - 우)
# 루트 노드보다 큰 수가 나오면 좌 서브 트리와 우 서브 트리 나누는 지점
# 이를 활용해 후위 순회

# 전위 순회 입력 받기
preorder = []
# 입력 받기 - 새로 알게 됨
while True:
    try:
        node = int(input())
        preorder.append(node)
    except:
        break

# 후위 순회
def postorder(s, e):
    # 종료 시점
    if s > e:
        return

    mid = e + 1
    for i in range(s+1, e+1):
        if preorder[i] > preorder[s]:
            mid = i
            break

    postorder(s+1, mid-1)
    postorder(mid, e)
    print(preorder[s])

postorder(0, len(preorder)-1)