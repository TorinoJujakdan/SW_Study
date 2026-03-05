import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1) # 방문 여부 확인을 위한 변수 생성

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) #방향없는 양방향 그래프

def bfs(start_node):
    q = deque([start_node]) # 큐 생성
    global visited
    visited[start_node] = True # 방문처리

    while q:
        c = q.popleft() # 방문하는 곳 하나씩 탐색

        # 노드 순회
        for next_node in graph[c]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)


c_cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        c_cnt += 1

print(c_cnt)