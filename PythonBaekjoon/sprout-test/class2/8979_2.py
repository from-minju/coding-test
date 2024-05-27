# 올림픽

n, k = map(int, input().split())
cnt = 0

# medals = [list(map(int, input().split())) for _ in range(n)]
medals = []
for _ in range(n):
    temp = list(map(int, input().split()))
    if temp[0] == k: #k나라인 경우
        mymedal = temp
    medals.append(temp)

# 정렬 (금-은-동 많은 순으로 정렬)
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

# 출력
for arr in medals:
    cnt += 1 #등수 카운팅
    if arr[1:] == mymedal[1:]: # k나라와 금은동 메달수가 모두 같다면
        print(cnt) #등수 출력
        break


