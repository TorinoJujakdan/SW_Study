n, m = map(int, input().split())

path = []
visited = [False] * (n+1)
def recur(cnt):
    if cnt == m:
        print(*path)
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        path.append(i)
        recur(cnt + 1)
        path.pop()
        visited[i] = False

recur(0)