from collections import deque
import copy

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 델타 배열 기본 세팅
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < n and 0 <= x < m

# bfs
def bfs(y, x, li):
    q = deque()
    q.append((y, x))
    li[y][x] = 2

    while q:
        cy, cx = q.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if in_range(ny, nx) and li[ny][nx] == 0:
                li[ny][nx] = 2
                q.append((ny, nx))

virus = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append([i, j])

empty = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            empty.append([i, j])


ans = 0
# 3가지 경우 만들기
def recur(cnt, prev):
    global ans
    if cnt == 3:
        check_arr = copy.deepcopy(arr)

        for y, x in virus:
            bfs(y, x, check_arr)
        
        safe_count = 0

        for i in range(n):
            for j in range(m):
                if check_arr[i][j] == 0:
                    safe_count += 1
        ans = max(ans, safe_count)
        return
    
    for i in range(prev, len(empty)):
        [r, c] = empty[i]
        arr[r][c] = 1
        recur(cnt + 1, i+1)
        arr[r][c] = 0

recur(0, 0)
print(ans)