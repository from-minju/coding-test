# 귤고르기

from collections import Counter
def solution(k, tangerine):

    answer = 0

    counter = Counter(tangerine) # 개수 세기

    for i in sorted(counter.values(), reverse=True):
       k -= i
       answer += 1
       if k <= 0:
           break

    return answer



k = int(input())
tangerine = list(map(int, input().split(', ')))
print(solution(k, tangerine))