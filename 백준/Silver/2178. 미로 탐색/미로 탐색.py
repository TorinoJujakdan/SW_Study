from collections import deque

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True

    while q:
        cy, cx = q.popleft()
        if cy == n - 1 and cx == m - 1:
            return arr[cy][cx]
        
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx):
                if arr[ny][nx] == 1:
                    arr[ny][nx] = arr[cy][cx] + 1
                    q.append((ny, nx))


n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

print(bfs(0, 0))
