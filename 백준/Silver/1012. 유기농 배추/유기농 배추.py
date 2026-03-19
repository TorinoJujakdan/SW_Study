from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    
    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx) and arr[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx))

            

T = int(input())
for tc in range(T):
    m, n, k = map(int, input().split())

    arr = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        arr[b][a] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j] and in_range(i, j):
                visited[i][j] = True
                bfs(i, j)
                cnt += 1
    
    print(cnt)