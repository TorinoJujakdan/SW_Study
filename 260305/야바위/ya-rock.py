n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)

# Please write your code here.

max_point = 0
for i in range(1, 4):
    cup = [[0,0], [1, 0], [2, 0], [3, 0]] # 컵 매번 초기화
    cup[i][1] = 1 #각각의 경우에 공을 어떤 종이컵에 넣을지 지정
    cnt = 0 # 각각의 경우에 최대 점수를 확인해야함
    for j in range(n):
        cup[a[j]][1], cup[b[j]][1] = cup[b[j]][1], cup[a[j]][1]
        if cup[c[j]][1] == 1:
            cnt += 1
    if cnt > max_point:
        max_point = cnt

print(max_point)
