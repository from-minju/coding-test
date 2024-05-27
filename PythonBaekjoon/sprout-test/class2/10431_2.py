def bubble_sort(List): #정렬할 list, 원소 수 N
    global cnt
    for i in range(len(List)-1, 0, -1) : # 범위의 끝
        for j in range(i) :
            if List[j] > List[j+1] : #현재 항이 다음 항보다 클 경우
                List[j], List[j+1] = List[j+1], List[j] #서로의 위치를 바꿔라
                cnt += 1

t = int(input()) #테스트 케이스 수

for _ in range(t):
    height = list(map(int, input().split()))[1:] #20명의 키 정보
    cnt = 0 #물러서는 횟수

    bubble_sort(height)
    print(_+1, cnt)