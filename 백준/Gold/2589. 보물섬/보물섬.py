from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < r and 0 <= x < c

def bfs(y, x, dis):
    visited = [[False] * c for _ in range(r)]
    q = deque()
    q.append((y, x, dis))
    visited[y][x] = True
    max_dis = 0

    while q:
        cy, cx, dis = q.popleft()
        if dis > max_dis:
            max_dis = dis

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx) and not visited[ny][nx] and arr[ny][nx] == "L":
                visited[ny][nx] = True
                q.append((ny, nx, dis + 1))

    return max_dis

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

result = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == "L":
            cnt = 0
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if in_range(ni, nj) and arr[ni][nj] == "L":
                    cnt += 1

            if cnt >= 3:
                continue

            result = max(result, bfs(i, j, 0))

print(result)
