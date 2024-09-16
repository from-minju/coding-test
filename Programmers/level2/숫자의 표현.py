def solution(n):
    answer = 0
    
    for s in range(1, n+1):
        sum = 0
        for e in range(s, n+1):
            sum += e
            if sum == n: 
                answer += 1
                break
            if sum > n: break
        
    return answer