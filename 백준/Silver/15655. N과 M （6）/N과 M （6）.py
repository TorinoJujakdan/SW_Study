def recur(cnt, prev):
    if cnt == m:
        print(*path)
        return
    for i in range(prev, n):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            recur(cnt + 1, i)
            path.pop()
            visited[i] = False

# 선택했던 뒤에 부분 같이 가져오기

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
visited = [False] * n
recur(0, 0)