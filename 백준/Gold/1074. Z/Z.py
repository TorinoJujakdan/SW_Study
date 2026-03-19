n, r, c = map(int, input().split())

def recur(n, r, c):
    if n == 0:
        return 0 # 탑 다운 형식으로 재귀
    
    half = 2**(n-1)
    
    if r < half and c < half:
        # 2사분면 : 그대로 축소되기 때문에 더하는 값 없음
        return recur(n-1, r, c)
    elif r >= half and c < half:
        # 3사분면 : 1, 2 사분면 더하고 난 뒤에 row 값만 절반이 빠져버림
        return 2 * (half * half) + recur(n-1, r-half, c)
    elif r < half and c >= half:
        # 1사분면 : 2사분면 더하고 난 뒤에 col 값만 절반이 빠져버림
        return (half * half) + recur(n-1, r, c-half)
    elif r >= half and c >= half:
        # 4사분면 : 1, 2, 3사분면 더하고 난 뒤에 둘다 절반씩 뺌
        return 3 * (half * half) + recur(n-1, r-half, c-half)

print(recur(n, r, c))
