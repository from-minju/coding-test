# 숫자 카드2 - 딕셔너리 key로 조회

# 가지고 있는 카드
N = int(input())
n = list(map(int, input().split()))
n.sort() #이진탐색을 위해 정렬

# 몇 개 있는지 구해야 할 카드
M = int(input())
m = list(map(int, input().split()))

# 딕셔너리 생성 {카드번호:개수}
dic = {}
for i in n:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 출력
for i in m:
    if i in dic: #가지고 있는 카드라면
        print(dic[i], end=" ") #개수(value) 출력
    else: #가지고 있지 않다면
        print(0, end=" ") #0을 출력