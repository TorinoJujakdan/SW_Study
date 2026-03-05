X, Y = map(int, input().split())

# Please write your code here.

def total(num):
    num = list(str(num))
    sum = 0
    for i in range(len(num)):
        sum += int(num[i])
    return sum

max_sum = 0
for i in range(X, Y+1):
    if max_sum < total(i):
        max_sum = total(i)

print(max_sum)
