def recur(cnt):
    if cnt == m:
        print(*path)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            recur(cnt + 1)
            path.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
visited = [False] * n

recur(0)
