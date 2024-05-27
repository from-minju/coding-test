# 줄세우기

t = int(input()) #테스트 케이스 수

for _ in range(t):

    height = list(map(int, input().split()))[1:] #20명의 키 정보
    cnt = 0 #물러서는 횟수

    for i in range(20):
        while i>0: # height의 2번째 학생부터 정렬
            if height[i] < height[i-1]: # 앞의 학생보다 작은경우
                height[i], height[i-1] = height[i-1], height[i] # 앞의 학생과 자리를 바꾼다.
                cnt += 1 # 물러서는 횟수 +1
                i -= 1 #그 다음 앞에 있는 학생과 비교하기위해
            else: break # 앞의 학생보다 큰 경우(정렬할 필요가 없는 경우) 
    
    print(_+1, cnt)



