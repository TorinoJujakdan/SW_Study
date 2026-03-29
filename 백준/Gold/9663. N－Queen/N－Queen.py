n = int(input())

# 가능한 정답 수 
# 방문 기록 탐색
# 대각선 고려

ans = 0

v1 = [False] * n # 열확인용
v2 = [False] * (n*2) # 우측대각선 확인용
v3 = [False] * (n*2) # 좌측대각선 확인용

def recur(row):
    global ans

    if row == n:
        ans += 1
        return
    
    for col in range(n):
        # 가지치기
        # 퀸의 경로에 이미 있다면
        if v1[col] or v2[row + col] or v3[row - col + n]:
            continue
        # 상태 기록
        v1[col] = True
        v2[row + col] = True
        v3[row - col + n] = True

        recur(row + 1)
        # 상태 초기화
        v1[col] = False
        v2[row + col] = False
        v3[row - col + n] = False

recur(0)
print(ans)