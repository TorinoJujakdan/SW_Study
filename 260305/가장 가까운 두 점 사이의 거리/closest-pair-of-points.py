n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

min_result = 1000001
for i in range(n-1):
    for j in range(i+1, n):
        result = (x[i] - x[j])**2 + (y[i] - y[j])**2 

        if result < min_result:
            min_result = result

print(min(min_result, result))