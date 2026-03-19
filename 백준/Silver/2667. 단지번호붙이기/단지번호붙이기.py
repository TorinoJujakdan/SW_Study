from collections import deque

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    q = deque()
    q.append((y, x))
    visited[y][x] = True
    apt = 1

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx) and not visited[ny][nx] and arr[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((ny, nx))
                apt += 1
    return apt

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

cnt = 0
li = []
for i in range(n):
    for j in range(n):
        if in_range(i, j) and arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            li.append(bfs(i, j))
            cnt += 1

print(cnt)
li.sort()
for i in range(len(li)):
    print(li[i])
