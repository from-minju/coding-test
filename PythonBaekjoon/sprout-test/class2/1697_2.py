#1697. 숨바꼭질
#큐에 누적 초를 함께 넣는 경우 :  q.append(현재위치, 누적 초)
#1697.py이 더 효율적인 방법임. 1697_2는 다르게구현된코드로만 참고.

from collections import deque

n, k = map(int, input().split())

#움직일 수 있는 최대 좌표는 100000
max = 100000

# 해당위치에 도착했을 때 시간을 표시하는 리스트
visited = [0] * (max + 1)

def bfs():
    q = deque()
    q.append((n, 0))
    while q:
        x, cnt = q.popleft()
        if x == k:
            print(cnt)
            break
        for j in (x-1, x+1, x*2):
            # 주어진 범위 내에 있고 아직 방문하지 않았다면
            if 0<= j <= max and not visited[j]:
                visited[j] = 1
                q.append((j, cnt+1))

bfs()