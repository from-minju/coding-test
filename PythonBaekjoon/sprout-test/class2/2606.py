# 2606. 바이러스 - bfs/인접행렬

from collections import deque

cnum = int(input())
rnum = int(input())

graph = [[0] * (cnum+1) for _ in range(cnum+1)]
visited = [0] * (cnum+1)

for _ in range(rnum):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def bfs() :
    result = 0

    q = deque()
    visited[1] = 1
    q.append(1)

    while q:
        x = q.popleft()

        for i in range(1, cnum + 1):
            if graph[x][i] == 1 and visited[i] == 0:
                visited[i] = 1
                result += 1
                q.append(i)
    
    print(result)

bfs()

    

