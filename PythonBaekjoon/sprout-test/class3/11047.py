# 동전 0

n, k = map(int, input().split())
worths = [int(input()) for _ in range(n)]
coin = 0

while k > 0:

    money = 1

    for i in worths:
        if i > k :
            break
        else:
            money = i
    
    coin += k//money
    k -= money * (k//money)

print(coin)
    