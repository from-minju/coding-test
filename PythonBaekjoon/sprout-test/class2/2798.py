# 블랙잭


n, m = map(int, input().split())
data = list(map(int, input().split()))
sum_list = []

for x in range(0, n-2):
    for y in range(x+1, n-1):
        for z in range(y+1, n):
            temp = data[x] + data[y] + data[z]
            if temp <= m:
                sum_list.append(temp)

sum_list.sort()
print(sum_list[-1])


'''
n장의 카드에서 3장을 뽑아
합이 m을 넘지 않으면서 m과 최대한 가깝게 만든다.
'''


'''
- n, m 입력받음.
- 카드에 쓰여있는 수 입력받음.
- 3중 for문
x [0] ~ [n-2]
y [x+1] ~ [n-1]
z [y+1] ~ [n]

'''