#1697. 숨바꼭질

'''
bfs

- n, k 입력받기
- dfs함수 
- 함수 실행 및 출력
'''

from collections import deque

n, k = map(int, input().split())

#움직일 수 있는 최대 좌표는 100000
max = 100000

# 해당위치에 도착했을 때 시간을 표시하는 리스트
visited = [0] * (max + 1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1, x+1, x*2):
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0<= j <= max and not visited[j]:
                visited[j] = visited[x] + 1
                q.append(j)

bfs()


# from collections import deque

# n, k = map(int, input().split())

# def dfs(n):
#     q = deque()
#     q.append((n, 0)) #시작점 N, 시간

#     tx = n
#     sec = 0

#     while tx != k: #tx == k

#         x, sec = q.popleft()
#         move = [1, -1, x]
        
#         for i in move:
#             tx = x + i #이동했을때의 점
#             q.append((tx, sec+1))
#             if tx == k: break
    
#     return sec+1

# print(dfs(n))

        
    
            




