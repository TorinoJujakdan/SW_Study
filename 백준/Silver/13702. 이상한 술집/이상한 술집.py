n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

def check(mid):
    total = 0
    for i in range(n):
        total += arr[i] // mid
    
    return total

def binary_search():
    left = 1
    right = max(arr)
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid) >= k:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1 
    return ans

print(binary_search())