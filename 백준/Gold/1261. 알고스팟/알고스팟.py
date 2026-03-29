import heapq
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(m)]

# 다익스트라 구현 위해서 초기 값 아주 크게 설정
dis = [[1e10] * n for _ in range(m)]

# delta 북동남서, 범위 함수
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    return 0 <= y < m and 0 <= x < n

# 다익스트라 구현
# 비용, y좌표, x좌표 순서대로 입력 넣기
# 그래야 비용이 제일 작은 것을 자동으로 맨 앞에 넣음(트리 생각해보면 됨)
def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    dis[0][0] = 0 # 시작점의 벽 부순 횟수 0

    while q:
        cost, cy, cx = heapq.heappop(q) # 가장 적게 부순 비용과 좌표 꺼내기

        # 이미 더 적은 비용으로 방문한적이 있으면 무시
        if cost > dis[cy][cx]:
            continue
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 1. 나가는 경우 확인
            if not in_range(ny, nx):
                continue
            # 2. 현재까지의 비용 + 다음 칸의 벽 여부 계산
            # 이 값이 저장된 값보다 작다? 그럼 갱신
            if cost + arr[ny][nx] < dis[ny][nx]:
                dis[ny][nx] = cost + arr[ny][nx]
                # 갱신된 새로운 비용과 좌표를 다시 큐에 넣기
                heapq.heappush(q, (dis[ny][nx], ny, nx))

dijkstra()
# 목표 지점까지 부순 벽의 최소 개수 출력
print(dis[m-1][n-1])