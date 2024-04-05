# 랜선 자르기

K, N = map(int, input().split())
already = []

for _ in range(K):
    already.append(int(input()))

total = sum(already)

for x in range(int(total//N), 1, -1):
    sum = 0
    for i in already:
        sum += int(i//x)
        if sum>=N:
            print(x)
            break
    if sum>=N: break

