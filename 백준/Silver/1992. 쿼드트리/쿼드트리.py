n = int(input())
arr = [list(input().strip()) for _ in range(n)]

# 한 구역이 전부 같은 숫자(0, 1) 으로 이루어 지는지 확인
# 아니라면 괄호 출력 - ( 하고 4등분해서 재귀 호출해서 계속 확인 (Z문제 처럼)
# 맞다면 해당 숫자 출력

def recur(x, y, num):
    # 가장 첫번째 숫자와 구역내 숫자가 같으면
    first = arr[x][y]
    # 전체 탐색
    for i in range(x, x + num):
        for j in range(y, y + num):
            if arr[i][j] != first:
                # 다르면 4등분
                print("(", end="")
                half = num // 2

                # 순서대로 재귀 호출
                recur(x, y, half)
                recur(x, y + half, half)
                recur(x + half, y, half)
                recur(x + half, y + half, half)

                # 4등분 끝나면 바로 닫기
                print(")", end="")
                return
    # 모두 같으면 해당 숫자 뽑기
    print(first, end="")

recur(0, 0, n)