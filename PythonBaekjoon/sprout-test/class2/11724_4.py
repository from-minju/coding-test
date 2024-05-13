# 11724. 연결요소의 개수 - DFS, 인접리스트
# 맞았습니다!

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
cnt = 0
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


for n in range(1, N + 1):    
    if not visited[n]:
        dfs(n)
        cnt += 1

print(cnt)