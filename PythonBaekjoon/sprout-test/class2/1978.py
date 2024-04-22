# 소수 찾기 - 내 답
'''
소수 : 약수가 1과 자기자신인 수, 1제외
'''

n = int(input())
data = list(map(int, input().split()))
cnt = 0

for i in data:
    temp = 0

    if i==1: 
        continue

    for j in range(2,i):
        if i%j==0: #소수가 아닌 경우
            temp = 1
            break

    if temp==0:
        cnt += 1

print(cnt)

