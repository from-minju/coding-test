# 랜선 자르기
import sys

# 입력받기
k, n = map(int, input().split())
data = [int(sys.stdin.readline()) for _ in range(k)]

# 이분 탐색의 처음과 끝
start = 1
end = max(data)

# 만들 수 있는 랜선의 최대 길이를 찾는다.
while start <= end: # start > end가 될때까지 반복

    lan = 0 # 만들 수 있는 랜선의 개수 초기화
    mid = (start + end) // 2 # 이분탐색의 중간

    # mid길이로 랜선을 잘랐을 때 만들어지는 랜선의 개수 구하기
    for i in data:
        lan += i // mid
    
    if lan < n: # 잘린랜선의 개수가 부족한 경우 길이를 줄여본다.
        end = mid - 1
    else: # 만들어진 개수가 필요개수보다 더 크거나 같을때 랜선의 길이를 늘린다.
        result = mid
        start = mid + 1
        
print(end)

