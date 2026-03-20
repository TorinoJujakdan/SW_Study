from collections import deque

m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# delta 배열
dz = [0, 0, 0, 0, 1, -1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, 1, 0, -1, 0, 0]

def in_range(z, y, x):
    return 0 <= z < h and 0 <= y < n and 0 <= x < m

q = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append((i, j, k))

while q:
    cz, cy, cx = q.popleft()

    for i in range(6):
        nz, ny, nx = cz + dz[i], cy + dy[i], cx + dx[i]

        if in_range(nz, ny, nx) and arr[nz][ny][nx] == 0:
            arr[nz][ny][nx] = arr[cz][cy][cx] + 1
            q.append((nz, ny, nx))

max_day = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                print(-1)
                exit()
            
            max_day = max(max_day, arr[i][j][k])

print(max_day - 1)