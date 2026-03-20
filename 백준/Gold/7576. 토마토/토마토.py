from collections import deque

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 델타배열
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

# bfs 인데 다중 탐색을 해야함
# 전역에서 큐를 하나만 생성

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))


while q:
    cy, cx = q.popleft()

    for i in range(4):
        ny, nx = cy + dy[i], cx + dx[i]

        if in_range(ny, nx) and arr[ny][nx] == 0:
            arr[ny][nx] = arr[cy][cx] + 1
            q.append((ny, nx))

# 결과 확인
max_day = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(-1)
            exit()
        max_day = max(max_day, arr[i][j])

print(max_day - 1)