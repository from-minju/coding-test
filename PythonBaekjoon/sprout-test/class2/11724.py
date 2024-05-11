# 11724. 연결요소의 개수

import sys
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
# graph = [[[0] for _ in range(n+1)] for _ in range(n+1)]

cnt = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs(x):
    #노드 x에 인접한 노드 탐색
    for i in range(1, n+1):
        if graph[x][i]==1 and graph[i][i]==0:
            graph[i][i] = 1
            dfs(i)


for i in range(1, n+1):
    if graph[i][i] == 0:
        dfs(i)
        cnt += 1


print(cnt)


