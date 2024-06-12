dx = [-1,1,0,0]
dy = [0,0,-1,1]

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = 0

def check():
	for i in range(N):
		for j in range(N):
			if graph[i][j] != 0:
				return False
	return True


while True:	
	temp = [arr[:] for arr in graph]
	for x in range(N):
		for y in range(N):
			# 아직 물들지 않은 곳이면
			if graph[x][y] != 0:
				cnt = 0 
				# 상하좌우에 0인곳 있는지 탐색
				for d in range(4):
					tx = x + dx[d]
					ty = y + dy[d]
					if 0<= tx <N and 0<= ty < N and graph[tx][ty]==0:
						cnt += 1	
				if cnt > temp[x][y]:
					temp[x][y]=0
				else:
					temp[x][y] -= cnt
	
	if check():
		break
	else:
		graph = [arr[:] for arr in temp]
		result += 1
		
			
print(result)
	
