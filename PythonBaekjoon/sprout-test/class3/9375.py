# 패션왕 신해빈

from collections import Counter

t = int(input())

for _ in range(t):

    n = int(input())
    kindl = []
    for i in range(n):
        name,kind = input().split()
        kindl.append(kind)
    kindd = dict(Counter(kindl))

    answer = 1
    for i in kindd.values():
        answer *= (i+1)
    
    print(answer-1)
        