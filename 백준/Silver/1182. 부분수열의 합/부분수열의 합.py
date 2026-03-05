n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def recur(idx, total,cnt_visited):
    global cnt
    # 1. 종료 조건
    # 모든 원소를 다고려했을때
    if idx == n:
        if total == s and cnt_visited !=0:
            cnt += 1
        return
    # 2. 현재 idx의 숫자를 포함하지 않음
    recur(idx+1, total, cnt_visited)
    # 3. 현재 idx의 숫자를 포함함
    recur(idx+1, total + arr[idx], cnt_visited + 1)

recur(0, 0, 0)
print(cnt)    

    