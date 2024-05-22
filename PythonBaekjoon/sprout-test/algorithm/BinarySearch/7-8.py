# [실전문제] 떡볶이 떡 만들기 - 나의 코드

n, m = map(int, input().split())
array = list(map(int, input().split()))

# 얻을 수 있는 떡의 길이의 합
def calsum(h):
    global array
    total = 0
    for x in array:
        if (x-h) < 0:
            total += 0
        else:
            total += (x-h)
    return total

# 이진탐색
def binary_search(start, end):
    global m

    while start <= end:
        mid = (start + end) // 2

        if m == calsum(mid):
            return mid
        elif m < calsum(mid):
            start = mid + 1
        else:
            end = mid - 1
    
    return mid

print(binary_search(0, max(array)))


