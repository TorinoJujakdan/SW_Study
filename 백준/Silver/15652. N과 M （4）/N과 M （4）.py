n, m = map(int, input().split())
path = []

def recur(cnt, prev):
    if cnt == m:
        print(*path)
        return
    for i in range(prev, n+1):

        path.append(i)
        recur(cnt + 1, i)
        path.pop()
    

recur(0, 1)