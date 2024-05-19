# 2606. 바이러스 - dfs/인접행렬

cnum = int(input())
rnum = int(input())

graph = [[0] * (cnum+1) for _ in range(cnum+1)]
visited = [0] * (cnum+1)

for _ in range(rnum):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

result = 0 

def dfs(x):
    global result

    visited[x] = 1
    for i in range(1, cnum+1):
        if graph[x][i] == 1 and visited[i] == 0:
            result += 1
            dfs(i)


dfs(1)
print(result)
    

