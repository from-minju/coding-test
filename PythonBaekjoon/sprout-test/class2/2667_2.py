# 단지 번호 붙이기
# bfs

from collections import deque
import sys
sys.setrecursionlimit(10**7)

n = int(input())

graph = []
result = []
cnt = 0

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    global cnt
    q = deque()
    graph[x][y] = 0 #현재 위치 방문처리
    q.append((x,y))

    while q:
        a, b = q.popleft()
        cnt += 1

        for i in range(4):
            tx = a + dx[i]
            ty = b + dy[i]

            if 0<= tx < n and 0<= ty < n and graph[tx][ty]==1:
                q.append((tx, ty))
                graph[tx][ty] = 0
    


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            cnt = 0
            bfs(i, j)
            result.append(cnt)


result.sort()

print(len(result))

for num in result:
    print(num)