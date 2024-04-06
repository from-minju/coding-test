# 숫자 카드 게임

n, m = map(int, input().split())
data = []
data2 = []
for i in range(n):
    data.append(list(map(int, input().split())))
    data[i].sort()
    data2.append(data[i][0])
data2.sort()
print(data2[-1])