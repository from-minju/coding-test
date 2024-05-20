# 트럭 주차 
# 구현
# 난이도 : 쉬움

parked = [0] * 100
starttime = 1
lasttime = 1
result = 0

A, B, C = map(int, input().split())
for _ in range(3):
    x, y = map(int, input().split())
    for i in range(x, y): parked[i] += 1
    starttime = min(starttime, x)
    lasttime = max(lasttime, y)

for i in parked[starttime:lasttime]:
    if i == 1: result += A
    elif i == 2: result += 2*B
    elif i == 3: result += 3*C

print(result)
