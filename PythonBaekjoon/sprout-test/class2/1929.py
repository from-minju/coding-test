# 1929. 소수 구하기

m, n = map(int, input().split())

for i in range(m, n+1): #m이상 n이하의 수 탐색
    #i가 소수인지 판별
    if i==1: continue
    for j in range(2, int(i**0.5) + 1): # 1~i-1까지 나누어봄
        if i % j == 0 : break #소수가 아님
    else: 
        print(i)a