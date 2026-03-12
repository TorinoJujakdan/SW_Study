from collections import deque


n = int(input())
graph = [[] for _ in range(n + 1)]
parents = [0] * (n+1)

# 인접 리스트
for _ in range(n-1):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    q = deque([start])
    parents[start] = -1

    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if parents[next_node] == 0:
                parents[next_node] = now
                q.append(next_node)

bfs(1)
for i in range(2, n + 1):
    print(parents[i])