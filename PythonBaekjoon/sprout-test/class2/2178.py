# 2178. 미로 탐색 (bfs)
'''
bfs는 시작지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색하므로.
'''

from collections import deque

n, m = map(int, input().split())

maps = []

dx = [-1, 0, 1, 0] #행
dy = [0, 1, 0, -1] #열

# nxm 미로 입력받기
for i in range(n):
    maps.append(list(map(int, input())))

def bfs(a,b):
    q = deque()
    q.append((a,b))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0<=tx<=n-1 and 0<=ty<=m-1: #이동했을 때의 위치가 maps의 범위 내에 있는지
                if maps[tx][ty]==1: #이동가능한 길인지, 방문하지 않은 곳인 경우
                    q.append((tx, ty))
                    maps[tx][ty] = maps[x][y] + 1

bfs(0,0)
print(maps[n-1][m-1])



# # -----
# # dfs로 잘못풀었음.
# n, m = map(int, input().split())

# maps = []

# # nxm 미로 입력받기
# for i in range(n):
#     maps.append(list(map(int, input())))

# dx = [0, 1, 0, -1] #행
# dy = [1, 0, -1, 0] #열

# result = 0

# def move(x, y, cnt):
#     global result 

#     maps[x][y] = 2 #시작 위치 방문처리
#     cnt += 1

#     for i in range(4):
#         tx = x + dx[i]
#         ty = y + dy[i]

#         if 0<=tx<=n-1 and 0<=ty<=m-1: #이동한 위치가 맵 범위 안에 있을 때
#             if maps[tx][ty]==1: #이동한 위치가 방문x and 이동가능
#                 if tx==n-1 and ty==m-1: #이동한 위치가 (n.m)이면
#                     cnt += 1
#                     result = cnt
#                     # print(cnt)
#                     break
#                 else: move(tx, ty, cnt)
    
        
# move(0,0,0)
# print(result)