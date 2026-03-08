k = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(k)]

def recur(start, end, depth):
    # 종료 조건 : 범위를 벗어나면
    if start > end:
        return
    # 중간 인덱스를 찾아 루트로 지정
    mid = (start + end) // 2

    # 현재 깊이의 리스트에 루트 값 추가
    tree[depth].append(arr[mid])

    # 왼쪽 서브 트리 재귀 호출
    recur(start, mid-1, depth+1)
    # 오른쪽 서브 트리 재귀 호출
    recur(mid+1, end, depth+1)

# 전체 배열 범위로 함수 시작
recur(0, len(arr)-1, 0)

# 각 깊이별로 결과 출력
for level in tree:
    print(*level)