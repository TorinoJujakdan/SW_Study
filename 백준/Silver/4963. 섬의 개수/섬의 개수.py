import sys
sys.setrecursionlimit(10**6)
# 8방위 델타배열
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1 , -1, -1]

def in_range(y, x):
    return 0 <= y < h and 0 <= x < w

def dfs(y, x):
    visited[y][x] = True

    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]

        if in_range(ny, nx) and arr[ny][nx] == 1 and not visited[ny][nx]:
            dfs(ny, nx)
        

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
                if arr[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    cnt += 1

    print(cnt)
