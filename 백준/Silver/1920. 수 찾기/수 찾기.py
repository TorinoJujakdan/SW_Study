n = int(input())
arr = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))
arr.sort()
def binary_search(num):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    return 0

for i in range(m):
    print(binary_search(target[i]))