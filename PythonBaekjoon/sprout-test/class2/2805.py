# 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2

    #잘랐을 때 가져갈 수 있는 나무의 길이 계산
    length = 0
    for i in trees:
        if i > mid:
            length += i - mid
        
    if length >= m : #필요 이상의 나무길이
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)