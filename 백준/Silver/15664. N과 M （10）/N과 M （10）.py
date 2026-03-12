def recur(cnt, prev):
    if cnt == m:
        print(*path)
        return 
    last_num = 0
    for i in range(prev, n):
        if not visited[i] and arr[i] != last_num:
            visited[i] = True
            path.append(arr[i])
            last_num = arr[i]
            recur(cnt + 1, i)
            path.pop()
            visited[i] = False


n, m = map(int, input().split())
arr = list(map(int, input().split()))
path = []
arr.sort()
visited = [False] * n

recur(0, 0)