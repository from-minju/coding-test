# 실전문제: [미로 탈출]

#1. 현재(시작)위치 방문처리 -> 여기선 무시. 어차피 오른쪽 아래로 이동하는것이기때문에 시작위치의 값이 변경되어도 상관없음.
#2. 큐에서 꺼내 상하좌우 탐색
#3. 방문하지 않은 경우, 방문처리하고 노드의값 이전+1
#4. 큐가 빌때까지 반복


from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
        
    return graph[n-1][m-1]


print(bfs(0,0))