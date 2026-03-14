n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n

def dfs(v):
    for i in range(n):
        if not visited[i] and arr[v][i] == 1:
            visited[i] = 1
            dfs(i)

for i in range(n):
    dfs(i)
    print(*visited)
    visited = [0] * n # 방문 초기화