from collections import deque

n = int(input())
arr = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

# 적록색약 은 빨강 초록 구별 못함
# 일반인은 구별 가능

# bfs 돌려서 red, blue, green 각각 탐색하고 탐색했을때
# 같은 색깔이면 개수 세기
# 그럼 타겟 숫자가 항상 바뀌어야함
# 델타배열 써야함

# 상하좌우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

# 범위 지정 함수
def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

# bfs 설계
def bfs(y, x, blind):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    color = arr[y][x]

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if in_range(ny, nx) and not visited[ny][nx]:
                if not blind:
                    if arr[ny][nx] == color:
                        visited[ny][nx] = True
                        q.append((ny, nx))
                else:
                    if color == "B":
                        if arr[ny][nx] == "B":
                            visited[ny][nx] = True
                            q.append((ny, nx))
                    else:
                        if arr[ny][nx] == "R" or arr[ny][nx] == "G":
                            visited[ny][nx] = True
                            q.append((ny, nx))



total_reg = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j, False)
            total_reg += 1

visited = [[False] * n for _ in range(n)]

total_ireg = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            bfs(i, j, True)
            total_ireg += 1
    

print(total_reg, total_ireg)     