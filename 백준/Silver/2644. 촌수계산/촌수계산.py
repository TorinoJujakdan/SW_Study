n = int(input())
a, b = map(int, input().split())
m = int(input()) # 노드 개수
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split()) # 인접 그래프
    graph[x].append(y)
    graph[y].append(x)

# dfs 방식으로 풀어보기
def dfs(graph, v, depth):
    global ans
    visited[v] = True
    
    if v == b:
        ans = depth
        return
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, depth + 1)
            

visited = [False] * (n+1)
ans = -1

dfs(graph, a, 0)
print(ans)

