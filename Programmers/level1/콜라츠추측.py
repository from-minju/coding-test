def solution(num):
    answer = 0
    
    for i in range(500):
        if num == 1: break
        
        if num % 2 ==0:
            num = num/2
        elif num % 2 !=0:
            num = 3*num + 1
        
        answer = i+1
        
        if num == 1: break
    else:
        answer = -1
        
    return answer