# 유기농 배추
# bfs로 풀었을 때

#BFS
from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    maps[y][x] = 2 #방문처리

    while q:
        x, y = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            # maps의 범위 안에 있고 방문하지 않은 배추가 있으면
            if 0<=tx<=m-1 and 0<=ty<=n-1 and maps[ty][tx]==1:
                q.append((tx, ty))
                maps[ty][tx] = 2 #방문처리


#DFS
import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    maps[y][x] = 2 #방문처리

    for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            # maps의 범위 안에 있고 방문하지 않은 배추가 있으면
            if 0<=tx<=m-1 and 0<=ty<=n-1 and maps[ty][tx]==1:
                dfs(tx, ty)
                maps[ty][tx] = 2 #방문처리




# t: 테스트케이스개수
t = int(input())

#상하좌우
dx = [0, 0, -1, 1] #가로/열
dy = [-1, 1, 0, 0] #세로/행

for _ in range(t):
        
    # m:가로/열, n:세로/행, k:배추개수
    m, n, k = map(int, input().split())

    cnt = 0
    location = []
    maps = [[0] * m for _ in range(n)] #2차원리스트 초기화



    # 배추의 위치 입력받기
    for _ in range(k):
        x, y = map(int, input().split())
        location.append((x, y))
        maps[y][x] = 1


    # 배추위치마다 필요한 흰지렁이 개수 조사
    for x, y in location:
        if maps[y][x]==1:
            bfs(x, y) #dfs로 풀려면 dfs(tx, ty)해주면 됨.
            cnt += 1

    print(cnt)

