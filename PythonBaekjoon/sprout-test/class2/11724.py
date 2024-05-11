# 11724. 연결요소의 개수

n, m = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

def dfs():
    pass

for i in range(1, n+1):
    pass