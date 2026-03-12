def recur(cnt):
    if cnt == m:
        print(*path)
        return
    for i in range(n):
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()
        

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []

recur(0)