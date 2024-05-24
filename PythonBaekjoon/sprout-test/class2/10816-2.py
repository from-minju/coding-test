# 숫자 카드2 - 딕셔너리, 이분탐색

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

# 이진탐색 (가지고 있는 카드인지 확인하기 위한)
def binary_search(target):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if n[mid] == target:
            return dic.get(target)
        elif n[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return 0

# 출력
for i in m:
    print(binary_search(i), end= " ")