# 숫자 카드2 - 나의 코드
# 시간초과

# 가지고 있는 카드
N = int(input())
n = list(map(int, input().split()))
n.sort() #이진탐색을 위해 정렬

# 몇 개 있는지 구해야 할 카드
M = int(input())
m = list(map(int, input().split()))


for target in m:
    start = 0 
    end = N - 1
    cnt = 0 #몇개있는지 카운팅

    #이진탐색
    while start <= end :
        mid = (start + end) // 2

        if n[mid] == target:
            cnt += 1
            # mid의 앞 뒤를 동시에 탐색. target과 다른 수가 나오기 전까지 탐색.
            i = 0
            while True:
                before = cnt
                i += 1
                if mid+i < N and n[mid + i] == target: #mid의 오른쪽을 조사
                        cnt += 1
                if mid-i >= 0 and n[mid - i] == target: #mid의 왼쪽을 조사
                    cnt += 1 
                if before == cnt:
                    break
            break
                
        elif target < n[mid]:
            end = mid - 1

        else:
            start = mid + 1

    print(cnt, end = " ")
