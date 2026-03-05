n = int(input())
arr = list(map(int, input().split()))

min_total = 100000000000000
for i in range(n):
    arr2 = arr[:]
    arr2.pop(i)
    for j in range(n-1):
        total = 0
        arr3 = arr2[:]
        arr3[j] = arr2[j] * 2
        for k in range(n-2):
            total += abs(arr3[k+1] - arr3[k])
        if min_total > total:
            min_total = total

print(min_total)