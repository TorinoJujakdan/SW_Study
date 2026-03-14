from collections import deque

def bfs(graph, start_node, visited):
    q = deque([start_node])
    visited[start_node] = True

    while q:
        curr = q.popleft()
        print(curr, end= " ")

        for next_node in graph[curr]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 양방향 그래퓨

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)