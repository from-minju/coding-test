# 귤고르기

from collections import Counter
def solution(k, tangerine):
    # 요소의 개수가 많은 순서대로 정렬
    counter = Counter(tangerine).most_common()

    print(counter)
    total=0
    answer = 0

    for i in counter:
        total += i[1] # 귤의 개수를 더한다.
        answer += 1 # 귤의 종류를 더한다.
        if total >= k: # 필요한 귤의 개수보다 많거나 같다면 
            break

    return answer



k = int(input())
tangerine = list(map(int, input().split(', ')))
print(solution(k, tangerine))