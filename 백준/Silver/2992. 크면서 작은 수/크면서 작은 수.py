num = input()
n = len(num)
target = int(num)
visited = [False] * n
ans = []

def recur(number):
    # 종료 조건 : 모든 자리 다 고르면
    if len(number) == n:
        val = int(number)
        if val > target:
            ans.append(val)
        return
    
    # 재귀 시작 : 순열 생성하기
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            recur(number + num[i])
            visited[i] = False # 재귀돌고 원상복구

recur("")

if ans:
    print(min(ans))
else:
    print(0)