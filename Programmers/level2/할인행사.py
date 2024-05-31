# 할인행사

from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    for i in range(len(discount) - 9):
        
        counter = Counter(discount[i:i+10])
        
        # 원하는 제품 10개가 모두 있는지 확인
        for i in range(len(want)):
            if want[i] in counter and number[i] <= counter[want[i]]:
                continue
            else:
                break
        else: # 원하는 제품이 모두 있다면
            answer += 1 #가능한 날짜를 증가시킴
                  
        
    return answer

want = list(input().split())
number = list(map(int, input().split())) 
discount = list(input().split())

print(solution(want, number, discount))

