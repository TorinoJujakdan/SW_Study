n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

min_w = 1600000001
for i in range(n):
    subx = x[::]
    suby = y[::]
    subx.pop(i)
    suby.pop(i)
    subx.sort()
    suby.sort()
    w = abs(subx[-1] - subx[0]) * abs(suby[-1] - suby[0])
    if w < min_w:
        min_w = w
    
print(min(min_w, w))