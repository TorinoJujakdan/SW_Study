import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
used = [0] * (N + 1)

def nm(idx, path):
    if idx == N + 1:
        if len(path) == M:
            print(*path[:])
        return
    
    nm(idx + 1, path + [idx])
    nm(idx + 1, path)

nm(1, [])