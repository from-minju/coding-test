# 1260. DFS와 BFS
'''
1. 입력값 받기
2. 그래프 선언
3. dfs
4. bfs
5. 함수실행
'''

from collections import deque

# n: 정점, m: 간선, v: 시작정점
n, m, v = map(int, input().split())

graph = [[False]*(n+1) for _ in range(n+1)]

visited1 = [False] * (n+1)
visited2 = [False] * (n+1)


for _ in range(m): #간선의개수만큼 입력받음
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    #시작정점 방문처리
    visited1[v] = True
    print(v, end=' ')
    #방문하지 않은 인접노드 탐색
    for i in range(1, n+1):
        if graph[v][i]==1 and not visited1[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited2[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i]==1:
                q.append(i)
                visited2[i] = True


dfs(v)
print()
bfs(v)