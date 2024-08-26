# 실패율
def solution(N, stages):
    
    # counter 초기화
    counter = {i:0 for i in range(N+2)}
    # counter 생성
    for i in stages:
        counter[i] += 1
    
    # 실패율 계산
    arr = []
    a = len(stages)
    for s in range(1, N+1):
        
        a = a - counter[s-1]
        b = counter[s]
        
        if a ==0: 
            rate = 0
        else:
            rate = b / a
        
        arr.append((s, rate))
        print(s, a, b)
    
    # 실패율 높은 순서대로 정렬
    arr.sort(key = lambda x:x[1], reverse = True)
    
    # 리턴값 형식으로 만들기
    returns = []
    for i in arr:
        returns.append(i[0])
    
    return returns
        
    
    