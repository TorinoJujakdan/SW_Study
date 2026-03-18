from collections import deque

m, n, k = map(int, input().split())

arr = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

visited = [[False] * n for _ in range(m)]

def in_range(y, x):
    return 0 <= y < m and 0 <= x < n

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    area = 1


    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx):
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    area += 1
    return area

result = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            result.append(bfs(i, j))
            

print(len(result))
print(*sorted(result))