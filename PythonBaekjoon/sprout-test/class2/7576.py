# 토마토


from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m,n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

# 큐에 맨 처음 입력받은 토마토의 위치 좌표를 append()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))


def bfs():

    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0<= tx < n and 0<= ty < m and graph[tx][ty]==0:
                q.append((tx,ty))
                # 일 수를 좌표값에 저장한다.
                graph[tx][ty] = graph[x][y] + 1

# 토마토 익히기
bfs()

# 정답이 담길 변수
result = 0

# 아직도 익지 않은 토마토가 있는지 탐색
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        # 최댓값이 정답이다.
        result = max(result, graph[i][j])

# 처음시작을 1일에서 시작해 +1해나갔으므로 -1해준다.
print(result-1)
