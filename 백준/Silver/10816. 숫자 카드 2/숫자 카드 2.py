n = int(input())
nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))

# counting 딕셔너리 초기화
di = {}
for num in nums1:
    if di.get(num):
        di[num] += 1
    else:
        di[num] = 1
# 카운팅 수 출력
for num in nums2:
    if di.get(num):
        print(di[num], end=' ')
    else:
        print(0, end=' ')