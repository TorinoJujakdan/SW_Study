n, m = map(int, input().split())
path = []
def recur(cnt):
    if cnt == m:
        print(*path)
        return
    for i in range(1, n+1):
        path.append(i)
        recur(cnt + 1)
        path.pop()

recur(0)