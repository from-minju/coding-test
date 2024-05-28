# 귤고르기

from collections import Counter
def solution(k, tangerine):
    # 요소의 개수가 많은 순서대로 정렬
    counter = Counter(tangerine)

    answer = 0

    for i in sorted(counter.values(), reverse=True):
       k -= i
       answer += 1
       if k <= 0:
           break

    return answer



k = int(input())
tangerine = list(map(int, input().split(', ')))
print(solution(k, tangerine))