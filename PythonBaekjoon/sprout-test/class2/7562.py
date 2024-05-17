# 나이트의 이동

from collections import deque

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(a, b, c, d):
    q = deque()
    #시작위치 방문처리
    graph[a][b] = 1
    q.append((a, b))

    while q :
        x, y = q.popleft()

        # 목적지에 도달하면 bfs()종료
        if x == c and y == d:
            break

        # 이동하기
        for i in range(8):
            # 이동했을 때의 위치
            tx = x + dx[i]
            ty = y + dy[i]

            # 그래프의 범위 내에 있지 않다면
            if tx<0 or tx>=I or ty<0 or ty>=I:
                continue

            # 방문하지 않은 곳이라면
            if graph[tx][ty] == 0:
                graph[tx][ty] = graph[x][y] + 1
                q.append((tx, ty))                
        

# 테스트케이스 개수
T = int(input())

for _ in range(T):

    #그래프 생성
    I = int(input())
    graph = [[0] * I for _ in range(I)]

    # 현재위치 (a,b)
    a, b = map(int, input().split())
    # 목표위치 (c, d)
    c, d = map(int, input().split())

    # bfs탐색
    bfs(a, b, c, d)

    # 현재위치에서 1부터 시작했으므로 1을 빼주어야 한다.
    print(graph[c][d] - 1)

