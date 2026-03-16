def recur(cnt):
    if cnt == m:
        print(*path)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = 1
            path.append(i)
            recur(cnt + 1)
            path.pop()
            visited[i] = 0
n, m = map(int, input().split())
path = []
visited = [0] * (n+1)

recur(0)