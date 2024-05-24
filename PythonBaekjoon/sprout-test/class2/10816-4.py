# 숫자 카드2 - Counter

from collections import Counter

# 가지고 있는 카드
N = int(input())
n = list(map(int, input().split()))
n.sort() #이진탐색을 위해 정렬

# 몇 개 있는지 구해야 할 카드
M = int(input())
m = list(map(int, input().split()))

# 카드 수 세기
c = Counter(n)

# 출력
for i in m:
    if i in c:
        print(c[i], end = " ")
    else:
        print(0, end = " ")
