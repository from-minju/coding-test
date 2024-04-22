# 소수 찾기
#i가 자신인 i에 도달 후 나누어떨어진다면 그 수는 소수이므로 cnt+=1

n = int(input())
data = list(map(int, input().split()))
cnt = 0

for i in data:
    
    if i==1: 
        continue

    for j in range(2,i+1):
        if i%j==0: #소수가 아닌 경우
            if i == j: cnt+=1
            break


print(cnt)

