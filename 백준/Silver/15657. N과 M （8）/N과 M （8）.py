def recur(cnt, prev):
    if cnt == m:
        print(*path)
        return

    for i in range(prev, n):
        path.append(arr[i])
        recur(cnt + 1, i)
        path.pop()
    

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []

recur(0, 0)