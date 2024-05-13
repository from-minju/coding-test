# 11724. 연결요소의 개수 - DFS, 인접행렬
# 맞았습니다!

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
result = 0


def dfs(v):
    for i in range(1, n+1):
        if graph[v][i] == 1 and not visited[i]:
            visited[i] = True
            dfs(i)


for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)


