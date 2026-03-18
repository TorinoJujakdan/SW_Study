from collections import deque

def in_range(y, x):
    return 0 <= y < l and 0 <= x < l

def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        cy, cx = q.popleft()

        if cy == ty and cx == tx:
            return
        
        for i in range(8):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx) and visited[ny][nx] == 0:
                visited[ny][nx] = visited[cy][cx] + 1 
                q.append((ny, nx))
            

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]

T = int(input())

for i in range(T):
    l = int(input())
    y, x = map(int, input().split())
    ty, tx = map(int, input().split())
    visited = [[0] * l for _ in range(l)]

    bfs(y, x)
    print(visited[ty][tx])
    