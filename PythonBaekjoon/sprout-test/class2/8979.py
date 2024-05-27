# 올림픽

n, k = map(int, input().split())
medals = [] # k나라를 제외한 나라들의 메달 수, 2차원배열
cnt = 1 #등수 = 자신보다 잘하는 나라 수 + 1이므로 나중에 1을 더하지 않기 위해 미리 1로 초기화

for _ in range(n):
    temp = list(map(int, input().split()))
    if temp[0] == k: #k나라인 경우
        mymedal = temp
    else: #k나라가 아닌 경우
        medals.append(temp)

# k나라보다 잘한 나라의 수를 센다.
for arr in medals:
    # 금메달 수 비교
    if arr[1] > mymedal[1]: #k나라보다 금메달 수가 많다면
        cnt+=1
    elif arr[1] == mymedal[1]: #k나라와 금메달 수가 같다면
        #은메달 수 비교
        if arr[2] > mymedal[2]: #금메달수는 같지만 k나라보다 은메달 수가 많다면
            cnt+=1
        elif arr[2] == mymedal[2]: #금메달수, 은메달 수 모두 같다면
            #동메달 수 비교
            if arr[3] > mymedal[3]:
                cnt+=1
    
print(cnt)




