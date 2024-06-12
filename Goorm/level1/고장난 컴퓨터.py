N, c = map(int, input().split())
sec = list(map(int, input().split()))

cnt = 1

for i in range(1, N):
	if abs(sec[i] - sec[i-1]) > c:
		cnt = 1
	else:
		cnt += 1

print(cnt)