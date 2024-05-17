# 토마토
# 틀린 코드

from collections import deque
graph = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m,n = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(a, b):
    q = deque()
    depth = 0
    q.append((a,b,depth))
    graph[a][b] = 2

    while q:
        x, y, depth = q.popleft()

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0<= tx < n and 0<= ty < m and graph[tx][ty]==0:
                q.append((tx,ty,depth + 1))
                graph[tx][ty] = 2
    
    return depth


days = 0

for i in range(n):
    for j in range(m):

        if graph[i][j] == 1:
            tdays = bfs(i,j)
            days = max(tdays, days)


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            days = -1
            break
    
    if days == -1: break

print(days)
