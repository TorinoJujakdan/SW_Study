from collections import deque

n = int(input())
m = int(input())

# 인접 리스트
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) # 양방향 그래프

# # bfs
def bfs(start_node):
    # 초기화
    q = deque([start_node])
    visited = [False] * (n + 1) # 정점 만큼 방문 여부 확인
    visited[start_node] = True

    cnt = 0 #1과 연결되어있는 정점 개수 카운트 변수

    while q:
        cur = q.popleft()

        # 방문한 시점은 q 에서 꺼낸 시점이라 여기서 +1
        cnt += 1

        # 노드들을 순회
        for next_node in graph[cur]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
        
    return cnt - 1
    
print(bfs(1))