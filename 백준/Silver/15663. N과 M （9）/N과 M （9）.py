def recur(cnt):
    if cnt == m:
        print(*path)
        return
    last_num = 0
    for i in range(len(arr)):
        if not visited[i] and arr[i] != last_num:
            visited[i] = True
            path.append(arr[i])
            last_num = arr[i]
            recur(cnt+1)
            path.pop()
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
path = []
arr.sort()
visited = [False] * len(arr)
recur(0)