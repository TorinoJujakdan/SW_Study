from collections import deque
# 8방위 델타배열
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1 , -1, -1]

def in_range(y, x):
    return 0 <= y < h and 0 <= x < w

def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.popleft()

        for i in range(8):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx) and not visited[ny][nx] and arr[ny][nx] == 1:
                visited[ny][nx] = 1
                q.append((ny, nx))
    


while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    else:
        arr = [list(map(int, input().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
    
        cnt = 0
        for i in range(h):
            for j in range(w):
                if in_range(i, j) and not visited[i][j] and arr[i][j] == 1:
                    visited[i][j] = 1
                    bfs(i, j)
                    cnt += 1

    print(cnt)
