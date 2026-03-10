n, m = map(int, input().split())

path = []
visited = [False] * (n+1)
def recur(cnt, prev):
    if cnt == m:
        print(*path)
        return
    
    for i in range(prev, n+1):
        if visited[i]:
            continue
        visited[i] = True
        path.append(i)
        recur(cnt + 1, i)
        path.pop()
        visited[i] = False
recur(0, 1)