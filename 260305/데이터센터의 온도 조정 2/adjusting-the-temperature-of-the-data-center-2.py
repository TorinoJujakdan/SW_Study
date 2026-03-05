N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

max_range = 0
for i in range(N):
    if ranges[i][1] > max_range:
        max_range = ranges[i][1]

max_total = 0
for i in range(max_range + 2):
    total = 0
    for j in range(N):
        if i < ranges[j][0]: total += C
        elif i <= ranges[j][1] : total += G
        else: total += H
    if total > max_total:
        max_total = total
print(max_total)