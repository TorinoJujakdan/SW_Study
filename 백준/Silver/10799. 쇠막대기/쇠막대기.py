from collections import deque

# ( 괄호앞에 연속되지 않고 ) 괄호면 - 파이프 새로 쌓는 행위 : total += 1
# ( 괄호앞에 ) 괄호면 - 레이저로 절단 : total += 쌓인 파이프개수만큼
# 괄호가 끝나면 끄트머리 개수 더해주기 : total += 1

arr = input()
q = deque()
total = 0

for i in range(len(arr)):
    if arr[i] == "(": # 파이프 혹은 레이저 이니 넣기
        q.append(arr[i])
    elif arr[i] == ")":
        if arr[i-1] == "(": # 레이저인 경우
            q.pop()
            total += len(q)
        else: # 끄트머리인 경우
            q.pop()
            total += 1

print(total)